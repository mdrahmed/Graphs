# Need to remove hbw nodes that comes after vgr publish node and nodes after that
from collections import defaultdict
import graphviz
import pygraphviz as pgv


# working with the txt file
# with open('test', 'r') as f:
# Path: CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good
# def read_file(file):
#     with open('test-files/'+file, 'r') as f:
#         return f.read()
with open('test-files/hbw', 'r') as f:
    input_str = f.read()

start_tracking_from = input("Enter the event name: ")
print("type of start_tracking_from:",type(start_tracking_from))
topics = defaultdict(list)
edges = 0
def parse_input(input_str):
    global edges
    global start_tracking_from
    lines = input_str.split("\n")
    i = 0
    ranges = 500
    found = False
    function_call = None
    functions = []
    globals = []
    callInsts = []
    topics_current = []
    false_block = None
    true_block = None
    current_graph = graphviz.Digraph(f'graph-{i}')
    graphs = []
    stateful = False
    states = 0

    # for line in reversed(lines):
    for idx, line in enumerate(reversed(lines)):
        print(line)
        #if line.startswith("b"):
        if i == ranges:
            # print(i,line)
            i = 0
            functions = []
            globals = []
            callInsts = []
            graphs.append(current_graph)
            current_graph = graphviz.Digraph()
            # print(idx)
            # break
        if "#vgr" in line:
            print("#vgr found",line)
            if topics["message_arrived"]:
                print("file break found",line, "topics[message_arrived]:",topics["message_arrived"])
                start_tracking_from = "topic"
                print(type(start_tracking_from))
                found = False

        if start_tracking_from in line:
            found = True
          
        if "loaded" in line and found:
            #if line.split()[-1] == '1':
            global_var = line.replace(":","-")
            if len(functions) > 0 and "isValidPos" in functions[-1]:
                stateful = True
            if stateful: 
                states += 1
                global_var += " - state {}".format(states)
            current_graph.node(global_var)
            if len(topics_current) > 0:
                #current_graph.edge(topics_current[-1], topics[topic_func])
                current_graph.edge(global_var, topics_current[-1], dir="back")
                topics_current = []
                i += 1
                edges += 1
            elif len(functions) > 0:
                #current_graph.edge(functions[-1], global_var)
                current_graph.edge(global_var, functions[-1], dir="back")
                functions = []
                i += 1
                edges += 1
            elif len(callInsts) > 0:
                #current_graph.edge(callInsts[-1], global_var)
                current_graph.edge(global_var, callInsts[-1], dir="back")
                callInsts = []
                i += 1
                edges += 1
            elif len(globals) > 0:
                #current_graph.edge(globals[-1], global_var)
                current_graph.edge(global_var, globals[-1], dir="back")
                i += 1
                edges += 1
            # elif len(topics_current) > 0:
            #     #current_graph.edge(topics_current[-1], topics[topic_func])
            #     current_graph.edge(global_var, topics_current[-1], dir="back")
            #     topics_current = []
            #     i += 1
            #     edges += 1
            # print(global_var)
            globals.append(global_var)

        elif "Function" in line and found:
            function_name = line.replace(":","-")
            stateful = False
            function_name += '\n'
            forward_idx = len(lines) - idx
            for next_line in lines[forward_idx:]:
                # print(next_line)
                next_line = next_line.replace(":","-")
                # print(next_line)
                function_name += next_line + '\n'
                if "arg_values" in next_line:
                    break
            current_graph.node(function_name)
            if len(topics_current) > 0:
                #current_graph.edge(topics_current[-1], topics[topic_func])
                current_graph.edge(function_name, topics_current[-1], dir="back")
                topics_current = []
                i += 1
                edges += 1
            elif len(globals) > 0:
                #current_graph.edge(globals[-1], function_name)
                current_graph.edge(function_name, globals[-1], dir="back")
                globals = []
                i += 1
                edges += 1
            elif len(callInsts) > 0:
                #current_graph.edge(callInsts[-1], function_name)
                current_graph.edge(function_name, callInsts[-1], dir="back")
                callInsts = []
                i += 1
                edges += 1
            elif len(functions) > 0:
                #current_graph.edge(functions[-1], function_name)
                current_graph.edge(function_name, functions[-1], dir="back")
                i += 1
                edges += 1
            # elif len(topics_current) > 0:
            #     #current_graph.edge(topics_current[-1], topics[topic_func])
            #     current_graph.edge(function_name, topics_current[-1], dir="back")
            #     topics_current = []
            #     i += 1
            #     edges += 1
            functions.append(function_name)

        elif "Called" in line and found:
            calling = True
            stateful = False
            # states = 0
            callInst = line.replace("(", "\\(").replace(":","-")
            current_graph.node(callInst)
            if len(topics_current) > 0:
                #current_graph.edge(topics_current[-1], topics[topic_func])
                current_graph.edge(callInst, topics_current[-1], dir="back")
                topics_current = []
                i += 1
                edges += 1
            elif len(globals) > 0:
                #current_graph.edge(globals[-1], callInst)
                current_graph.edge(callInst, globals[-1], dir="back")
                globals = []
                i += 1
                edges += 1
            elif len(functions) > 0:
                #current_graph.edge(functions[-1], callInst)
                current_graph.edge(callInst, functions[-1], dir="back")
                functions = []
                i += 1
                edges += 1
            elif len(callInsts) > 0:
                #current_graph.edge(callInsts[-1], callInst)
                current_graph.edge(callInst, callInsts[-1], dir="back")
                i += 1
                edges += 1
            callInsts.append(callInst)

        elif "topic" in line and found:
            topic_line = line.replace(":","-")
            topic_func = line.split()[0]
            print(topic_func)
            # if topic_func not in topics:
            #     topics[topic_func] = []
            # topic = "topic- "+line.split()[-1]
            topics[topic_func].append(topic_line)
            # topics[topic_func].append(line.split()[-1])
            print(topics)
            current_graph.node(topic_line)


            if topic_func == "publish":
                print("topic:",topic_line,topics["message_arrived"])
                for topic in topics["message_arrived"]:
                    if topic.split()[-1] == topic_line.split()[-1]:
                        current_graph.edge(topic, topic_line)
                        topics["message_arrived"].remove(topic)
                        topics["publish"].pop()
                        print("topics:",topics)
                        globals = []
                        functions = []
                        break
            # if len(topics_current) > 0:
            #     #current_graph.edge(topics_current[-1], topics[topic_func])
            #     current_graph.edge(topic_line, topics_current[-1], dir="back")
            #     topics_current = []
            #     i += 1
            #     edges += 1
            if len(globals) > 0:
                #current_graph.edge(globals[-1], topics[topic_func])
                current_graph.edge(topic_line, globals[-1], dir="back")
                globals = []
                i += 1
                edges += 1
            elif len(functions) > 0:
                #current_graph.edge(functions[-1], topics[topic_func])
                current_graph.edge(topic_line, functions[-1], dir="back")
                functions = []
                i += 1
                edges += 1
            elif len(callInsts) > 0:
                #current_graph.edge(callInsts[-1], topics[topic_func])
                current_graph.edge(topic_line, callInsts[-1], dir="back")
                i += 1
                edges += 1
            elif len(topics_current) > 0:
                #current_graph.edge(topics_current[-1], topics[topic_func])
                current_graph.edge(topic_line, topics_current[-1], dir="back")
                topics_current = []
                i += 1
                edges += 1
            
            # current_graph.node(topic)
            topics_current.append(topic_line)

    if(i < ranges):
        graphs.append(current_graph)
    return graphs

# graphs = []
graphs = parse_input(input_str)
# print(type(graphs))
# for file in files:
#     # graphs.extend(parse_input(read_file(file)))
#     input_str = read_file(file)
#     graphs.extend(parse_input(input_str))
    
print("total edges: ",edges)
for i, graph in enumerate(graphs):
    graph.render(f'test-files/combined-graph-{i}.dot')
    # graph.render(f'test-files/combined-graph-{i}.png')
    #with open(f'hbw-graph/hbw-graph-{i}.png') as f:
    #    dot_graph = f.read()
    #graphviz.Source(dot_graph)
    
    # dot_graph = pgv.AGraph(f'hbw-graph/hbw-graph-{i}.dot')
    # search_str = "isValidPos"
    # for node in dot_graph.nodes():
    #     if search_str in node.get_name():
    #         print(f"String found in graph {i}: {node}")
    #         break


