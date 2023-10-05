import graphviz
import pygraphviz as pgv
from collections import defaultdict
from termcolor import colored
import os

# working with the txt file
# with open('test', 'r') as f:
# Path: CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good
# with open('/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/motivation-log-test', 'r') as f:
## delivery-underflow
#with open('/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/delivery-underflow/motivation-log-v2-delivery', 'r') as f: ##Storing 1 workpiece --Input: `hbw/ack`
#with open('/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/delivery-underflow/motivation-log-v3', 'r') as f: ##Storing 9 workpiece
# store-overflow
#with open('/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/store-overflow/motivation-log-v2-store', 'r') as f: ##look at the folder, it has descriptive names
#    input_str = f.read()

## delivery-underflow with readable function calls.
with open('/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/hbwall3', 'r') as f: 
    input_str = f.read()


start_tracking_from = input("Enter the event name: ")
# print("type of start_tracking_from:",type(start_tracking_from))
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
    separate_file = False
    global_states = 0
    function_states = 0
    callInst_states = 0
    msg_topic_states = 0
    pub_topic_states = 0
    prev_posi = -1
    prev_posj = -1
    # print("starting prev_posi",prev_posi,"prev_posj",prev_posj)

    # for line in reversed(lines):
    for idx, line in enumerate(reversed(lines)):
        # print(line)
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
        #if "#vgr" in line:
        #    # print("#vgr found",line)
        #    # if topics["message_arrived"]:
        #        # print("file break found",line, "topics[message_arrived]:",topics["message_arrived"])
        #    start_tracking_from = "get_topic"
        #    # print(type(start_tracking_from))
        #    found = False
        #    separate_file = True
        #    functions = []
        #    globals = []
        #    callInsts = []
        #    # msg_topic_states = 0
        #    # pub_topic_states = 0

        if start_tracking_from in line:
            found = True
        
        # if "loaded" in line and found:
        #     #if line.split()[-1] == '1':
        #     global_var = line.replace(":","-")
        #     if len(functions) > 0 and "isValidPos" in functions[-1]:
        #         stateful = True
        #     if stateful: 
        #         global_states += 1
        #         global_var += " - state {}".format(global_states)
        #     current_graph.node(global_var)
        #     if len(topics_current) > 0:
        #         #current_graph.edge(topics_current[-1], topics[topic_func])
        #         current_graph.edge(global_var, topics_current[-1], dir="back")
        #         topics_current = []
        #         i += 1
        #         edges += 1
        #     elif len(functions) > 0:
        #         #current_graph.edge(functions[-1], global_var)
        #         current_graph.edge(global_var, functions[-1], dir="back")
        #         functions = []
        #         i += 1
        #         edges += 1
        #     elif len(callInsts) > 0:
        #         #current_graph.edge(callInsts[-1], global_var)
        #         current_graph.edge(global_var, callInsts[-1], dir="back")
        #         callInsts = []
        #         i += 1
        #         edges += 1
        #     elif len(globals) > 0:
        #         #current_graph.edge(globals[-1], global_var)
        #         current_graph.edge(global_var, globals[-1], dir="back")
        #         i += 1
        #         edges += 1
        #     # print(global_var)
        #     globals.append(global_var)

        if "Function" in line and found:
            collision = False
            function_name = line.replace(":","-")
            stateful = False
            #function_name += '\n'
            forward_idx = len(lines) - idx
            #for next_line in lines[forward_idx:]:
            #    # print(next_line)
            #    next_line = next_line.replace(":","-")
            #    # print(next_line)
            #    function_name += next_line + '\n'
            #    if "Position" in next_line:
            #        posi = int(next_line.split()[-2])
            #        posj = int(next_line.split()[-1])
            #        # print("next_line",next_line,"posi",posi,"posj",posj)
            #        # if posi == prev_posi and posj == prev_posj:
            #        if prev_posi == -1 and prev_posj == -1:
            #            # As the file is traversed backwards, the collision will be detected after the collision happens, so considering the
            #            # 1st function node as the collision node
            #            print(colored("Collision detected", "red"))
            #            collision = True
            #        # print("prev_posi",prev_posi,"prev_posj",prev_posj)
            #        prev_posi = posi
            #        prev_posj = posj
            #    # elif "Table" in next_line:
            #    #     table = next_line.split()
            #    #     print(table)
            #    #     # Find the index where 'Table-' appears in the list
            #    #     table_index = table.index('Table-')
            #    #     # Create a 3x3 list starting from the element after 'Table-'
            #    #     table_list = [table[table_index+1 : table_index+4],
            #    #                 table[table_index+4 : table_index+7],
            #    #                 table[table_index+7 : table_index+10]]
            #    #     if posj == 2:
            #    #         posj = 0
            #    #     elif posj == 0:
            #    #         posj = 2
            #    #     print(table_list,function_name)
            #    #     if table_list[posi][posj] == '0' and "TxtHighBayWarehouseStorage5fetch" in function_name:
            #    #         print(colored("Collision detected", "red"))
            #    #         collision = True
            #    #     elif table_list[posi][posj] == '1' and "TxtHighBayWarehouseStorage14fetchContainer" in function_name:
            #    #         print(colored("Collision detected", "red"))
            #    #         collision = True

            #    if "arg_values" in next_line:
            #        break
            function_states += 1
            #function_name += " - state {}".format(function_states)
            if collision:
                current_graph.node(function_name, style='filled', fillcolor='red')
                collision = False
            else:
                current_graph.node(function_name)
            # print("topics_current inside function:",topics_current)
            
            ## to pickup
            #if "requestVGRfetchContainer" in line: 
            #    fetchContainer = function_name
            #elif "TxtDeliveryPickupStation6is_DIN" in line:
            #    sensor_name = "u16LastStateDIN,reqUpdateDIN => sensor"
            #    current_graph.node(sensor_name, style='filled', fillcolor='cornflowerblue')
            #    current_graph.edge(sensor_name, function_name, dir="back")

            #if len(topics_current) > 0:
            #    #current_graph.edge(topics_current[-1], topics[topic_func])
            #    # print("topics_current inside function if:",topics_current)
            #    current_graph.edge(function_name, topics_current[-1], dir="back")
            #    topics_current = []
            #    i += 1
            #    edges += 1
            if len(globals) > 0:
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
            functions.append(function_name)

        #elif "Called" in line and found:
        #    calling = True
        #    stateful = False
        #    callInst = line.replace("(", "\\(").replace(":","-")
        #    callInst_states += 1
        #    #callInst += " - state {}".format(callInst_states)
        #    current_graph.node(callInst)
        #    #if "PickupStation" in line:
        #    #    current_graph.edge(fetchContainer, callInst)
        #    if len(topics_current) > 0:
        #        #current_graph.edge(topics_current[-1], topics[topic_func])
        #        current_graph.edge(callInst, topics_current[-1], dir="back")
        #        topics_current = []
        #        i += 1
        #        edges += 1
        #    elif len(globals) > 0:
        #        #current_graph.edge(globals[-1], callInst)
        #        current_graph.edge(callInst, globals[-1], dir="back")
        #        globals = []
        #        i += 1
        #        edges += 1
        #    elif len(functions) > 0:
        #        #current_graph.edge(functions[-1], callInst)
        #        current_graph.edge(callInst, functions[-1], dir="back")
        #        functions = []
        #        i += 1
        #        edges += 1
        #    #elif len(topics_current) > 0:
        #    #    #current_graph.edge(topics_current[-1], topics[topic_func])
        #    #    current_graph.edge(callInst, topics_current[-1], dir="back")
        #    #    topics_current = []
        #    #    i += 1
        #    #    edges += 1
        #    elif len(callInsts) > 0:
        #        #current_graph.edge(callInsts[-1], callInst)
        #        current_graph.edge(callInst, callInsts[-1], dir="back")
        #        i += 1
        #        edges += 1
        #    callInsts.append(callInst)

        #elif "get_topic" in line and found:
        #    topic_line = line.replace(":","-")
        #    topic_func = line.split()[0]
        #    
        #    similar_topic = False
        #    if topic_func == "publish":
        #        pub_topic_states += 1
        #        topic_line += " - state {}".format(pub_topic_states)
        #        # print("topic:",topic_line, "topics msg:",topics["message_arrived"])
        #        if 'f/i' in topic_line or 'f/o' in topic_line:
        #            current_graph.node("Server", style='filled', fillcolor='green')
        #            current_graph.edge(topic_line, "Server", dir="back")
        #        else:
        #            current_graph.node(topic_line)
        #            topics[topic_func].append(topic_line)
        #            for topic in topics["message_arrived"]:
        #                if topic.split()[3] == topic_line.split()[3] and separate_file:
        #                    similar_topic = True
        #                    # pub_state = topic.split()[-1]
        #                    # topic_line += " - state {}".format(pub_state)
        #                    current_graph.edge(topic, topic_line)
        #                    topics["message_arrived"].remove(topic)
        #                    # print("pub_state",topic_line.split()[3])
        #                    break
        #        # if not similar_topic and len(topics["message_arrived"]) > 0:
        #        #     pub_topic_states += 1
        #        #     topic_line += " - state {}".format(pub_topic_states)
        #        #     print("pub_topic_states",topic_line)
        #    elif topic_func == "message_arrived":
        #        msg_topic_states += 1
        #        topic_line += " - state {}".format(msg_topic_states)
        #        if 'f/i' in topic_line or 'f/o' in topic_line:
        #            current_graph.node("Server", style='filled', fillcolor='green')
        #            current_graph.edge("Server", topic_line, dir="back")
        #        else:
        #            current_graph.node(topic_line)
        #            # print("topic_line:",topic_line, "topics pub:",topics["publish"])
        #            topics[topic_func].append(topic_line)
        #            # print("topics msg:", topics["message_arrived"])
        #            for topic in topics["publish"]:
        #                # print("topic:",topic.split()[3], "topic_line.split()[3]",topic_line.split()[3])
        #                if topic.split()[3] == topic_line.split()[3] and separate_file:
        #                    similar_topic = True
        #                    # msg_state = topic.split()[-1]
        #                    # topic_line += " - state {}".format(msg_state)
        #                    current_graph.edge(topic, topic_line)
        #                    topics["publish"].remove(topic)
        #                    # print("msg_state",topic_line.split()[3])
        #                    break
        #                
        #    # This part is for the case when I need to draw the graph without complete vgr edges
        #    # if similar_topic:
        #    #     # similar_topic = False
        #    #     globals = []
        #    #     functions = []
        #    # print("topic_line after similar if:",topic_line)
        #    # print("functions after similar if:",functions)
        #    if len(globals) > 0:
        #        #current_graph.edge(globals[-1], topics[topic_func])
        #        current_graph.edge(topic_line, globals[-1], dir="back")
        #        globals = []
        #        i += 1
        #        edges += 1
        #    elif len(functions) > 0:
        #        #current_graph.edge(functions[-1], topics[topic_func])
        #        current_graph.edge(topic_line, functions[-1], dir="back")
        #        functions = []
        #        i += 1
        #        edges += 1
        #    elif len(callInsts) > 0:
        #        #current_graph.edge(callInsts[-1], topics[topic_func])
        #        current_graph.edge(topic_line, callInsts[-1], dir="back")
        #        callInsts = []
        #        i += 1
        #        edges += 1
        #    elif len(topics_current) > 0 and not similar_topic:
        #        #current_graph.edge(topics_current[-1], topics[topic_func])
        #        current_graph.edge(topic_line, topics_current[-1], dir="back")
        #        topics_current = []
        #        similar_topic = False
        #        i += 1
        #        edges += 1
        #    # current_graph.node(topic)
        #    topics_current.append(topic_line)
        #    # print("topics_current inside get_topic:",topics_current)  

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

