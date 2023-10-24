import os
import sys
import time
import pandas as pd

#input_dir = "/raid/brutusxu/function_calls/logs/OnlyFunctionNames"
input_dir = "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/OnlyFunctionNames"
fname = "hbwall3"

fin = open(os.path.join(input_dir, fname), "r")
function_calls = []
for line in fin:
    function_calls.append(line.strip())

# print(len(function_calls))
# print(function_calls[0])

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


subsequences = break_into_subsequences_non_overlap(function_calls, 512, 256)
print(len(subsequences))
# print(subsequences[0])

# print(subsequences[0])
from prefixspan import PrefixSpan

ps = PrefixSpan(subsequences)
print(f"finish initializing object")
ps.minlen=5
ps.maxlen=10

print(ps.topk(10))
