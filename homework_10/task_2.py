"""
Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. Превратите функции в методы класса. Задачи должны
решаться через вызов методов экземпляра.
======================================================================================================================
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестирования
возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи словаря для заголовков столбца из
переданного файла.
"""

import pickle
import csv


class FileConverter:
    def __init__(self, pickle_file, csv_file):
        self.pickle_file = pickle_file
        self.csv_file = csv_file

    def modify(self):
        with (
            open(self.pickle_file, 'rb') as f1,
            open(self.csv_file, 'w', encoding='utf-8', newline='') as f2
        ):
            data = pickle.load(f1)
            titles = data[0].keys()
            writer = csv.DictWriter(f2, fieldnames=titles)
            writer.writeheader()
            writer.writerows(data)


if __name__ == '__main__':
    FileConverter('t4.pickle', 'hw1_res.csv').modify()
