import json
import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--json_dir", type=str)
parser.add_argument("--json_file", type=str)
args = parser.parse_args()

json_file = os.path.join(args.json_dir, args.json_file)
#with open("./meta/variantPatternsRetrieved.txt_1000_256_5_10_100.json", "r") as fin:
with open(json_file, "r") as fin:
    data = json.load(fin)

# Extract the list from the dictionary
pattern_list = data.get("topk", [])

# Flatten the list of lists and convert it to a set
low_level_set = set(item for sublist in pattern_list for item in sublist[1])


input_file = "./variantPatternsRetrieved.txt"
if not os.path.isdir("./uniqueTraces"):
    os.mkdir("./uniqueTraces")
fout_path = "./uniqueTraces"
arguments = r'_(\d+_\d+_\d+_\d+_\d+)\.json'
match = re.search(arguments, args.json_file)
if match:
    fout_name = f"uniqueVariantTraces_{match.group(1)}"
else:
    fout_name = f"uniqueVariantTraces_"
# Process the input file and write to the output file
with open(input_file, "r") as fin, open(os.path.join(fout_path, fout_name), "w") as fout:
    for line in fin:
        if line.strip() not in low_level_set:
            fout.write(line)
    print("Unique variant traces are written to " + fout_path + '/' + fout_name)
