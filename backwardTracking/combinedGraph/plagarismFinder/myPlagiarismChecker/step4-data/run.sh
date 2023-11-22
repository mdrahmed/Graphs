#!/bin/bash

# according to the README.md of ../step3-data the following files has minimum traces will most important functions
files=("uniqueVariantTraces_1000_256_1_10_100" "uniqueVariantTraces_1000_256_2_10_100")
freq_to_remove=("0.05" "0.03" "0.02" "0.015" "0.01")

for file in "${files[@]}"; do
    for freq in "${freq_to_remove[@]}"; do
        python idf.py --fname "$file" --freq_to_remove "$freq"
    done
done


# print total lines
directory="./idf_traces"
find "$directory" -type f -exec sh -c '
    echo -n "{}: "
    wc -l "{}" | cut -d " " -f 1
' \;
