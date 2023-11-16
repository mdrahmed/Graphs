#!/bin/bash

fname="variantPatternsRetrieved.txt"
seq_len=1000
if [ ! -e "$fname" ]; then
    echo "$fname not found. Removing the unwanted texts like \"Pattern\", \"pattern_size\"" 
    python retrieveVariantPatterns.py
fi

for min_len in 1 2 3 4 5; do
    for stride in 64 128 256 500 1000; do
        echo "Command: python frequentPattern2.py --fname $fname --min_len $min_len --stride $stride --seq_len $seq_len"
        python frequentPattern2.py --fname $fname --min_len $min_len --stride $stride --seq_len $seq_len
    done
done

echo ""
echo "---------------------------------------------"
echo ""
# removing low-level details
for json_files in meta/*.json; do
    json_file=$(basename $json_files)
    echo "Running command: python findUniqueVariantPatterns.py --json_dir meta --json_file $json_file"
    python findUniqueVariantPatterns.py --json_dir meta --json_file $json_file
done


# print total lines
directory="./uniqueTraces"
find "$directory" -type f -exec sh -c '
    echo -n "{}: "
    wc -l "{}" | cut -d " " -f 1
' \;
