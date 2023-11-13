import argparse

def remove_prefix(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            cleaned_line = line.replace('FFF Function:', '')
            outfile.write(cleaned_line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Input file name")
    parser.add_argument("output_file", type=str, help="Output file name")
    args = parser.parse_args()

    remove_prefix(args.input_file, args.output_file)
    print("FFF Function: removed")
