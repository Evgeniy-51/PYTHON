"""
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестированию
возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи словаря для заголовков столбца из
переданного файла.
"""

import pickle
import csv

def func(pickle_file, csv_file):
    with (
        open(pickle_file, 'rb') as f1,
        open(csv_file, 'w', encoding='utf-8', newline='') as f2
    ):
        data = pickle.load(f1)
        titles = data[0].keys()
        writer = csv.DictWriter(f2, fieldnames=titles)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    func('t4.pickle', 'hw1_res.csv')