Data mining results:

1. Step 1: Noisy patterns remove after comparing hbw and vgr
    File: updatedHBW-shared.txt
    File size: 73514 (Not updated completely but we will get data even less than this)
    path:`Graphs/backwardTracking/combinedGraph/plagarismFinder/myPlagiarismChecker`

2. Step 2: From above file found multiple retrievals and plagiarism is kept inside this file: updatedHBW-variannt_pattern_output, the common patterns were extracted
    File: variantPatternsRetrieved.txt
    File size: 2398
    path: `Graphs/backwardTracking/combinedGraph/plagarismFinder/myPlagiarismChecker/step2-data`
    
3. Step 3: Remove common patterns appearing multile times within the same retrievals(Previous file: variantPatternsRetrieved.txt)
    File: uniqueVariantTraces_1000_256_2_10_100
    File size: 848
    path: `Graphs/backwardTracking/combinedGraph/plagarismFinder/myPlagiarismChecker/step3-data/uniqueTraces`

4. Step 4: Removing based on frequency using inverse document frequency algorithm. `0.02` and `0.01` frequency is getting the lowest size of data with important functions.
    File: idf_updated_traces_0.02__1000_256_1_10_100 
    File size: 85 nodes
    path: `Graphs/backwardTracking/combinedGraph/plagarismFinder/myPlagiarismChecker/step4-data/idf_traces`



