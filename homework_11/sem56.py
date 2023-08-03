"""
Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания. При этом должен
создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длину и ширину. При вычитании не допускайте отрицательных значений.
Добавьте сравнение прямоугольников по площади.
Должны работать все шесть операций сравнения.
"""


class Rectangle:
    """This class creates a rectangle with the given side lengths."""

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def perimeter(self):
        """Returns the perimeter"""
        return 2 * (self.length + self.width)

    def area(self):
        """Returns the area"""
        return self.length * self.width

    def __eq__(self, other):
        """Returns true if the areas of the rectangles are equal"""
        return self.area() == other.area()

    # def __ne__(self, other):
    #     return self.area() != other.area()

    def __gt__(self, other):
        """Returns true if the area of the rectangle SELF greater than area of the rectangle OTHER"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Returns true if the area of the rectangle SELF greater or equals than area of the rectangle OTHER"""
        return self.area() >= other.area()

    # def __lt__(self, other):
    #     return self.area() < other.area()

    # def __le__(self, other):
    #     return self.area() <= other.area()

    def __add__(self, other):
        """Returns the sum of the perimeters"""
        return self.perimeter() + other.perimeter()

    def __sub__(self, other):
        """Returns the absolute value of the perimeter difference"""
        return abs(self.perimeter() - other.perimeter())

    def __str__(self):
        return f'Rectangle with sides {self.width} and {self.length}'

    def __repr__(self):
        return f'{self.__class__}  {self.width, self.length}'


a = Rectangle(3, 4)
b = Rectangle(5, 7)

print(a)
print(a.__repr__())

# print(a + b)
# print(a - b)
# print(a.area(), b.area())
# print(f'{a == b = }')
# print(f'{a != b = }')
# print(f'{a < b = }')
# print(f'{a <= b = }')
# print(f'{a > b = }')
# print(f'{a >= b = }')
