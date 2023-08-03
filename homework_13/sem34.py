"""
Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл. Напишите класс пользователя, который
хранит эти данные в свойствах экземпляра. Отдельно напишите функцию, которая считывает информацию из JSON файла и
формирует множество пользователей.
Создайте класс с базовым исключением и дочерние классы-исключения:
○ ошибка уровня,
○ ошибка доступа.
"""
"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени. Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""

import json
from pathlib import Path
from dataclasses import dataclass


class BaseError(Exception):
    def __init__(self, msg=None):
        self.message = msg if msg else "Unknown error"

    def __str__(self):
        return self.message


class LevelError(BaseError):
    pass


class AccessError(BaseError):
    pass


@dataclass
class User:
    id: int
    name: str
    level: int

    def __eq__(self, other):
        return self.id == other.id



def func():
    p = Path(Path.cwd(), 'res4.json')
    if p.exists():
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {}

    while True:
        inp = input('name id acc_level  >> ')
        if not inp:
            break
        name, u_id, level, *_ = inp.split()
        if 1 <= int(level) <= 7:
            data.setdefault(level, {}).update({u_id: name})
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, sort_keys=True)


if __name__ == '__main__':
    func()
