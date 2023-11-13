#!/bin/bash

# Set the absolute directory path
directory="/home/raihan/Graphs-all/Graphs/backwardTracking/combinedGraph/hbw-graph"

# Check if the directory exists
if [ -d "$directory" ]; then
    # Run the command in the specified directory and save the output to a text file in the current directory
    (cd "$directory" && \
     rg -l "buffer_ref" | xargs rg -l "make_message" | xargs rg -l "message6create" | \
     xargs rg -l "message12validate" | xargs rg -l "message12set_retained" | \
     xargs rg -l "to_int" | xargs rg -l "message7set_qos" | xargs rg -l "message9get_topic" *.dot) > longestPatternRemoved.txt

    echo "Command executed.\nOutput saved to longestPatternRemoved.txt"
else
    echo "Error: Directory not found."
fi

