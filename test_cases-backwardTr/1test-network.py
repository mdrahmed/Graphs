import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Add edges to the graph
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Draw the graph
nx.draw(G, with_labels=True)

# Show the graph
#plt.show()

# Save the graph as a PDF file
plt.savefig("graph.pdf")

# Save the graph as a PNG file
plt.savefig("graph.png")
