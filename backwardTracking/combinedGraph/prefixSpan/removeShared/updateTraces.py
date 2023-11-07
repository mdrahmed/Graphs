import sys
import os

if not os.path.isdir("./originalFormat"):
    os.mkdir("./originalFormat")
fout_path = "./originalFormat"

parser = argparse.ArgumentParser();
parser.add_argument("--input_dir", type=str, default="sharedPatternRemoved")
fin=args[1] 
fout=args[1]
# Read the list from the input file
with open(os.path.join("originalFormat/",fin), 'r') as input_file:
    data = input_file.read()

# Extract the function names (assuming the list is in the format "length -> [f1, f2, f3]")
start_index = data.find('[')
end_index = data.find(']')
if start_index != -1 and end_index != -1:
    function_list = data[start_index + 1:end_index].split(', ')

# Write the function names to the output file
with open(os.path.join("originalFormat/", fout), 'w') as output_file:
    for function_name in function_list:
        cleaned_function_name = function_name.replace('\'', '').replace('FFF ', '')
        output_file.write(cleaned_function_name + '\n')

print("Function names extracted and written to 'new_output.txt'.")

