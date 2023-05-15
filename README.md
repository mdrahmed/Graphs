Working files,

1. graph-hbw.py is not working as it is crossing the edge limit.
Error:
```
Error: Edge length 75278.000000 larger than maximum 65535 allowed.
Check for overwide node(s).
Error: Edge length 74540.000000 larger than maximum 65535 allowed.
Check for overwide node(s).
Error: Edge length 103250.000000 larger than maximum 65535 allowed.
Check for overwide node(s).
Error: Edge length 103349.000000 larger than maximum 65535 allowed.
Check for overwide node(s).
Error: Edge length 74522.000000 larger than maximum 65535 allowed.
Check for overwide node(s).
Error: Edge length 74522.000000 larger than maximum 65535 allowed.
Check for overwide node(s).
Error: Edge length 414043.319493 larger than maximum 65535 allowed.
Check for overwide node(s).
Error: Edge length 103340.000000 larger than maximum 65535 allowed.
Check for overwide node(s).
Error: Edge length 103991.983276 larger than maximum 65535 allowed.
Check for overwide node(s).
Error: Edge length 103479.178778 larger than maximum 65535 allowed.
Check for overwide node(s).
Error: Edge length 103970.535179 larger than maximum 65535 allowed.
Check for overwide node(s).
```

2. graph-hbw2.py is created to generate graph with the 1st 1000 edges from the tracking event. It's working fine. The graph is present inside graphs-drawn folder with the same name as the file - graph-hbw2.py

The test folder will contain programs with all the test cases just to check if my code is working for all case senarios.

gSpan: Using gSpan to find subgraphs from a set of graphs

3. `hbw-graph2.txt` is created from `hbw-graph.txt` because `hbw-graph.txt` contains `Calling:` and `Function:` both in one line but `hbw-graph2.txt` has those in 2 separate lines, check following code,
```
sed -i '/Calling:/s/Function:/\n&/' ../hbw-graph2.txt
```

 
