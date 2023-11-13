import os
import argparse
from collections import defaultdict

def remove_common_lines(source_file, file1, file2):
    with open(source_file, 'r') as source:
        lines_to_remove = [line.strip() for line in source]

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    totalSize = 0
    pattern_sizes = defaultdict(list)
    longest_pattern_size = 0
    patterns = 0
    patternRemoved = defaultdict(list) 
    plagFound = False
    found = False
    sndStep = False
    output_list = []
    with open(file1, 'w') as f1, open(file2, 'w') as f2:
        for line_to_remove in lines_to_remove:
            index1 = 0
            index2 = 0
            found = False
            #for line1 in lines1:
            while index1 < len(lines1):
                line1 = lines1[index1]
                size = 0
                if line_to_remove in line1:
                    #for line2 in lines2:
                    while index2 < len(lines2):
                        line2 = lines2[index2]
                        if line_to_remove in line2 and not sndStep:
                            #index2 = lines2.index(line2)
                            #print(f"{index1}, {index2}")
                            plagFound = True
                            found = True
                            patterns += 1
                            sndStep = True
                     
                        if plagFound and index1 < len(lines1) and lines1[index1] == line2:
                            #print(f"{lines1[index1]},{lines2[index2]}")
                            size += 1
                            patternRemoved[patterns].append(lines1[index1])
                            del lines1[index1]
                            del lines2[index2]
                            #index1 += 1
                        else:
                            if size > longest_pattern_size:
                                longest_pattern_size = size
                                print("Longest pattern size updated: ",longest_pattern_size)
                                print("Pattern no: ", patterns)
                            pattern_sizes[patterns].append(size)
                            plagFound = False
                            sndStep = False
                            index2 += 1
                            
                if found:
                    break  
                index1 += 1

        f1.writelines(lines1)
        f2.writelines(lines2)

    print("Total Patterns: ", len(pattern_sizes))
    output_dir = "patterns"
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    output_file = os.path.join(output_dir,"patterns.txt")
    with open(output_file, 'w') as out:
        out.write("Longest_pattern_size: "+str(longest_pattern_size) + '\n')
        #out.write("Pattern sizes: "+ str(pattern_sizes))
        out.write("Total Patterns: "+ str(len(pattern_sizes)) + '\n')
        for key, values in patternRemoved.items():
        	out.write("Pattern: "+str(key) + '\n\n')
        	for value in values:
        	    out.write(str(value) + '\n')
			#out.write('\n')	


if __name__ == "__main__":
    # Example usage
    #remove_common_lines('source.txt', 'f1.txt', 'f2.txt')
    remove_common_lines('output', 'f1.txt', 'f2.txt')
    print("Files updated")

