import sys
import os
import argparse


# Parse command-line arguments
parser = argparse.ArgumentParser()
#parser.add_argument("input_dir", type=str, default="sharedPatternRemoved")
parser.add_argument("input_file", type=str, help="Input file name")
args = parser.parse_args()


input_dir = "./"
input_file = os.path.join(args.input_file)

output_dir = "./"
# Write the function names to the output file
output_file_path = os.path.join(f"{args.input_file}_.txt")
with open(os.path.join(output_file_path), 'w') as output_file:
    with open(input_file, 'r')as file_: 
        for line in file_:
            cleaned_function_name = line.replace('\'', '').replace('FFF ', '')
            output_file.write(cleaned_function_name + '\n')

