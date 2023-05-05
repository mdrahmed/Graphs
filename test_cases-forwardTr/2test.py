import graphviz

# working with the txt file
input_str = """
0
c
g 1
f


b

1
c
c
c
g 1
f


b

2
c
c
g 1
g 1
f

b

3
c
c
c
g::: 1
g::: 1
g 1
g 1
f
f
f

b

4
c 1
c 2
c 3
g 3
g 1
f 1
f 2
f 5
f 6 

b

5
k
a
i
c
k
c
lcc
c
jk
ll
l
g 1
k
g 1
m
a
g1
l
j
z
f
k
f
l
"""
start_tracking_from = input("Enter the event name: ")

def parse_input(input_str):
    lines = input_str.split("\n")
    i = 0
    found = False
    function_call = None
    functions = []
    globals = []
    callInsts = []
    false_block = None
    true_block = None
    current_graph = graphviz.Digraph(f'hbw-graph-{i}')
    graphs = []

    for line in lines:
        if line.startswith("b"):
            functions = []
            globals = []
            callInsts = []
            graphs.append(current_graph)
            current_graph = graphviz.Digraph()

        if start_tracking_from in line:
            found = True
          
        if "g" in line:
            if line.split()[-1] == '1':
                global_var = line.replace(":","-")
                current_graph.node(global_var)
                if len(functions) > 0:
                    current_graph.edge(functions[-1], global_var)
                    functions = []
                elif len(callInsts) > 0:
                    current_graph.edge(callInsts[-1], global_var)
                    callInsts = []
                elif len(globals) > 0:
                    current_graph.edge(globals[-1], global_var)
                globals.append(global_var)

        elif "f" in line and found:
            function_name = line.replace(":","-")
            current_graph.node(function_name)
            if len(globals) > 0:
                current_graph.edge(globals[-1], function_name)
                globals = []
            elif len(callInsts) > 0:
                current_graph.edge(callInsts[-1], function_name)
                callInsts = []
            elif len(functions) > 0:
                current_graph.edge(functions[-1], function_name)
            functions.append(function_name)

        elif "c" in line and found:
            calling = True
            callInst = line.replace("(", "\\(").replace(":","-")
            current_graph.node(callInst)
            if len(globals) > 0:
                current_graph.edge(globals[-1], callInst)
                globals = []
            elif len(functions) > 0:
                current_graph.edge(functions[-1], callInst)
                functions = []
            elif len(callInsts) > 0:
                current_graph.edge(callInsts[-1], callInst)
            callInsts.append(callInst)

    graphs.append(current_graph)
    return graphs

graphs = parse_input(input_str)
for i, graph in enumerate(graphs):
    graph.render(f'g/hbw-graph-{i}.png')
    with open(f'g/hbw-graph-{i}.png') as f:
        dot_graph = f.read()
    graphviz.Source(dot_graph)

