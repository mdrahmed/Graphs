import graphviz
import re
import os

#print(graphviz.__version__)
# working with the txt file
#input_str = open('../hbw-graph-d.txt','r')
with open('../hbw-graph2.txt', 'r') as f:
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
    current_graph = graphviz.Digraph(f'hbw-graph-{i}')
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
            #if prev_line is not None:
            #    line = prev_line
            #break
            #if(t<=5):
            #    break

        if start_tracking_from in line:
            found = True
          
        #if "g" in line:
        if "Global" in line and found:
            if line.split()[-1] == '1':
                global_var = line.replace(":","-")
                if "!dbg" in line:
                    global_var = re.sub(r",\s*!dbg\s*!.*", "",global_var)
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
        #prev_line = line


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

graph_id = 0
node_id = 1
edge_id = 1
node_dict = {}  # Dictionary to store node IDs
edge_dict = {}  # Dictionary to store edge IDs

# Create the 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

original_file = 'data/hbw.data'
existing_file = 'data/existing_edges.data'
existing_file_id = len(graphs)
combined_file = 'data/combined_file.data'

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

for i, graph in enumerate(graphs):
    graph.render(f'backtrackingGraphsGenerated/graphs-{i+1}/hbw-graph-{i}.dot')
    graph.render(f'backtrackingGraphsGenerated/graphs-{i+1}/hbw-graph-{i}.png')
    with open(f'backtrackingGraphsGenerated/graphs-{i+1}/hbw-graph-{i}.png') as f:
        dot_graph = f.read()
    graphviz.Source(dot_graph)

## Reading existing and original data takes like forever.
### Combining the original file in the combined file
#with open(original_file, 'r') as f_source:
#    original_contents = f_source.read()
#with open(combined_file, 'a') as f_combined:
#    f_combined.write(original_contents)
#
### Combining the existing file in the combined file
#with open(existing_file, 'r') as f_source:
#    existing_contents = f_source.read()
#with open(combined_file, 'a') as f_combined:
#    f_combined.write(existing_contents)


## Only appending to original data
with open(existing_file, 'r') as f_source:
    existing_contents = f_source.read()
with open(original_file, 'a') as f_combined:
    f_combined.write(existing_contents)
