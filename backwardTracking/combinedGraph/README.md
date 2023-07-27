Worked files till now,
------------------
1. All logs are combined to create a simple file,
```
./combined-graph-v3.py ##This file is a copy of ./combined-graph-v2.py, I used this to draw the motivation part of the paper. 
```
The motivation part will show following,<br/>
To storage initially,<br/>
0 0 0<br/>
0 0 0<br/>
0 0 0<br/>

Storing 1 workpiece at (0,2),<br/>
1 0 0<br/>
0 0 0<br/>
0 0 0<br/>

Delievering 1 workpiece from (1,0) - [COLLISION-THE CONTAINER AT PLACE (1,0) IS EMPTY, NOTHING IS DELIVERED],<br/>
1 0 0<br/>
0 0 0<br/>
0 0 0<br/>

The table index is following,<br/>
j\i 2 1 0<br/>
0   - - -<br/>
1   - - -<br/>
2   - - -<br/>

The graph should show function calls with table and wp position, call instructions but not global variables. This file `./combined-graph-v3.py` is working fine with all the corner cases. If it finds a `message_arrived get_topic` and finds similar `publish get_topic` then it will **link these two nodes with same states.** This is shown in `motivation-part-graphs-test`. All the original graphs are present in `motivation-part-graphs` folder.

```
./combined-graph.py ##This file will draw graph with 500 edges and nodes using states, but graphs from seperate files e.g., vgr and hbw are not drawn.
```
In this file, I have found all the graphs and nodes with `isValidPos`, check to file at the end to search a different string,
```
./combined-graph-v2.py ## This is the copy of `combined-graph.py` but contains states for everything e.g., functions, callinsts and variables has states
```
Need to check if I need all the states.

```
./test-combined.py
```
This file `test-combined.py` is using the test dataset present inside the `test-files` dir and using that to draw graphs with `topics` and the it's drawing from `hbw` to `vgr` when it finds a `publish` funciton then it checks if similar `topic` is received the `message_arrived` function. If it does then it creates another branch with the new file and keep doing the same otherwise it will just add the functions,callInsts and variables from same file.
That file uses `#file-name` to identify new files.

2. To generate graph of one-log e.g., `hbw`/`vgr`/`mpo`/`sld`
```
./one-file-graph.py ##This file will draw graph with 500 edges and nodes using states. It is using this to draw graphs for `hbw` - `~/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/hbwall3`
```
This file has `isValidPos` function in following graphs.
```
(cpsenv) raihan@raihan-XPS-8940:~/Graphs-all/Graphs/backwardTracking/combinedGraph$ python3 one-file-graph.py
Enter the event name: isValidPos
total edges:  671476
String found in graph 0: Called from- _ZN2ft26TxtHighBayWarehouseStorage5fetchENS_11TxtWPType_tE _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values- -1
String found in graph 251: Called from- _ZN2ft26TxtHighBayWarehouseStorage14storeContainerEv _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values- -1
String found in graph 347: Called from- _ZN2ft26TxtHighBayWarehouseStorage5fetchENS_11TxtWPType_tE _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values- -1
String found in graph 647: Called from- _ZN2ft26TxtHighBayWarehouseStorage14storeContainerEv _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values- -1
String found in graph 762: Called from- _ZN2ft26TxtHighBayWarehouseStorage5fetchENS_11TxtWPType_tE _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values- -1
String found in graph 874: Called from- _ZN2ft26TxtHighBayWarehouseStorage5storeENS_12TxtWorkpieceE _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values- -1
String found in graph 937: Called from- _ZN2ft26TxtHighBayWarehouseStorage14fetchContainerEv _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values- -1
String found in graph 1234: Called from- _ZN2ft26TxtHighBayWarehouseStorage14storeContainerEv _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values- -1
String found in graph 1309: Called from- _ZN2ft26TxtHighBayWarehouseStorage5fetchENS_11TxtWPType_tE _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values- -1
```
251,647,874,1234 will not have states with `isValidPos` as this function is also used in `storeContainer` and `store` function.

------------------

Working files,
- `test-combined.py` file is drawing connecting 2 files. The test dataset are present in `test-files`.
- `hbwall2-test, test,  vgrall2-test` are the test dataset
- `graph` and `stateful-graphs` contains the graphs drawn
- `graphviz-combined.py` and `3test.py` are other python files to generate `gspan` data format file and test program respectively. 
- `isValidPos-graphs` contains the graph with string `isValidPos`
