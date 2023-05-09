import graphviz

# working with the txt file
#input_str = open('../hbw-graph-d.txt','r')
with open('../hbw-graph.txt', 'r') as f:
    input_str = f.read()

start_tracking_from = input("Enter the event name: ")
edges = 0
def parse_input(input_str):
    global edges
    #lines = input_str.split("\n")
    i = 0
    ranges = 1000
    found = False
    function_call = None
    functions = []
    globals = []
    callInsts = []
    false_block = None
    true_block = None
    current_graph = graphviz.Digraph(f'hbw-graph-{i}')
    graphs = []

    for line in reversed(input_str.split('\n')):
        #if line.startswith("b"):
        if i == ranges:
            #print(i,line)
            i = 0
            functions = []
            globals = []
            callInsts = []
            graphs.append(current_graph)
            current_graph = graphviz.Digraph()
            #break

        if start_tracking_from in line:
            found = True
          
        #if "g" in line:
        if "Global" in line and found:
            if line.split()[-1] == '1':
                global_var = line.replace(":","-")
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
                globals.append(global_var)

        #elif "f" in line and found:
        elif "Function:" in line and found:
            function_name = line.replace("(", "\(").replace(":","-")
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

        #elif "c" in line and found:
        elif "Calling" in line and found:
            calling = True
            callInst = line.replace("(", "\(").replace(":","-")
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
    graph.render(f'backtrackingGraphsGenerated/graphs-{i+1}/hbw-graph-{i}.png')
    with open(f'backtrackingGraphsGenerated/graphs-{i+1}/hbw-graph-{i}.png') as f:
        dot_graph = f.read()
    graphviz.Source(dot_graph)

