import os
import sys
import time
import argparse
import copy
import json

from prefixspan import PrefixSpan

def read_file(input_dir, fname):
    fin = open(os.path.join(input_dir, fname), "r")
    function_calls = []
    for line in fin:
        function_calls.append(line.strip())
    return function_calls

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

def mine_recurring_pattern(function_calls_dict, key, args):
    if args.split_mode == "nonoverlapping":
        subsequences = break_into_subsequences_non_overlap(function_calls_dict[key][0], args.seq_len, args.stride)
    else:
        subsequences = break_into_subsequences(function_calls_dict[key][0], args.seq_len, args.stride)

    ps = PrefixSpan(subsequences)
    print(f"finish initializing object")
    print(f"total number of functions in fname {key} -> {len(function_calls_dict[key][0])}")
    print(f"total number of subsequences for fname {key} -> {len(subsequences)}")
    ps.minlen = args.min_len
    ps.maxlen = args.max_len
    topk = ps.topk(args.topk)
    pattern_dict = {}
    for i, (support, pattern) in enumerate(topk):
        pattern_dict[tuple(pattern)] = support
    print(f"total number of patterns mined from fname {key} -> {len(pattern_dict)}")
    return subsequences, pattern_dict

def mine_common_pattern_whole_traces(function_calls_dict, args):
    """
    find common patterns from whole traces
    """

    sequences = [v[0] for k, v in function_calls_dict.items()]
    ps = PrefixSpan(sequences)
    print(f"finish initializing object")
    ps.minlen = args.min_len
    ps.maxlen = args.max_len
    topk = ps.topk(args.topk)
    pattern_dict = {}
    for i, (support, pattern) in enumerate(topk):
        pattern_dict[tuple(pattern)] = support
    print(f"total number of patterns -> {len(pattern_dict)}")
    return pattern_dict


def find_shared_pattern_threshold(function_calls_dict, threshold):
    """
    only show the pattern that is at least epsilon in both dictionary
    function_calls_dict := {fname: [functions, subsequences, common_patterns]}
    """
    shared_pattern_dict = {}
    for k, v in function_calls_dict.items():
        single_pattern_dict = {}

        for pattern, support in function_calls_dict[k][2].items():
            single_pattern_dict[tuple(pattern)] = support / len(function_calls_dict[k][1]) 
    
        for pattern, freq in single_pattern_dict.items():
            if freq >= threshold:
                if pattern not in shared_pattern_dict:
                    shared_pattern_dict[pattern] = []
                shared_pattern_dict[pattern].append(freq)

    num_files = len(function_calls_dict)
    filtered_pattern_dict = {}
    for k, v in shared_pattern_dict.items():
        if len(v) == num_files:
            filtered_pattern_dict[k] = v

    return filtered_pattern_dict
    
def remove_pattern_greedy(pattern, function_calls):
    filtered_pattern_list = []
    """
    recursively remove pattern from a single trace
    """
    print(f"length of pattern -> {len(pattern)}")
    
    flag = True
    counter = 0
    while flag:
        indexes = []
        prefix = []
        for idx, func_name in enumerate(function_calls):
            if func_name == pattern[len(prefix)]:
                prefix.append(func_name)
                indexes.append(idx)
            if len(indexes) == len(pattern):
                """
                we find one matching pattern, early stop the for loop and perform one filtering
                """
                break
            if func_name != pattern[len(prefix)] and idx == len(function_calls)-1:
                """
                this indicates we arrive as last index and no pattern match anymore
                we can end the while loop
                """
                flag = False
        if flag:
            function_calls = [function_calls[i] for i in range(len(function_calls)) if i not in indexes]
            counter += 1
    print(f"total number of filtering -> {counter}")

    return function_calls


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, default="/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/OnlyFunctionNames/")
    parser.add_argument("--fnames", type=str, default="hbwall3", help="input arbitrary number of filenames, separate by -")
    parser.add_argument("--fname_to_remove", type=str, required=True)
    parser.add_argument("--split_mode", type=str, choices=["overlapping", "nonoverlapping"], default="nonoverlapping")
    parser.add_argument("--seq_len", type=int, required=True)
    parser.add_argument("--stride", type=int, default=256)
    parser.add_argument("--min_len", type=int, default=5)
    parser.add_argument("--max_len", type=int, default=15)
    parser.add_argument("--topk", type=int, default=100)
    parser.add_argument("--common_threshold", type=float, default=0.5)

    args = parser.parse_args()

    fnames = args.fnames.split("-")
    function_calls_dict = {}
    for i, fname in enumerate(fnames):
        function_calls_dict[fname] = [read_file(args.input_dir, fname)]
    
    pattern_dict = mine_common_pattern_whole_traces(function_calls_dict, args)

    
    for k, v in function_calls_dict.items():
        subsequences, pattern_dict = mine_recurring_pattern(function_calls_dict, k, args)
        function_calls_dict[k].extend([subsequences, pattern_dict])
    
    shared_pattern_dict = find_shared_pattern_threshold(function_calls_dict, args.common_threshold)
    print(f"total number of target patterns -> {len(shared_pattern_dict)}")
    for k, v in shared_pattern_dict.items():
        print(f"{k} -> {v}")

    function_calls = function_calls_dict[args.fname_to_remove][0]
    print(f"length before filtering -> {len(function_calls)}")

    for k, v in shared_pattern_dict.items():
        print(f"current target pattern -> {k}")
        function_calls = remove_pattern_greedy(k, function_calls)

    print(f"length after filtering -> {len(function_calls)}")


    """
    write your save function here
    """

    # Open a file for writing
    with open('output.txt', 'w') as file:
        # Redirect the standard output to the file
        original_stdout = sys.stdout
        sys.stdout = file
    
        # Perform your print statements
        print(f"length after filtering -> {function_calls}")
    
        # Restore the original standard output
        sys.stdout = original_stdout

