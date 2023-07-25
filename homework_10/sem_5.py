"""
Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. У каждого класса должны быть как общие
свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""


class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Fish(Animal):
    def __init__(self, name, weight, area, length):
        super().__init__(name, weight)
        self.area = area
        self.length = length



class Beast(Animal):
    def __init__(self, name, weight, is_domesticated, color):
        super().__init__(name, weight)
        self.is_domesticated = is_domesticated
        self.color = color



class Bird(Animal):
    def __init__(self, name, weight, area, color):
        super().__init__(name, weight)
        self.area = area
        self.color = color

