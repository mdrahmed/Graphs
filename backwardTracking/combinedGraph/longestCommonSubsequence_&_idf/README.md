## For data mining task, we used 3 steps
**Specify the dataset at first in the Data Folder.**
1. Step 1 & step 2:	</br>
	Folder: `./file-common-patterns/`	</br>
	Program: `find_remove_patterns.py`	</br>
	Run: `python3 find_remove_patterns.py ../Data/hbw-Retrievals/ -f ../Data/vgr-traces/vgrall3.txt -o`	</br>
	Note: 3 hbw retrievals are present inside the `../Data/hbw-Retrievals/`, which is compared with `../Data/vgr-traces`

   Step1: The updated retrieval/store traces will be written to this folder `./file-common-patterns/step1.2-noises_removed`
   Step2: The common patterns will be extracted and it will be present here `step2-extracted_common_part_retrieval`

3. Step 3 - IDF: Remove functions based on frequency
	Dir: `step3`	  </br>
	File: `idf.py` 	  </br>
        Run: `./run.sh` - It will use the `../step2/patterns` file and remove based on the frequency defined in `run.sh`. The updated traces will be written inside `updated_idf_traces`. It will also store the function frequency in `frequent_traces_removed` and the traces will present inside `idf_traces` with unwanted texts like `patterns, Pattern`. `run.sh` will use `removeUnwantedText` to remove unwanted text like `patterns, Pattern` and it will save files inside `updated_idf_traces`. 

## Get reduction numbers
Execute `shell.sh` to get the reduced numbers. After executing this, manually check which file has all the important functions. 