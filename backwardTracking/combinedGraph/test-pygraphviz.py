import pygraphviz as pgv
graph = pgv.AGraph()
graph.add_node("Node1")
graph.add_node("Node2")
graph.add_edge("Node1", "Node2")
graph.draw("graph.png", prog="dot", format="png")
graph.draw(prog="dot")

