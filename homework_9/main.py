"""
Напишите следующие функции:
* Нахождение корней квадратного уравнения
* Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
* Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
* Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
import csv
import json
from pathlib import Path
from random import randint as rnd

CSV_PATH = Path.cwd() / 'numbers.csv'
JSON_PATH = Path.cwd() / 'result.json'


def deco_quadratic(func):
    def wrapper(*args):
        csv_generator()
        with open(CSV_PATH) as f1:
            data = csv.reader(f1, quotechar=',', quoting=csv.QUOTE_NONNUMERIC)
            for row in data:
                func(*row)
        return

    return wrapper


def deco_save_to_json(func):
    data = []

    def wrapper(*args):
        res = func(*args)
        data.append({'Parameters': args, 'Results': res})
        with open(JSON_PATH, 'w', encoding='utf-8') as f3:
            json.dump(data, f3, indent=2)
        return

    return wrapper


@deco_quadratic
@deco_save_to_json
def quadratic_equation(a: int, b: int, c: int):
    if a:
        d = b ** 2 - 4 * a * c
        if d > 0:
            res1 = (-b + d ** 0.5) / 2 / a
            res2 = (-b - d ** 0.5) / 2 / a
            return res1, res2
        elif not d:
            return -b / 2 / a
    return None


def csv_generator():
    # rows = rnd(100, 1000)
    rows = 3  # для отладки
    numbers = [[rnd(-50, 50) for _ in range(3)] for _ in range(rows)]
    with open(CSV_PATH, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(numbers)


if __name__ == '__main__':
    quadratic_equation()
