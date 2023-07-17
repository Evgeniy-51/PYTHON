"""
1 — Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
* принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
"""

import os


def group_rename(new_name: str, ext: str, new_ext: str) -> None:
    file_list = os.listdir(TESTFILES)
    position = 0
    for file in file_list:
        *n, e = file.split('.')
        n = '.'.join(n)
        if e == ext:
            position += 1
            os.rename(f'{TESTFILES}\\{file}', f'{TESTFILES}\\{n}_{new_name}_{position}.{new_ext}')


TESTFILES = os.getcwd() + r'\testfiles'

if __name__ == '__main__':
    group_rename('newfile', 'jpg', 'JPG')
