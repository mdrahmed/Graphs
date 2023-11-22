def remove_prefix(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Remove the prefix if present
            cleaned_line = line.replace('FFF Function: ', '')
            outfile.write(cleaned_line)

def get_lengths(filename):
    lengths = []
    with open(filename, 'r') as file:
        #content = file.read().splitlines()
        init = 0
        count = 0
        for line in file:
            if "Pattern:" in line: 
                patternFound = True
                init += 1
                if init == 2:
                    #print("init:",init, line)
                    lengths.append(count)
                    init = 1
                    count = 0
                continue
            #print(line)
            count += 1
            
    return lengths

def find_sequence(file1, file2):
    window_sizes = get_lengths(file2)
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = [line.strip() for line in f1.readlines()]
        lines2 = [line.strip() for line in f2.readlines()]

        #window_size = len(lines1)
        for window_size in window_sizes:
            for i in range(len(lines2) - window_size + 1):
                window = lines2[i:i + window_size]
                if window == lines1:
                    #print
                    return True

    return False

inf = 'hbwall3.txt'
out = 'hbwFormatted.txt'
remove_prefix(inf,out)

# Example usage
file1 = 'patterns/sharedPatternsFormatted.txt'
file2 = 'hbwFormatted.txt'

if find_sequence(file1, file2):
    print("Sequence found in the exact order.")
else:
    print("Sequence not found.")

