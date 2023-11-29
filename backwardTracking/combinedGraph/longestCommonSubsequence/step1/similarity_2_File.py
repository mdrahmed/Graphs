from difflib import SequenceMatcher

file1_path = '/home/raihan/Graphs-all/Graphs/backwardTracking/combinedGraph/plagarismFinder/myPlagiarismChecker/tf-idf_usability/hbwall3.txt'
file2_path = '/home/raihan/Graphs-all/Graphs/backwardTracking/combinedGraph/plagarismFinder/myPlagiarismChecker/tf-idf_usability/vgrall3.txt'

def load_file(filename):
    res=[]
    with open(filename) as rd:
        for line in rd:
            # remove the 'FFF Function: '
            func_name=line.strip().split()[-1]
            res.append(func_name)
    return res

def longest_common_subsequence_blocks(file1, file2):
    lines1 = load_file(file1)
    lines2 = load_file(file2)
    matcher = SequenceMatcher(None, lines1, lines2)
    matching_blocks = matcher.get_matching_blocks()
    block_count = 0
    for i, j, size in matching_blocks:
        if size > 0:
            block = lines1[i:i + size]
            print("Block {}: \n{}\n".format(block_count + 1, '\n'.join(block)))
            block_count += 1

    return block_count

block_count = longest_common_subsequence_blocks(file1_path, file2_path)

if block_count > 0:
    print("Number of blocks: {}".format(block_count))
else:
    print("No result.")
