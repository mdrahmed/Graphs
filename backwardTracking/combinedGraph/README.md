Worked files till now,
------------------
1. All logs are combined to create a simple file
```
./combined-graph.py ##This file will draw graph with 500 edges and nodes using states, but graphs from seperate files e.g., vgr and hbw are not drawn.
```
2. To generate graph of one-log e.g., `hbw`/`vgr`/`mpo`/`sld`
```
./one-file-graph.py ##This file will draw graph with 500 edges and nodes using states. It is using this to draw graphs for `hbw` - `~/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/hbwall3`
```

------------------

Working files,
- `hbwall2-test, test,  vgrall2-test` are the test dataset
- `graph` and `stateful-graphs` contains the graphs drawn
- `graphviz-combined.py` and `3test.py` are other python files to generate `gspan` data format file and test program respectively. 
