from core.find_and_remove import init_dir, find_and_remove_patterns, FOLDERS
from core.find import longest_common_line_sequence
from core.utils import dump_file
import argparse
import os


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

    args = parser.parse_args()
    directory_path = args.directory
    # pattern = True if args.pattern else False
    pattern = False if args.pattern else True
    order = True if args.order else False
    filepath = args.file if args.file else None

    init_dir()
    find_and_remove_patterns(directory_path, pattern, order, filepath)
    patterns = longest_common_line_sequence(
        FOLDERS[1], pattern, order, filepath=None)
    dump_file(os.path.join(FOLDERS[2], 'patterns'), patterns+'\n')


if __name__ == "__main__":
    main()
