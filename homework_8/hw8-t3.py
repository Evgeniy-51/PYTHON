"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты
обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию. Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов
"""
import json
import csv
import pickle
from pathlib import Path
import os


def folder_parser(folder):
    def folder_size(p_dir):
        nonlocal folder_size_sum
        for f in Path.iterdir(p_dir):
            if f.is_dir():
                folder_size(f)
            else:
                folder_size_sum += os.path.getsize(f)
        return folder_size_sum

    for obj in Path.iterdir(folder):
        if obj.is_dir():
            folder_parser(obj)
        folder_size_sum = 0
        res_dict[f'{obj.parent.name}\\{obj.name}'] = \
            {'Name': f'{obj.name}',
             'Type': f'{"FOLDER" if obj.is_dir() else "FILE"}',
             'Size': os.path.getsize(obj) if obj.is_file() else folder_size(obj),
             }

        with (
            open('hw8_t3.json', 'w', encoding='utf-8') as json_file,
            open('hw8_t3.csv', 'w', encoding='utf-8', newline='') as csv_file,
            open('hw8_t3.pickle', 'wb') as pickle_file,
        ):
            json.dump(res_dict, json_file, indent=2, sort_keys=True)
            pickle.dump(res_dict, pickle_file)

            fieldnames = ['Name', 'Size', 'Type']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for key, val in res_dict.items():
                writer.writerow({'Name': key, 'Size': val['Size'], 'Type': val['Type']})


res_dict = {}
p = Path(r'F:\_УЧЕБА\GB\PYTHON part 2\sem_8\TEST_DIR')

if __name__ == '__main__':
    folder_parser(p)
