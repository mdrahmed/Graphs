#!/bin/bash

input_file="./onlyRetrievals/commonPatternInMultipleVariants"
output_file="output"

start_pattern="Similarity"
end_pattern="Similarity"

# Find line numbers of the start and end patterns
start_line=$(grep -n "$start_pattern" "$input_file" | head -n 1 | cut -d ":" -f 1)
end_line=$(grep -n "$end_pattern" "$input_file" | head -n 2 | tail -n 1 | cut -d ":" -f 1)

# Extract the text between the patterns
if [ -n "$start_line" ] && [ -n "$end_line" ]; then
    sed -n "$((start_line + 1)),$((end_line - 1))p" "$input_file" > "$output_file"
    echo "Extracted text saved to $output_file"
else
    echo "Could not find the required pattern in the file."
fi

