#! /bin/bash

# This find_remove_patterns.py will create following 3 folders,
# step1.1-hbw_vgr_common - this folder will contain common patterns between hbw all retrievals and 1 vgr file
# step1.2-noises_removed - this folder will contain updated hbw retrievals which is obtained after removing the noises
# step2-extracted_common_part_retrieval - this folder will contain the extracted common pattern between multiple retrievals
## python3 find_remove_patterns.py ../Data/hbw-Retrievals/ -f ../Data/vgr-traces/vgrall3.txt -o


echo "The data reduced to following sizes:"

# The original size of ALL retrieval process-S1: print total lines in all the retrievals present inside the "/home/raihan/Graphs-all/Graphs/backwardTracking/combinedGraph/longestCommonSubsequence/Data/hbw-Retrievals"
echo "The original size of ALL retrieval process-S1:"
directory="./Data/hbw-Retrievals"
find "$directory" -type f -exec sh -c '
    echo -n "{}: "
    wc -l "{}" | cut -d " " -f 1
' \; | sort -n
echo ""

# S1 minus common pattern size between VGR and HBW = S2: This is present inside this folder - ./file-common-patterns/step1.2-noises_removed
echo "S1 minus common pattern size between VGR and HBW = S2:"
directory="./file-common-patterns/step1.2-noises_removed/"
find "$directory" -type f -exec sh -c '
    echo -n "{}: "
    wc -l "{}" | cut -d " " -f 1
' \; | sort -n
echo ""

# The size of common part among multiple retrieval processes (S2', S2'', S2''', ...) = S3: This is present in ./file-common-patterns/step2-extracted_common_part_retrieval
echo "The size of common part among multiple retrieval processes (S2', S2'', S2''', ...) = S3:"
directory="./file-common-patterns/step2-extracted_common_part_retrieval"
find "$directory" -type f -exec sh -c '
    echo -n "{}: "
    wc -l "{}" | cut -d " " -f 1
' \; | sort -b
echo ""


# S3 minus high-frequent patterns = S4: This is present inside /home/raihan/Graphs-all/Graphs/backwardTracking/combinedGraph/longestCommonSubsequence/step3/updated_idf_traces
echo "S3 minus high-frequent patterns = S4:"
directory="./step3/updated_idf_traces"
find "$directory" -type f -exec sh -c '
    echo -n "{}: "
    wc -l "{}" | cut -d " " -f 1
' \; | sort -n
