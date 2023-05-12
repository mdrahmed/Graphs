import graphviz
print(graphviz.__version__)
# working with the txt file
#input_str = open('../hbw-graph-d.txt','r')
with open('../vgr-graph.txt', 'r') as f:
    input_str = f.read()

start_tracking_from = input("Enter the event name: ")
#start_tracking_from = "Calling" 
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
    current_graph = graphviz.Digraph(f'vgr-graph-{i}')
    graphs = []
    t = 0

    for line in reversed(input_str.split('\n')):
        #if line.startswith("b"):
        if i == ranges:
            #print(i,line)
            t += 1
            i = 0
            functions = []
            globals = []
            callInsts = []
            graphs.append(current_graph)
            current_graph = graphviz.Digraph()
            #break
            #if(t<=5):
            #    break

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
            #current_graph.node(callInst)

            ## The Topic should be removed from the logs with the pass
            position = callInst.find("Topic from")
            if position != -1:
                # Extract the substring before "Topic"
                callInst = callInst[:position].strip()
            callee = callInst.split()[-1]
            if "Topic from" in callInst:
                print("Callee: ",callee, "callInst: ",callInst)
            current_graph.node(callee)
            if len(globals) > 0:
                #current_graph.edge(callInst, globals[-1], dir="back")
                current_graph.edge(callee, globals[-1], dir="back")
                globals = []
                i += 1
                edges += 1
            elif len(functions) > 0:
                #current_graph.edge(callInst, functions[-1], dir="back")
                current_graph.edge(callee, functions[-1], dir="back")
                functions = []
                i += 1
                edges += 1
            elif len(callInsts) > 0:
                #current_graph.edge(callInst, callInsts[-1], dir="back")
                current_graph.edge(callee, callInsts[-1], dir="back")
                i += 1
                edges += 1
            #callInsts.append(callInst)
            callInsts.append(callee)

    if(i < ranges):
        graphs.append(current_graph)
    return graphs

# Function to extract nodes and edges from a graph object
def get_nodes_and_edges(graph):
    nodes = []
    edges = []
    for obj in graph.body:
        #print("\n\nobj:",obj)
        if '->' in obj:
            # It's an edge
            edge_parts = obj.split('->')
            src = edge_parts[0].strip()
            src = src.replace(" ","").replace("Function-","").replace("Calling-","")
            tgt = edge_parts[1].strip()
            tgt = tgt.replace(" ","").replace("Function-","").replace("Calling-","")
            #print("src,tgt:",src,tgt)
            if "Topicfrom" in src or "Topicfrom" in tgt:
                print("edge:",obj)
            edges.append((src, tgt))
        else:
            # It's a node
            node_label = obj.strip()
            node_label = node_label.replace(" ", "").replace("Function-","").replace("Calling-","")
            #print("node:",node_label)
            if "Topicfrom" in node_label:
                print("node:",obj)
            nodes.append(node_label)
    #for tail, head in graph.iteredges():
    #    print(tail,head)
    #    edges.append((tail, head))
    return nodes, edges


graphs = parse_input(input_str)
#nodes,edges = get_nodes_and_edges(graph)
#print("nodes:",nodes,"edges: ",edges)
print("total edges: ",edges)

with open('vgr.data', 'w') as f:
    #f.write(f"t # 0\n")
    for i, graph in enumerate(graphs):
    
        nodes,edges = get_nodes_and_edges(graph)
        #print("i:",i,"\nnodes:",nodes,"\nedges: ",edges)
    
        # Write the graph ID (t line)
        f.write(f"t # {i}\n")
        
        node_id = 1
        #print(f"Nodes (Graph {i+1}):")
        for node in nodes:
            #print(f"Node: {node}")
            f.write(f"v {node} {node_id}\n")
            node_id += 1
        
        edge_id = 1
        #print(f"Edges (Graph {i+1}):")
        for src, tgt in edges:
            tgt = tgt.replace("[dir=back]", "")
            #print(f"Source: {src}, \nTarget: {tgt}")
            f.write(f"e {src} {tgt} {edge_id}\n")
            edge_id += 1 ## Not using edge this time
    
        graph.render(f'backtrackingGraphsGenerated-vgr/graphs-{i+1}/vgr-graph-{i}.dot')
        graph.render(f'backtrackingGraphsGenerated-vgr/graphs-{i+1}/vgr-graph-{i}.png')
        with open(f'backtrackingGraphsGenerated-vgr/graphs-{i+1}/vgr-graph-{i}.png') as f_in:
            dot_graph = f_in.read()
        graphviz.Source(dot_graph)
    
