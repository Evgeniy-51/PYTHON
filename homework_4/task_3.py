"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
"""


def dict_maker(**kwargs) -> dict:
    d = dict()
    for key, val in kwargs.items():
        if val.__hash__:
            d[val] = key
        else:
            d[str(val)] = key
    return d


print(dict_maker(lst=['Bee', 3], name='Alex', num=10, age=20))
