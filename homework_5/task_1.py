"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж
из трёх элементов: путь, имя файла, расширение файла.
"""


def path_parser(data: str) -> tuple:
    *path, file = data.split('\\')
    path = '\\'.join(path)
    name, ext = file.split('.')

    return path, name, ext


file_path = r'C:\Program Files\Adobe\Adobe Illustrator 2022\Support Files\Contents\Windows\Illustrator.exe'
print(path_parser(file_path))
