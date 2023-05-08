Working files,

1. 2test.py is working properly and it is drawing graphs seperately, it makes a graph when until is sees `b`. It starts making a new graph when it sees `b`. I can use this `b` as a condition to draw gseperate graphs. It's creating graph in the backward direction.

2. graph-hbw2-test.py is a copy of the file ../graph-hbw2.py. Using the 2test.py to check if it's working fine with all test cases and then I will merge the result inside the file graph-hbw2-test.py

3. 3test.py is creating graph for a certain range working fine to find graphs in backward direction.

4. In `networkx` if I use `plt.show()` then it will show us the graph but to save it as a png or pdf, I have to do it before that like following,
```
# Draw the graph
nx.draw(G, with_labels=True)

# Show the graph
#plt.show()

# Save the graph as a PDF file
plt.savefig("graph.pdf")

# Save the graph as a PNG file
plt.savefig("graph.png")
```

Check 1test-network.py file to see the whole code. 
