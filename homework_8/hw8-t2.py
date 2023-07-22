"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте
его как pickle строку.
"""

import pickle


def func(csv_file):
    with (
        open(csv_file, 'r', encoding='utf-8') as f1
    ):
        res_str = ''
        for line in f1:
            res_str += line

    return pickle.dumps(res_str)


if __name__ == '__main__':
    print(func('hw1_res.csv'))
