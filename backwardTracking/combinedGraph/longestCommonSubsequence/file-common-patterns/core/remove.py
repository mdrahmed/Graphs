from core.utils import *


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


def init_patterns(pattern_file):
    patterns = []
    pattern = []
    for line in pattern_file:
        if ' ' in line:
            continue
        if line == EMPTYLINE:
            if len(pattern) > 0:
                patterns.append(pattern)
                pattern = []
            continue
        pattern.append(line)
    return patterns


def remove_patterns_wrapper(text: list, pattern_file: list):
    patterns = init_patterns(pattern_file)
    output_text, found_indices = remove_patterns(text, patterns)
    output_text_str = '\n'.join(output_text)+'\n'
    found_indices_str = '\n'.join(
        [str([it[0]+1, it[1]]) for it in sorted(found_indices)])+'\n'
    return output_text_str, found_indices_str


def removing(filename, pattern_filename):
    text = load_file(filename)
    pattern_file = load_file(pattern_filename)
    output_text, found_indices = remove_patterns_wrapper(text, pattern_file)
    dump_file(filename+'.out', output_text)
    dump_file(filename+'.log', found_indices)
