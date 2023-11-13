# Find most-important functions
Steps are following,
1. Find sub-patterns within two/multiple files - `pairwise_frequent_pattern.py
    ```
    python pairwise_frequent_pattern.py --fname1 hbwall3 --fname2 vgrall3 --seq_len 1024 --topk 1000 --common_threshold 0.2 --split_mode overlapping > ./pairwise_frequent_pattern/hbw-vgr
    ```
2. Remove those patterns from files - `find_and_remove.py`
    ```
    python find_and_remove.py --fnames hbwall3-vgrall3 --split_mode overlapping --seq_len 512 --topk 2000 --fname_to_remove hbwall3 --common_threshold 0.1
    ```
3. Remove patterns from the same files - `findPattern.py` or, `frequentPattern2.py` or, `frequentPattern.py` --- **Only use this for same file**
    ```
    python frequentPattern2.py --fname f1.txt --seq_len 2000
    ```
   

## Finding sub-patterns
To find the sub patterns, we used the `prefixspan`. 
The documentation is [here](https://github.com/chuanconggao/PrefixSpan-py/tree/master#closed-patterns-and-generator-patterns)

Steps:
- Breaking the whole sequence into subsequences with the param `seq_len`
- Then using it to find the common subsequence.


### Sub-patterns between different files

`pairwise_frequent_pattern.py` file is used to find sub-patterns. Run following,
```
python pairwise_frequent_pattern.py --fname1 hbwall3 --fname2 vgrall3 --seq_len 1024 --topk 1000 --common_threshold 0.2 --split_mode overlapping > ./pairwise_frequent_pattern/hbw-vgr
```
