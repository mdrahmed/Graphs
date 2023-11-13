#import graphviz
#import pygraphviz as pgv
from collections import defaultdict

def find_and_store_functions(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f:
        input_str = f.read()

    # Split the input_str into lines
    lines = input_str.split('\n')

    # Initialize a list to store lines with "Function"
    function_lines = []

    for line in lines:
        if "Function" in line:
            function_lines.append(line)

    # Write the found lines to the output file
    with open(output_file_path, 'w') as out_file:
        out_file.write('\n'.join(function_lines))

# Define the paths for input and output files
input_file_path = '/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/vgrall3.2'
output_file_path = '/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/OnlyFunctionNames/vgrall3.2'  # Replace with your desired output file path

# Call the function to find and store "Function" lines
find_and_store_functions(input_file_path, output_file_path)

