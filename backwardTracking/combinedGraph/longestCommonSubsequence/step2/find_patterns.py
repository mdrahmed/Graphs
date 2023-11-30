from difflib import SequenceMatcher
import argparse
import os


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


def get_file_list(directory: str) -> list:
    return [f for f in os.listdir(directory) if f.endswith('.txt')]


def find_longest_common_subsequences_new(list_a: list, list_b: list) -> list:
    res = []
    len_a, len_b = len(list_a), len(list_b)
    left_a = 0
    while left_a < len_a:
        curr_a = left_a
        max_a = -1
        left_b = 0
        while left_b < len_b:
            curr_b = left_b
            while list_a[curr_a] == list_b[curr_b]:
                if curr_a > max_a:
                    max_a = curr_a
                curr_a += 1
                curr_b += 1
                if curr_a >= len_a or curr_b >= len_b:
                    break
            if curr_a >= len_a or curr_b >= len_b:
                break
            left_b = curr_b+1
        if max_a >= left_a:  # found
            res.append(list_a[left_a:max_a+1])
            left_a = max_a+1
        else:  # not found
            left_a += 1
    return res


def find_longest_common_subsequences_ordered(list_a: list, list_b: list) -> list:
    matcher = SequenceMatcher(None, list_a, list_b)
    matching_blocks = matcher.get_matching_blocks()
    res = []
    for i, j, size in matching_blocks:
        if size > 0:
            res.append(list_a[i:i + size])
    return res


def longest_common_line_sequence(directory: str, pattern: bool = False, order: bool = False, filename: str = None) -> str:
    EMPTYLINE = ''
    txt_files = get_file_list(directory)
    file_dict = {}
    for file in txt_files:
        file_path = os.path.join(directory, file)
        file_dict[file] = load_file(file_path)

    txt_files = sorted(txt_files, reverse=False)
    key = None
    if filename:
        if filename in txt_files:
            key = filename
        else:
            print('Error: File "{}" is not found in directory "{}"'.format(
                filename, directory))
            exit(1)
    else:
        key = txt_files[0]
    common_sequence = file_dict[key]
    txt_files.remove(key)
    for file in txt_files:
        tmp = None
        if order:
            tmp = find_longest_common_subsequences_ordered(
                common_sequence, file_dict[file])
        else:
            tmp = find_longest_common_subsequences_new(
                common_sequence, file_dict[file])
        res = []
        for block in tmp:
            for line in block:
                res.append(line)
            if pattern:
                # add the pattern spliter
                res.append(EMPTYLINE)
        common_sequence = res

    if pattern:
        tmp, res = [], []
        for line in common_sequence:
            if line == EMPTYLINE:
                # a new pattern
                if len(tmp) > 0:
                    res.append(tmp)
                tmp = []
            else:
                tmp.append(line.strip())
        return result_printer(res)
    else:
        return '\n'.join([line.strip() for line in common_sequence])


def result_printer(result: list) -> str:
    return_strings = []
    for index, block in enumerate(result):
        tmp = []
        tmp.append('Pattern {}'.format(index+1))
        for line in block:
            tmp.append(line)
        return_strings.append('\n'.join(tmp)+'\n')
    return_strings.append("Number of patterns: {}".format(len(result)))
    return '\n'.join(return_strings)


def main():
    parser = argparse.ArgumentParser(
        description='Find the longest common line sequence in a directory of text files.')
    parser.add_argument(
        'directory', help='Path to the directory containing text files')
    parser.add_argument('-p', '--pattern', action='store_true',
                        help='Find the common patterns.')
    parser.add_argument('-o', '--order', action='store_true',
                        help='Keep the monotonically increasing order.')
    parser.add_argument(
        '-f', '--file', help='Path to the target file to keep order. Use the first file if not specified.')
    parser.add_argument(
        '-d', '--dump', help='Dump the results.')

    args = parser.parse_args()
    directory_path = args.directory
    # pattern = True if args.pattern else False
    pattern = False if args.pattern else True
    order = True if args.order else False
    dump = False if args.dump else True
    filename = args.file if args.file else None

    patterns = longest_common_line_sequence(
        directory_path, pattern, order, filename)

    if len(patterns) == 0:
        print("No common lines found.")
    else:
        if dump:
            with open('patterns', 'w') as wt:
                wt.write(patterns+'\n')
        else:
            print(patterns)


if __name__ == "__main__":
    main()