## THIS FOLLOWING PART WILL GENERATE GRAPH
for i, graph in enumerate(graphs):
    graph.render(f'graphsGeneratedForGspan/combined-graph-{i}.dot')
    

# THIS PART WILL GENERATE GSPAN DATA FORMAT FOR GPSAN INPUT
graph_id = 0
node_id = 1
edge_id = 1
node_dict = {}  # Dictionary to store node IDs
edge_dict = {}  # Dictionary to store edge IDs

## Function to extract nodes and edges from a graph object
def get_nodes_and_edges(graph):
    nodes = []
    edges = []
    for obj in graph.body:
        #print("\n\nobj:",obj)
        if '->' in obj:
            # It's an edge
            edge_parts = obj.split('->')
            src = edge_parts[0].strip()
            #src = src.replace(" ","").replace("Function-","").replace("Calling-","")
            # To remove FFF and Calledfrom is there, to remove Calledfrom-, I will need to understand a lot of stuff. So, I just need functions, lets work with functions.
            src = src.replace(" ","").replace("FFFFunction-","").replace("Calling-","").replace("Called-","")
            #print(src)
            #break
            tgt = edge_parts[1].strip()
            tgt = tgt.replace(" ","").replace("FFFFunction-","").replace("Calling-","")
            #print("src,tgt:",src,tgt)
            if "Topicfrom" in src or "Topicfrom" in tgt:
                print("edge:",obj)
            edges.append((src, tgt))
        else:
            # It's a node
            node_label = obj.strip()
            node_label = node_label.replace(" ", "").replace("FFFFunction-","").replace("Calling-","")
            #print("node:",node_label)
            if "Topicfrom" in node_label:
                print("node:",obj)
            nodes.append(node_label)
    #for tail, head in graph.iteredges():
    #    print(tail,head)
    #    edges.append((tail, head))
    return nodes, edges

