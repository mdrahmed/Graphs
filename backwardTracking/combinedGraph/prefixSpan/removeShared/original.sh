input_dir="sharedPatternRemoved"

# List all files in the input directory and process each one
for input_file in "$input_dir"/*; do
    # Check if it's a file (not a directory)
    if [ -f "$input_file" ]; then
        # Run the Python script with the input directory and input file as arguments
		file_name=$(basename "$input_file")
		echo $file_name
        python3 updateTraces.py "$file_name"
    fi
done

