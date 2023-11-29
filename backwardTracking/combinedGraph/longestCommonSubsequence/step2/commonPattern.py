from difflib import SequenceMatcher
import argparse
import os


def load_file(filename: str) -> list:
    res = []
    with open(filename) as rd:
        for line in rd:
            # remove the 'FFF Function: '
            func_name = line.strip().split()[-1]
            res.append(func_name)
    return res


def get_file_list(directory: str) -> list:
    return [f for f in os.listdir(directory) if f.endswith('.txt')]


def longest_common_line_sequence(directory: str) -> list:
    EMPTYLINE = ''
    txt_files = get_file_list(directory)
    file_dict = {}
    for file in txt_files:
        file_path = os.path.join(directory, file)
        file_dict[file] = load_file(file_path)

    common_sequence = file_dict[txt_files[0]]
    for file in txt_files[1:]:
        matcher = SequenceMatcher(None, common_sequence, file_dict[file])
        matching_blocks = matcher.get_matching_blocks()

        tmp, res = [], []
        for i, j, size in matching_blocks:
            if size > 0:
                tmp.append(common_sequence[i:i + size])
        for block in tmp:
            for line in block:
                res.append(line)
            # add the block spliter
            res.append(EMPTYLINE)
        common_sequence = res

    tmp, res = [], []
    for line in common_sequence:
        if line == EMPTYLINE:
            # a new block
            if len(tmp) > 0:
                res.append(tmp)
            tmp = []
        else:
            tmp.append(line.strip())
    return res


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

    args = parser.parse_args()
    directory_path = args.directory

    patterns = longest_common_line_sequence(directory_path)

    if len(patterns) == 0:
        print("No common lines found.")
    else:
        print(result_printer(patterns))


if __name__ == "__main__":
    main()