## Create the 'data' folder if it doesn't exist
if not os.path.exists('data-gspan'):
    os.makedirs('data-gspan')
original_file = 'data-gspan/hbw.data'
existing_file = 'data-gspan/existing_edges.data'
existing_file_id = len(graphs)
combined_file = 'data-gspan/combined_file.data'

with open(original_file, 'w') as f:
    #f.write(f"t # 0\n")
    for i, graph in enumerate(graphs):
    
        nodes,edges = get_nodes_and_edges(graph)
        #print("i:",i,"\nnodes:",nodes,"\nedges: ",edges)
    
        # Write the graph ID (t line)
        #f.write(f"t # {i}\n")
        f.write(f"\nt # {i}\n")
        
        nodes_new = [] # For same graph, there should not be multiple same vertices
        edges_new = [] # For same graph, if there is multiple edges then those should be smaller graphs

        #node_id = 1
        #print(f"Nodes (Graph {i+1}):")
        for node in nodes:
            #print(f"Node: {node}")
            if node not in nodes_new:
                #nodes_new.append(node)
                if node not in node_dict:
                    node_dict[node] = node_id
                    node_id += 1

                nid = node_dict[node]
                f.write(f"v {node} {nid}\n")
            nodes_new.append(node)
        
        #edge_id = 1
        #print(f"Edges (Graph {i+1}):")
        for src, tgt in edges:
            tgt = tgt.replace("[dir=back]", "")
            #print(f"Source: {src}, \nTarget: {tgt}")
            if (src,tgt) not in edges_new:
                #edges_new.append((src,tgt))
                if (src,tgt) not in edge_dict: 
                    edge_dict[(src,tgt)] = edge_id
                    edge_id += 1
                
                eid = edge_dict[(src,tgt)]
                f.write(f"e {tgt} {src} {eid}\n") 
                ## mistake made earlier, src become target and target became source, now just replaced the src and tgt and it should be "e {tgt} {src}\n"
                #edge_id += 1 ## Not using edge this time
            else: 
                # Write the existing edge to the separate file
                with open(existing_file, 'a') as f_existing:
                    ## the existing file is in append mode so, that whenever I open it will keep the previous data
                    f_existing.write(f"\nt # {existing_file_id}\n")
                    existing_file_id += 1
                    # vertices
                    if tgt not in node_dict:
                        node_dict[tgt] = node_id
                        node_id += 1
                    
                    nid = node_dict[tgt]
                    f_existing.write(f"v {tgt} {nid}\n")
                    
                    if src not in node_dict:
                        node_dict[src] = node_id
                        node_id += 1
                
                    nid = node_dict[src]
                    f_existing.write(f"v {src} {nid}\n")
                

                    if (src,tgt) not in edge_dict:
                        edge_dict[(src,tgt)] = edge_id
                        edge_id += 1

                    eid = edge_dict[(src,tgt)]
                    f_existing.write(f"e {tgt} {src} {eid}\n")

            edges_new.append((src,tgt))
        #graph.render(f'backtrackingGraphsGenerated/graphs-{i+1}/hbw-graph-{i}.dot')
        #graph.render(f'backtrackingGraphsGenerated/graphs-{i+1}/hbw-graph-{i}.png')
        #with open(f'backtrackingGraphsGenerated/graphs-{i+1}/hbw-graph-{i}.png') as f_in:
        #    dot_graph = f_in.read()
        #graphviz.Source(dot_graph)

## Only appending to original data
if os.path.exists(existing_file):
    with open(existing_file, 'r') as f_source:
        existing_contents = f_source.read()
        print("existing_file contents are written.")
else:
    print(f"existing_file not found inside data-gspan/")

if os.path.exists(original_file) and os.path.exists(existing_file):
    with open(original_file, 'a') as f_combined:
        f_combined.write(existing_contents)
        print(f"existing_file has been combined to the {original_file}.")
else:
    print(f"Can't append existing_file to original_file.\nBecause existing_file was not created yet, check inside data-gspan/")


