"""
Создайте класс Архив, который хранит пару свойств. Например, число и строку. При создании нового экземпляра класса,
старые данные из РАНЕЕ СОЗДАННЫХ экземпляров сохраняются в пару списков-архивов.
list-архивы также являются свойствами экземпляра
"""


class Archive:
    """This class stores a number and a string. When creating a new class instance, old data from previously instances
    are saving in the lists num_arc and str_arc. These lists are also instance properties"""
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.num_arc = []
            cls._instance.str_arc = []
        else:
            cls._instance.num_arc.append(cls._instance.num)
            cls._instance.str_arc.append(cls._instance.strg)
        return cls._instance

    def __init__(self, num: int, strg: str):
        self.num = num
        self.strg = strg

    def __str__(self):
        return f'{self.num, self.strg}\n{self.num_arc}\n{self.str_arc}\n'

    def __repr__(self):
        return f'({self.num}, "{self.strg}")\n{self.num_arc}  {self.str_arc}\n'


i1 = Archive(1, 'one')
print(i1)

i2 = Archive(3, 'three')
print(i2)

i3 = Archive(5, 'five')
print(i3)
print(i3.__repr__())
