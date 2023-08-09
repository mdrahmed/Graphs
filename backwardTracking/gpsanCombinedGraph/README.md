Worked files till now for `gspan`, 
------------------
```
graphviz-combined.py
```
------------------

Working files,

1. **This file is generating `.data` file for the gspan.** This `graphviz-combined.py` file is a copy of `graphViz-bt-hbw5.py` file. But this will find topic and when it sees one, it will start looking into another file and then create graph with that with a recursive call. After that it will come back and then use the previous file to draw the graph in the general way. But there will be an edge between the 2 files with the `topic`.
