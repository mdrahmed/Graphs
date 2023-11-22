# Variant common pattern

After removing the common patterns from the shared files `hbw, vgr`. Now, extracting the common patterns between multiple variants - from 3 `hbw` retrievals. All the retrievals are present inside the `onlyRetrievals` folder.
Do following to extract the common patterns.
```
# it will get the common patterns by checking with plagiarism checker and save the 1st line of commons inside 'commonPatternInMultipleVariants' - all the patterns found will have same text - check after "Similarity"
sh step2.sh 

# Now, this script will extract the common patterns and save the output in patterns/patterns.txt file
removeCommonsS2.sh
```
Now, use the `patterns/patterns.txt` for step 3

### others - not related to step2
The `extractCommons.sh` will extract only the 1st similar common patterns. Because all the patterns listed are same.

![variantCommonPatterns](pics/variantCommonPatterns.png)


## Total noises removed
`updatedHBW-shared.txt` initilly has 73514 total functions.
Extracted the stores and retrieves. Then after removing the noises, we have `updatedHBW-variant.txt` file,
```
Initial total function of file - ./onlyRetrievals/2retrieval.txt: 12452
Initial total function of file - ./onlyRetrievals/3retrieval.txt: 20260
Initial total function of file - ./onlyRetrievals/1retrieval.txt: 8301
updatedHBW-variant.txt File size after removing the patterns: 5417
```
