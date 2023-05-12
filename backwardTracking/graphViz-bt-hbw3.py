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
    ranges = 10
    found = False
    function_call = None
    functions = []
    globals = []
    callInsts = []
    false_block = None
    true_block = None
    current_graph = graphviz.Digraph(f'hbw-graph-{i}')
    graphs = []
    t = 0
    node_id = 0
    edge_id = 0

    with open("hbw-test.data", 'w') as f:
        f.write(f't # {t}\n')
        for line in reversed(input_str.split('\n')):
            #if line.startswith("b"):
            if i == ranges:
                #print(i,line)
                t += 1
                f.write(f't # {t}\n')
                i = 0
                node_id = 0
                edge_id = 0
                functions = []
                globals = []
                callInsts = []
                graphs.append(current_graph)
                current_graph = graphviz.Digraph()
                #break
                if(t>=5):
                    break

            if start_tracking_from in line:
                found = True
              
            #if "g" in line:
            if "Global" in line and found:
                if line.split()[-1] == '1':
                    global_var = line.replace(":","-")
                    current_graph.node(global_var)
                    f.write(f'v {node_id} {global_var}\n')
                    node_id += 1
                    if len(functions) > 0:
                        #current_graph.edge(functions[-1], global_var)
                        current_graph.edge(global_var, functions[-1], dir="back")
                        f.write(f'e {global_var} {functions[-1]} {edge_id}\n')
                        edge_id += 1
                        functions = []
                        i += 1
                        edges += 1
                    elif len(callInsts) > 0:
                        #current_graph.edge(callInsts[-1], global_var)
                        current_graph.edge(global_var, callInsts[-1], dir="back")
                        f.write(f'e {global_var} {callInst[-1]} {edge_id}\n')
                        edge_id += 1
                        callInsts = []
                        i += 1
                        edges += 1
                    elif len(globals) > 0:
                        #current_graph.edge(globals[-1], global_var)
                        current_graph.edge(global_var, globals[-1], dir="back")
                        f.write(f'e {global_var} {globals[-1]} {edge_id}\n')
                        edge_id += 1
                        i += 1
                        edges += 1
                    globals.append(global_var)

            #elif "f" in line and found:
            elif "Function:" in line and found:
                function_name = line.replace("(", "\(").replace(":","-")
                current_graph.node(function_name)
                f.write(f'v {node_id} {function_name}\n')
                node_id += 1
                if len(globals) > 0:
                    #current_graph.edge(globals[-1], function_name)
                    current_graph.edge(function_name, globals[-1], dir="back")
                    f.write(f'e {function_name} {globals[-1]} {edge_id}\n')
                    edge_id += 1
                    globals = []
                    i += 1
                    edges += 1
                elif len(callInsts) > 0:
                    #current_graph.edge(callInsts[-1], function_name)
                    current_graph.edge(function_name, callInsts[-1], dir="back")
                    f.write(f'e {function_name} {callInst[-1]} {edge_id}\n')
                    edge_id += 1
                    callInsts = []
                    i += 1
                    edges += 1
                elif len(functions) > 0:
                    #current_graph.edge(functions[-1], function_name)
                    current_graph.edge(function_name, functions[-1], dir="back")
                    f.write(f'e {function_name} {functions[-1]} {edge_id}\n')
                    edge_id += 1
                    i += 1
                    edges += 1
                functions.append(function_name)

            #elif "c" in line and found:
            elif "Calling" in line and found:
                calling = True
                callInst = line.replace("(", "\(").replace(":","-")
                current_graph.node(callInst)
                f.write(f'v {node_id} {callInst}\n')
                node_id += 1
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


def get_nodes(graph):
    return [node for node in graph.obj_dict['nodes'].keys()]

def write_graph_data_file(graphs, file_path):
    with open(file_path, 'w') as f:
        for i, graph in enumerate(graphs):
            f.write(f't # {i}\n')
            node_mapping = {}
            node_id = 0

            nodes = get_nodes(graph)
            print(graph)
            break
            # Write vertices
            #for node in graph.nodes:
            for node, attr in graph.body[0].items():
                node_mapping[node] = node_id
                label = attr.get('label', '') 
                f.write(f'v {node_id} {label}\n')
                node_id += 1

            # Write edges
            #for edge in graph.edges:
            for edge, attr in graph.body[0].edges:
                source = edge[0]
                target = edge[1]
                label = attr.get('label', '') 
                f.write(f'e {node_mapping[source]} {node_mapping[target]} {label}\n')

            f.write('\n')


graphs = parse_input(input_str)
#write_graph_data_file(graphs, 'hbw.data')

print("total edges: ",edges)
for i, graph in enumerate(graphs):
    graph.render(f'backtrackingGraphsGenerated/graphs-{i+1}/hbw-graph-{i}.png')
    with open(f'backtrackingGraphsGenerated/graphs-{i+1}/hbw-graph-{i}.png') as f:
        dot_graph = f.read()
    graphviz.Source(dot_graph)

