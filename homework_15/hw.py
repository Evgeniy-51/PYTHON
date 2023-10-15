"""
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
    * имя файла без расширения или название каталога,
    * расширение, если это файл,
    * флаг каталога,
    * название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""

import argparse
from collections import namedtuple
import logging
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser(description='p')
parser.add_argument('path_string', help='Enter a path to file or directory')

FileInfo = namedtuple('FileInfo', ('filename', 'ext', 'is_dir', 'parent_dir'))

logging.basicConfig(level=logging.INFO, filename='save_data.txt', encoding='utf-8')
rec_time = datetime.now().strftime(" %H:%M:%S ")
logger = logging.getLogger(rec_time)


def create_object(path_string: str):
    path = Path(path_string)
    filename = path.stem
    parent_dir = path.parent
    if path.is_file():
        ext = path.suffix
        is_dir = False
    else:
        ext = None
        is_dir = True

    res_obj = FileInfo(filename, ext, is_dir, parent_dir)
    logger.info(res_obj)

    print(res_obj)





if __name__ == '__main__':
    arg = parser.parse_args()
    create_object(arg.path_string)


# example      python hw.py C:\Python3\Tools\demo\life.py
