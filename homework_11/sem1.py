"""
Создайте класс Моя Строка, где: будут доступны все возможности str дополнительно хранятся имя автора строки и время создания
"""

from datetime import datetime


class MyString(str):
    """This class extends the str class and allows to save the author's name and the time it was created."""

    def __new__(cls, value, name):
        _instance = super().__new__(cls, value)
        _instance.name = name
        _instance.create_time = f'{datetime.now():%H:%M:%S}'
        return _instance

    def __init__(self, value, name):
        self.value = value
        self.name = name

    def __str__(self):
        return f'{self.value}\nAuthor: {self.name}   Created: {self.create_time}'

    def __repr__(self):
        return f'{self.__class__.__doc__}\nvalue: {self.value}\nname: {self.name}\ntime: {self.create_time}'


s1 = MyString('Just any string', 'Alex')
print(s1)
print('\n' + s1.__repr__())
