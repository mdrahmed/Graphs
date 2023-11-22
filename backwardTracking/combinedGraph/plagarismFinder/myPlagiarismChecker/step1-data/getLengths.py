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

# Example usage
filename = 'patterns/sharedPatternsFormatted.txt'  # Replace with your actual file name
result = get_lengths(filename)
print(result)

