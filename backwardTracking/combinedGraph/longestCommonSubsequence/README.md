## For data mining task, we used 3 steps
1. Step 1 & step 2:</br>
	Folder: `./file-common-patterns/`</br>
	Program: `find_remove_patterns.py`</br>
	Run: `python3 find_remove_patterns.py ../Data/hbw-Retrievals/ -f ../Data/vgr-traces/vgrall3.txt -o`</br>

   Step1: The updated retrieval/store traces will be written to this folder `./file-common-patterns/step1.2-noises_removed`
   Step2: The common patterns will be extracted and it will be present here `step2-extracted_common_part_retrieval`

3. Step 3 - IDF: Remove functions based on frequency
	Dir: `step3`
	File: `idf.py`
        Run: `./run.sh` - It will use the `../step2/patterns` file and remove based on the frequency defined in `run.sh`. It will store the function frequency in `frequent_traces_removed` and the updated traces will be written inside `idf_traces`. The unwanted text `patterns, Pattern` will be removed from the file by `removeUnwantedText` and it will save files inside `updated_idf_traces`

## Get reduction numbers
Execute `shell.sh` to get the reduced numbers. After executing this, manually check which file has all the important functions. 
