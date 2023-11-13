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


def common_pattern(pattern_dict_1, pattern_dict_2, subsequences_1, subsequences_2):
    """
    the statistics is computed by support_1/len(subsequences_1) * support_2/len(subsequences_2)
    it is bounded to [0, 1]
    """

    pattern_dict = {}
    for k, v in pattern_dict_1.items():
        if k in pattern_dict_2:
            pattern_dict[k] = pattern_dict_1[k]*pattern_dict_2[k] / (len(subsequences_1) * len(subsequences_2))
        else:
            pattern_dict[k] = 0
    for k, v in pattern_dict_2.items():
        if k not in pattern_dict:
            pattern_dict[k] = 0
    return pattern_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_dir", type=str, default="/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/OnlyFunctionNames")
    parser.add_argument("--fname1", type=str, required=True)
    parser.add_argument("--fname2", type=str, required=True)
    parser.add_argument("--fname3", type=str, required=True)
    parser.add_argument("--fname4", type=str, required=True)
    parser.add_argument("--split_mode", type=str, choices=["overlapping", "nonoverlapping"], default="nonoverlapping")
    parser.add_argument("--seq_len", type=int, required=True)
    parser.add_argument("--stride", type=int, default=256)
    parser.add_argument("--min_len", type=int, default=5)
    parser.add_argument("--max_len", type=int, default=15)
    parser.add_argument("--topk", type=int, default=100)
    parser.add_argument("--common_threshold", type=float, default=0.5)

    args = parser.parse_args()
    
    # hbwall3
    fin = open(os.path.join(args.input_dir, args.fname1), "r")
    function_calls_1 = []
    for line in fin:
        function_calls_1.append(line.strip())
    if args.split_mode == "nonoverlapping":
        subsequences_1 = break_into_subsequences_non_overlap(function_calls_1, args.seq_len, args.stride)
    else:
        subsequences_1 = break_into_subsequences(function_calls_1, args.seq_len, args.stride)
    
    ps = PrefixSpan(subsequences_1)
    print(f"finish initializing object")
    print(f"total number of subsequences for fname {args.fname1} -> {len(subsequences_1)}")

    ps.minlen = args.min_len
    ps.maxlen = args.max_len

    topk = ps.topk(args.topk)
    pattern_dict_1 = {}
    for i, (support, pattern) in enumerate(topk):
        pattern_dict_1[tuple(pattern)] = support

    # vgrall3
    fin = open(os.path.join(args.input_dir, args.fname2), "r")
    function_calls_2 = []
    for line in fin:
        function_calls_2.append(line.strip())
    if args.split_mode == "nonoverlapping":
        subsequences_2 = break_into_subsequences_non_overlap(function_calls_2, args.seq_len, args.stride)
    else:
        subsequences_2 = break_into_subsequences(function_calls_2, args.seq_len, args.stride)

    ps = PrefixSpan(subsequences_2)
    print(f"finish initializing object")
    print(f"total number of subsequences for fname {args.fname2} -> {len(subsequences_2)}")

    ps.minlen = args.min_len
    ps.maxlen = args.max_len

    topk = ps.topk(args.topk)
    pattern_dict_2 = {}
    for i, (support, pattern) in enumerate(topk):
        pattern_dict_2[tuple(pattern)] = support

    common_pattern_dict = common_pattern(pattern_dict_1, pattern_dict_2, subsequences_1, subsequences_2)
    sorted_common_pattern_dict = sorted(common_pattern_dict.items(), key=lambda x: x[1])
    for i, (pattern, ratio) in enumerate(sorted_common_pattern_dict):
        if ratio >= args.common_threshold:
            print(f"{pattern} -> {ratio}")
