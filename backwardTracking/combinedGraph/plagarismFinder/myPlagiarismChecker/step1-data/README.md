
## Step 1 is to remove common patterns between shared text
The common patterns were found in the `../patterns/patterns.txt` file. It is copied here. 

Working files,
```
# remove unwanted text like length, pattern etc from patterns.txt and write to sharedPatternsFormatted.txt
python removeUnwantedText.py

# The main purpose is to remove the shared common patterns. I am removing it using sliding window
# Following file will get the lengths of the patterns/windows from patterns/sharedPatternsFormatted.txt
python getLengths.py


# sequence.py will format hbwall3 to hbwFormatted.txt 
# it will also check if the exact pattern is found in the hbw
# implementation is not done yet, remove all other patterns except the 1st one, it will print that "Sequence found in the exact order."
python sequence.py

# Now, update the sequence.py file to remove the shared patterns
```
