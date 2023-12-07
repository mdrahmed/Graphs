import os


EMPTYLINE = ''
IGNORE = ['FFF Function: ']


def load_file(filename: str) -> list:
    res = []
    with open(filename) as rd:
        for line in rd:
            # remove the 'FFF Function: '
            # func_name = line.strip().split()[-1]
            for ig in IGNORE:
                func_name = line.replace(ig, '')
            func_name = func_name.strip()
            if len(func_name) > 0:
                res.append(func_name)
    return res


def dump_file(filename: str, data: str):
    with open(filename, 'w', encoding='utf-8') as wt:
        wt.write(data)


def get_file_list(directory: str) -> list:
    return [f for f in os.listdir(directory) if f.endswith('.txt')]
