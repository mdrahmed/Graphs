import graphviz

# working with the txt file
input_str = """
f
g 1
c

b

f
f
f
g 1
c

b

f
g 1
g 1
c

b

f
f
f
g 1
g 1
c

b

f
g 1
c
c
c

b

f
f
g 1
g 1
g 1
c
c
d

f
g 1
c

b

f
f
f
g 1
g 1
c

b

f
g 1
g 1
c

b

f
f
f
g 1
g 1
c

b

f
g 1
c
"""
start_tracking_from = 'f'

def parse_input(input_str):
    lines = input_str.split("\n")
    i = 0
    found = False
    function_call = None
    functions = []
    globals = []
    values = []
    false_block = None
    true_block = None
    current_graph = graphviz.Digraph(f'hbw-graph-{i}')
    graphs = []

    for line in lines:
        if line.startswith("b"):
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
                elif len(values) > 0:
                    current_graph.edge(values[-1], global_var)
                    values = []
                elif len(globals) > 0:
                    current_graph.edge(globals[-1], global_var)
                globals.append(global_var)

        elif "f" in line and found:
            function_name = line.replace(":","-")
            current_graph.node(function_name)
            if len(globals) > 0:
                current_graph.edge(globals[-1], function_name)
                globals = []
            elif len(values) > 0:
                current_graph.edge(values[-1], function_name)
                values = []
            elif len(functions) > 0:
                current_graph.edge(functions[-1], function_name)
            functions.append(function_name)

        elif "c" in line and found:
            calling = True
            value = line.replace("(", "\\(").replace(")", "\\)").replace(":","-").replace(":","-")
            current_graph.node(value)
            if len(globals) > 0:
                current_graph.edge(globals[-1], value)
                globals = []
            elif len(functions) > 0:
                current_graph.edge(functions[-1], value)
                functions = []
            elif len(values) > 0:
                current_graph.edge(values[-1], value)
            values.append(value)

        if i == 1000:
            break

    return graphs

graphs = parse_input(input_str)
for i, graph in enumerate(graphs):
    graph.render(f'hbw-graph-{i}.png')
    with open(f'hbw-graph-{i}.png') as f:
        dot_graph = f.read()
    graphviz.Source(dot_graph)

