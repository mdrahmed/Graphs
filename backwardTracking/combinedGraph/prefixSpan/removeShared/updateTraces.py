import sys
import os
import argparse


output_dir = "./originalFormat"

# Parse command-line arguments
parser = argparse.ArgumentParser()
#parser.add_argument("input_dir", type=str, default="sharedPatternRemoved")
parser.add_argument("input_file", type=str, help="Input file name")
args = parser.parse_args()

if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
fout_path = "./originalFormat"

input_dir = "sharedPatternRemoved"
input_file_path = os.path.join(input_dir, args.input_file)
with open(input_file_path, 'r') as input_file:
    data = input_file.read()

# Extract the function names (assuming the list is in the format "length -> [f1, f2, f3]")
start_index = data.find('[')
end_index = data.find(']')
if start_index != -1 and end_index != -1:
    function_list = data[start_index + 1:end_index].split(', ')

# Write the function names to the output file
output_file_path = os.path.join(output_dir, f"{args.input_file}_original.txt")
with open(os.path.join(output_file_path), 'w') as output_file:
    for function_name in function_list:
        cleaned_function_name = function_name.replace('\'', '').replace('FFF ', '')
        output_file.write(cleaned_function_name + '\n')

print("Function names extracted and written to 'new_output.txt'.")

