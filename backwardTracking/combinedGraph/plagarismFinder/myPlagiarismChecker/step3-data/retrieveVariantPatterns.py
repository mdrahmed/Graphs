def remove_lines_with_patterns(input_file, output_file, patterns):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not any(pattern in line for pattern in patterns) and line.strip():
                outfile.write(line)

# Example usage
input_file = '../step2-data/patterns/patterns.txt'
output_file = 'variantPatternsRetrieved.txt'
patterns_to_remove = ['Pattern', 'Patterns:', 'Longest_pattern_size']

remove_lines_with_patterns(input_file, output_file, patterns_to_remove)
print("Unwanted text removed\n")

