#! /usr/bin

# extract the commonPatternInMultipleVariants to the output file - EXTRACTING ONLY THE 1ST COMMON TEXT BCZ THERE WILL BE ONLY SIMILAR PATTERNS
sh extractCommons.sh

# Format the files
python3 ../updateFormat.py ./onlyRetrievals/1retrieval.txt ./f1.txt
python3 ../updateFormat.py ./onlyRetrievals/2retrieval.txt ./f2.txt

# Removing common patterns from the 1 & 2 retrievals
python3 ../removeCommons.py
echo "Removed common patterns between 1-retrieval.txt and 2retrieval.txt"

cp f1.txt updatedHBW-variant.txt

## Now, checking if the pattern is present on f1.txt file
## Format the files
#python3 ../updateFormat.py ./f1.txt ./f1.txt
#python3 ../updateFormat.py ./onlyRetrievals/2retrieval.txt ./f2.txt
#
## Removing common patterns from the 1 & 2 retrievals
#python3 ../removeCommons.py
#echo "Removed common patterns between 1-retrieval.txt and 3retrieval.txt"
#
#
## Format the files
#python3 ../updateFormat.py ./f1.txt ./f1.txt
#python3 ../updateFormat.py ./onlyRetrievals/3retrieval.txt ../f2.txt
#
## Removing common patterns from the 1 & 2 retrievals
#python3 ../removeCommons.py
#echo "Removed common patterns between 2retrieval.txt and 3retrieval.txt"


# Check the size of the files
text_files=$(find ./onlyRetrievals -type f -name "*.txt")

# Initialize a variable to store the total line count
total_lines=0

# Loop through each text file and count lines
for file in $text_files; do
    lines=$(wc -l < "$file")
    echo "Initial size of file - $file: $lines"
done

echo "updatedHBW-variant.txt File size after removing the patterns: $(wc -l < updatedHBW-variant.txt)"
