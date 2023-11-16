import json
import os

# Load the JSON file
with open("./meta/variantPatternsRetrieved.txt_1000_256_5_10_100.json", "r") as json_file:
    config = json.load(json_file)

# Extract the desired values (assuming "topk" contains the list of strings)
strings_to_write = []
for topk_entry in config.get("topk", []):
    strings_to_write.extend(topk_entry[1])


if not os.path.isdir("./format_variant_pattern"):
    os.mkdir("./format_variant_pattern")
fout_path = "./format_variant_pattern"
fout_name = f"remove_common_pattern_variant.txt"
# Write the strings to a text file
with open(os.path.join(fout_path, fout_name), "w") as text_file:
    for string_value in strings_to_write:
        text_file.write(f"{string_value}\n")

