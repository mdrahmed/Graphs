#### Attack 2. Store-overflow/Store-collision
```
motivation-store-overflow/motivation-part-graphs-with-complete-edges/1-position-changed
# This folder contains a complete graph with complete `hbw` and `vgr` edges.
```
In here, the 7 workpieces are stored in the `hbw` first. Then an adversary changed the value of 6th position (1,2) from 1 to 0. In this case, we can detect the change if we keep count of the workpieces. The graph is in following folder,
```
1-position-changed/combined-graph-0.dot
```

**But, if the attacker changed the value of 6th position (1,2) from 1 to 0 and then again change an empty position e.g., 9th position (2,2) from 0 to 1. Then we can't detect the change with the count of the workpieces.** The graph is in following folder,
```
2-position-changed/combined-graph-0.dot
```
Dataset: `~/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/store-overflow/motivation-log-v2-store`
