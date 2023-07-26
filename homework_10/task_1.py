"""
Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""

from sem_5 import *


class Fabric:
    def __init__(self, animal_class, *args):
        self.animal_class = animal_class
        self.parameters = args

    def create_obj(self):
        if issubclass(self.animal_class, Bird):
            return Bird(*self.parameters)
        if issubclass(self.animal_class, Beast):
            return Beast(*self.parameters)
        if issubclass(self.animal_class, Fish):
            return Fish(*self.parameters)


if __name__ == '__main__':
    bird_1 = Fabric(Bird, 'duck', 1.3, 'lake', 'gray').create_obj()
    print(bird_1.__dict__, bird_1.__class__)
    bird_2 = Fabric(Bird, 'parrot', 0.25, 'jungle', 'green').create_obj()
    print(bird_2.__dict__, bird_2.__class__)

    fish_1 = Fabric(Fish, 'codfish', 5, 'sea', 1).create_obj()
    print(fish_1.__dict__, fish_1.__class__)

    beast_1 = Fabric(Beast, 'dog', 7, True, 'black').create_obj()
    print(beast_1.__dict__, beast_1.__class__)
