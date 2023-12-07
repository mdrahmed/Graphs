#!/bin/bash

# Input folder: ../step2/
# Input file: patterns
files=("patterns")
freq_to_remove=("0.05" "0.03" "0.02" "0.015" "0.01" "0.005" "0.001" "0.0005" "0.0004")

# Remove functions based on frequency
for file in "${files[@]}"; do
    for freq in "${freq_to_remove[@]}"; do
        # idf.py file will get frequency of each function and store it in frequent_traces_removed and then remove functions based on frequency and store it in idf_traces
        python idf.py --fname "$file" --freq_to_remove "$freq"
    done
done

# Remove unwanted text e.g., Pattern/Patterns. The file will take input from idf_traces directory and remove the unwanted text and save the output inside updated_idf_traces
python3 removeUnwantedText.py

# print total lines
directory="./updated_idf_traces"
find "$directory" -type f -exec sh -c '
    echo -n "{}: "
    wc -l "{}" | cut -d " " -f 1
' \;
