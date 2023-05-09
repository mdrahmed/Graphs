def merge_dot_files(dot_files, output_file):
    with open(output_file, 'w') as out_file:
        for i, dot_file in enumerate(dot_files):
            with open(dot_file) as in_file:
                graph = in_file.read().rstrip()
                # remove '\r' characters from each line
                graph = graph.replace('\r', '')
                # add closing bracket for previous graph
                if i > 0:
                    graph = graph[:-1] + f' -> {prev_graph.split()[0]};\n}}'
                out_file.write(graph)
                prev_graph = graph

dot_files = ['hbw-graph-0.dot', 'hbw-graph-1.dot']
merge_dot_files(dot_files, "merged.dot")
