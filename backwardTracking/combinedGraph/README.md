Worked files till now,
------------------
1. All logs are combined to create a simple file, while executing give the input properly - see below for inputs.
```
./combined-graph-v3.py ##This file is a copy of ./combined-graph-v2.py, I used this to draw the motivation part of the paper. 
```
Sometimes, I will need to work with only functions, so, created a separate file for that,
```
./combinedOnlyFunc.py ## This file is a copy of ./combined-graph-v3.py but commented out everything excepts functions.
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
i\j 2 1 0<br/>
0 &nbsp; - - -<br/>
1 &nbsp; - - -<br/>
2 &nbsp; - - -<br/>

The graph should show function calls with table and wp position, call instructions but not global variables. This file `./combined-graph-v3.py` is working fine with all the corner cases. If it finds a `message_arrived get_topic` and finds similar `publish get_topic` then it will **link these two nodes with same states.** This is shown in `motivation-part-graphs-test`. All the original graphs are present in `motivation-delivery-underflow/motivation-part-graphs` folder.

**While drawing the graphs, it depends on from where I am starting.**
#### Attack 1. Delivery-underflow
##### With complete hbw & vgr edges
```
motivation-delivery-underflow/motivation-part-graphs-with-complete-edges/motivation-part-graphs-v2-1wp 
# input: hbw/ack, dataset: motivation-log-v2-delivery
# This folder contains a complete stateful graph after storing 1 workpiece at 0,0 and then ordering 1 workpiece from 0,1 to show the attack 
motivation-delivery-underflow/motivation-part-graphs-with-complete-edges/motivation-part-graphs-v3-9wp 
# this folder contains a complete stateful graph after storing 9 workpieces in the HBW and then ordering 1 wp from 0,1 and again ordering from 0,1 to show the attack
#input: topic, dataset: motivation-log-v3
motivation-delivery-underflow/motivation-part-graphs-with-complete-edges/motivation-part-graphs 
# This folder has graph same as motivation-part-graphs-v2-1wp but it is starting from the storeContainer, which is storing the empty container back to the storage.
# input: storeContainer, dataset: motivation-log-v2-delivery
```
##### Without complete vgr edges
```
motivation-part-graphs-without-complete-edges/motivation-delivery-underflow/motivation-part-graphs-v2-1wp 
# This folder contains a complete stateful graph after storing 1 workpiece a 0,0 and then ordering 1 workpiece from 0,1 to show the attack
# input: hbw/ack
motivation-part-graphs-without-complete-edges/motivation-delivery-underflow/motivation-part-graphs-v3-9wp 
# this folder contains a complete stateful graph after storing 9 workpieces in the HBW and then ordering 1 wp from 0,1 and again ordering from 0,1 to show the attack
#input: topic
motivation-part-graphs-without-complete-edges/motivation-delivery-underflow/motivation-part-graphs 
# This folder has graph same as motivation-part-graphs-v2-1wp but it is starting from the storeContainer, which is storing the empty container back to the storage.
# input: storeContainer
```

#### Attack 2. Store-overflow/Store-collision
```
motivation-store-overflow/motivation-part-graphs-with-complete-edges/ 
# This folder contains a complete graph with complete `hbw` and `vgr` edges.
motivation-store-overflow/motivation-part-graphs-without-complete-edges/ 
# This folder contains graph without complete `vgr` edges.
```

Dataset: The combined dataset used here is following,
The dataset `motivation-log-v2` is updated as following,
- Added delivery and store node: Each and every communication is done with mqtt. During the delivery after the hbw grabs the workpiece, it will send a mqtt message to vgr with topic fl/hbw/ack. So, for the delivery node I added that publish function. Similarly, after the hbw stores a workpiece it will send the same mqtt message to vgr. So, for store node I added that same publish function. [Things to consider: This msg will not trigger vgr to move. Also, this msg is not sent to the server/dashboard. This is like a two-way handshake to establish the communication. The vgr will not send any request in the middle, it will send message after it receives that topic fl/hbw/ack, which is acknowledging the task is done.]
- Initial storage: Table in the initial form is removed from the graph. The table or storage contains no workpieces at the beginning - Table - 0 0 0 0 0 0 0 0 0
- Extended the vgr: At the beginning the vgr is receiving mqtt message with topic f/o/order from server/dashboard. I added this part. Also, after it receives the message, it sends another mqtt message with topic f/i/order, I have shown this part in the graph too.
- Added message-arrived, publish and the functions changing the value of global variables: I added the most important functions which will show the exact work. Like after vgr sends mqtt message f/i/order to server. Then it sends mqtt message to hbw with topic fl/vgr/do, now that is received by the hbw and it calls the function requestVGRfetchContainer which will change the global variable reqVGRfetchContainer, which will trigger the hbw fetchContainer and this will call hbw storage fetchContainer, then it will check the isValidPos. [NOT SHOWN IN GRAPH: After all this, it will send the message with topic /fl/hbw/ack. After this is received by the vgr, the vgr will send same topic fl/vgr/do to hbw and hbw will do store workpiece in hbw storage and then send the msg fl/hbw/ack again. I didn't show this part in graph because the graph was already too complex and as we have the table showing the updated storage.] Similarly while delivering the workpiece, the hbw is calling requestVGRfetch and it is changing the variable reqVGRfetch, which is calling hbw fetch, hbw storage fetch and, isValidPos simultaneously. [NOT SHOWN IN GRAPH: After this it is storing the empty container with storeContainer function call.]
```
~/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/motivation-log-v2 # This is both delivery and store => updated with the guidelines
~/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/motivation-log-v2-delivery # This is the delivery part of hbw and vgr
```


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


## Generate gspan subgraphs
The gspan data format has been created with this following python file,
```
gspanDataFormat.py # copy of ./combinedOnlyFunc.py
```
This `combinedOnlyFunc.py` file is different from the `gpsanDataFormat.py`. Because I was getting following keyErrors and that's why I needed to change the file.
```
Index was out of range because the data file was created with function names, arguments and it's values putting all in a new line.
...
KeyError: '"message_arrivedget_topicvalue-f/o/order-state4"'
...
KeyError: '"u16LastStateDIN,reqUpdateDIN=>sensor"'
..
KeyError: '"publishget_topicvalue-f/i/order-state4"'
```
![gpsan-error](pics/gspan-error.png)

**After changing the file. I am getting subgraphs present in the `Graphs/pics` dir.** Now, the `gpsanDataFormat.py` is updated with only functions. And the gspan-subgraphs will be found in the `gspan-subgraphs` folder.
![gspan-graphs](pics/gpsan-subg-vgr.png)
