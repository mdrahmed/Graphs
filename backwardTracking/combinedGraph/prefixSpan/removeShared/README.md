## Remove shared pattern
`find_and_remove.py` will remove shared data. 
```
python3 find_and_remove.py --fnames hbwall3-vgrall3 --split_mode overlapping --seq_len 512 --topk 2000 --fname_to_remove hbwall3 --common_threshold 0.1
```

After this it will create the `output.txt` and thats a list, so, run `updateTraces.py` to update this file into the original traces format.
```
python3 updateTraces.py
```

## shell.sh
The `shell.sh` file is running the `find_and_remove.py` file with different `seq_len` and `topk`. So, getting this data inside the `meta` directory.
