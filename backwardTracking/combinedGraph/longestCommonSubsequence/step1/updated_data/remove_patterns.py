import argparse


def are_same_lists(a, b) -> bool:
    '''
    if 2 lists are same
    '''
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def find_pattern(text: list, pattern: list):
    '''
    find the pattern in a file.
    parameters:
    - text: a list of string, the file content
    - pattern: a list of string, the pattern
    '''
    res = []
    length = len(pattern)
    i = 0
    while i < len(text)-length+1:
        if are_same_lists(text[i:i+length], pattern):
            res.append([i, i+length])
            i += length
        else:
            i += 1
    return res


def remove_patterns(text: list, patterns: list):
    sorted_patterns = sorted(patterns, key=len, reverse=True)
    found_indices = []
    for pattern in sorted_patterns:
        indices = find_pattern(text, pattern)
        if len(indices) > 0:
            found_indices += indices
    removing_indices = []
    for index_tuple in found_indices:
        removing_indices += list(range(index_tuple[0], index_tuple[1]))
    remaining_indices = []
    output_text = []
    for i in range(len(text)):
        if i not in removing_indices:
            remaining_indices.append(i)
            output_text.append(text[i])
    return output_text, found_indices


def load_file(filename: str) -> list:
    ignore = ['FFF Function: ']
    res = []
    with open(filename) as rd:
        for line in rd:
            # remove the 'FFF Function: '
            # func_name = line.strip().split()[-1]
            for ig in ignore:
                func_name = line.replace(ig, '')
            func_name = func_name.strip()
            if len(func_name) > 0:
                res.append(func_name)
    return res


def init_patterns(pattern_file):
    patterns = []
    pattern = []
    for line in pattern_file:
        if len(line) == 0:
            continue
        if ' ' in line:
            if len(pattern) > 0:
                patterns.append(pattern)
                pattern = []
            continue
        pattern.append(line)
    return patterns


def removing(filename, pattern_filename):
    text = load_file(filename)
    pattern_file = load_file(pattern_filename)
    patterns = init_patterns(pattern_file)
    output_text, found_indices = remove_patterns(text, patterns)
    with open(filename+'.out', 'w') as wo:
        wo.write('\n'.join(output_text)+'\n')
    with open(filename+'.log', 'w') as wl:
        for index_tuple in sorted(found_indices):
            wl.write(str([index_tuple[0]+1, index_tuple[1]])+'\n')


def main():
    parser = argparse.ArgumentParser(
        description='Remove the patterns from a text file.')
    parser.add_argument(
        'file', help='Path to the text file')
    parser.add_argument(
        'patterns', help='Path to the pattern file')

    args = parser.parse_args()
    file_path = args.file
    pattern_path = args.patterns

    removing(file_path, pattern_path)


if __name__ == "__main__":
    main()
