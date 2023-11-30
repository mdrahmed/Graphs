## For data mining task, we used 3 steps
1. Step 1 - LCS: Remove common patterns from 2/more files `vgr` and `hbw`. But the `similarity_2_File.py` file will find same patterns from the 2 files only.
    Dir: `step1`
    File: `similarity_2_File.py` - specify the file path first.
        Run: `python3 similarity_2_File.py > patterns`
2. Step 2 - LCS: Extract common patterns from multiple(>2) files. 
    Dir: `step2`
    File: `similarity_multiple.py`
        Run: `python3 <this_file>.py <your_directory_to_txt_files> > patterns`
        E.g., `python3 similarity_multiple.py.py  /home/raihan/Graphs-all/Graphs/backwardTracking/combinedGraph/plagarismFinder/myPlagiarismChecker/step2-data/onlyRetrievals > patterns`
3. Step 3 - IDF: Remove functions based on frequency
    Dir: `step3`
    File: `idf.py`
        Run: `./run.sh` - It will use the `../step2/patterns` file and remove based on the frequency defined in `run.sh`. It will store the function frequency in `frequent_traces_removed` and the updated traces will be written inside `idf_traces`. The unwanted text `patterns, Pattern` will be removed from the file by `removeUnwantedText` and it will save files inside `updated_idf_traces`

**The `find_patterns.py` is the updated version of the `similarity_multiple.py` file**

## Old
`lcs.py` will find all common subsequence has length greater than 1.
