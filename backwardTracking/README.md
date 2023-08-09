Worked files till now,
------------------
```
combinedGraph/combined-graph.py ##This file will draw graph with 500 edges and nodes using states, but graphs from seperate files e.g., vgr and hbw are not drawn.
```
------------------

Working files,

1. `3test.py` is creating graph for a certain range (1k edges) working fine to find graphs in backward direction.

2. `graphViz-bt-hbw2.py` is creating graph with 1k edges for `hbw-graph.txt`.

3. `graphViz-bt-vgr.py` is creating graph for all the logs present in `../vgr-graph.txt`

4. The `graph without merging` folder is creating graph with `networkx` using all the logs.

5. With this file `graphViz-bt-hbw3.py` tried to make gspan-mining format type of data. But couldn't.

6. **The file `graphViz-bt-hbw4.py`(copy of `..hbw2.py`) will prepare the file in the form of `graph.data` which can be used later for gspan-mining.** => saved this file
	This file will still not prepare the file that is required by gspan-mining bcz of following issues,
		a. Same nodes should have same id/label
		b. Same edges should have same id/label
			[None of that is considered by this file]
		c. So, creating `graphViz-bt-hbw5.py` to consider same edges and same nodes and provide those same id's
			[Problem is if I have same node and edge in the same graph then gspan will not consider that so I will need to create new graph from then on]

7. `graphViz-bt-vgr2.py` is just to check if it is creating the file in the gspan format and working fine. It's a copy of `graphViz-bt-hbw4.py`

8. `graphViz-bt-hbw5.py` is considering same edges and same nodes and providing the same vertices and edges the same id if created earlier in any of the graph.
	* This file is not considering same vertices if defined twice in the same graph.
	* But if 1 or multiple edges is defined multiple times then it creates separate graph with those inside `data/existing_edges.data` file with new graph id and same vertex and edge id.
	* After that, it combines the original file and the existing file inside the combined file - `data/combined_file.data`. **But as I am appending the data from original and existing file to combined file and also the exisiting file is appending data, so that I am not losing all the other data. That's why, before running it again. I should remove the data folder to create the combined and existing file with the original content without using the previous contents.**
	
	[Issues]
	* The `src` and `tgt` of edge is defined in the opposite way in `get_nodes_and_edges(graph)` function. So, `tgt` is source and `src` is `tgt`. This file `graphViz-bt-hbw5.py` links the edges correctly but not manipulating the function `get_nodes_and_edges(graph)` instead replacing while writing it to the `data` files e.g., `f.write(f"e {tgt} {src} {eid}\n")` and `f_existing.write(f"e {tgt} {src} {eid}\n")`.
		

[Note]
1. The `hbw-graph.txt` has `Calling: ...` and `Function: ...` in the same line as it was created using a pass that didn't add new line after the `Calling:...`. But `hbw-graph2.txt` is updated version that has `Calling: ...` and `Function: ...` in separate lines. It was done with this cmd 
	```
	sed -i '/Calling:/s/Function:/\n&/' ../hbw-graph2.txt
	```	
