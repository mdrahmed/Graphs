import graphviz

# working with the txt file
# with open('test', 'r') as f:
# Path: CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good
with open('/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/hbwall3', 'r') as f:
    input_str = f.read()

start_tracking_from = input("Enter the event name: ")
edges = 0
def parse_input(input_str):
    global edges
    lines = input_str.split("\n")
    i = 0
    ranges = 500
    found = False
    function_call = None
    functions = []
    globals = []
    callInsts = []
    false_block = None
    true_block = None
    current_graph = graphviz.Digraph(f'hbw-graph-{i}')
    graphs = []
    stateful = False
    states = 0

    # for line in reversed(lines):
    for idx, line in enumerate(reversed(lines)):
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
            if len(functions) > 0:
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

        elif "Called" in line and found:
            calling = True
            stateful = False
            # states = 0
            callInst = line.replace("(", "\\(").replace(":","-")
            current_graph.node(callInst)
            if len(globals) > 0:
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

    if(i < ranges):
        graphs.append(current_graph)
    return graphs

graphs = parse_input(input_str)
print("total edges: ",edges)
for i, graph in enumerate(graphs):
    graph.render(f'graph/combined-graph-{i}.dot')
    graph.render(f'graph/combined-graph-{i}.png')
    with open(f'graph/combined-graph-{i}.png') as f:
        dot_graph = f.read()
    graphviz.Source(dot_graph)

