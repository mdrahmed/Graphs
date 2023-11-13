import os
import sys
import time
import argparse
import copy
import json

from prefixspan import PrefixSpan


def break_into_subsequences(input_sequence, seq_len, stride):
    assert seq_len%2==0, "seq_len must be even"
    output_sequences = []
    for i, func_call in enumerate(input_sequence):
        if (i+1)%stride == 0:
            pre_context = i + 1 - seq_len // 2
            pro_context = i + 1 + seq_len // 2
            output_sequences.append(input_sequence[pre_context:pro_context])
    return output_sequences

def break_into_subsequences_non_overlap(input_sequence, seq_len, stride):
    return [input_sequence[i: i+seq_len] for i in range(len(input_sequence)//seq_len+1)]



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_dir", type=str, default="/home/raihan/Graphs-all/Graphs/backwardTracking/combinedGraph/plagarismFinder/myPlagiarismChecker")
    parser.add_argument("--fname", type=str, required=True)
    parser.add_argument("--seq_len", type=int, required=True)
    parser.add_argument("--stride", type=int, default=256)
    parser.add_argument("--min_len", type=int, default=5)
    parser.add_argument("--max_len", type=int, default=10)
    parser.add_argument("--topk", type=int, default=100)

    args = parser.parse_args()

    fin = open(os.path.join(args.input_dir, args.fname), "r")
    function_calls = []
    for line in fin:
        function_calls.append(line.strip())

    subsequences = break_into_subsequences(function_calls, args.seq_len, args.stride)
    ps = PrefixSpan(subsequences)
    print(f"finish initializing object")
    ps.minlen = args.min_len
    ps.maxlen = args.max_len

    topk = ps.topk(args.topk)
    config = vars(args)
    meta = copy.deepcopy(config)
    meta["topk"] = topk

    print(topk)

    if not os.path.isdir("./meta"):
        os.mkdir("./meta")
    fout_path = "./meta"
    fout_name = f"{args.fname}_{args.seq_len}_{args.stride}_{args.min_len}_{args.max_len}_{args.topk}.json"
    with open(os.path.join(fout_path, fout_name), "w") as fout:
        json.dump(meta, fout)
