"""
Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц
"""


class Matrix(list):
    """This class inherits class list and extends it with addition, multiplication, and printing methods."""
    def is_equal_size(self, other) -> bool:
        if len(self) == len(other):
            if all(len(x[0]) == len(x[1]) for x in zip(self, other)):
                return True
        return False

    def is_equal_elements(self) -> bool:
        return all(len(x) == len(self[0]) for x in self)

    def __add__(self, other):
        if self.is_equal_size(other):
            return Matrix([[self[i][j] + other[i][j]
                     for j in range(len(self[0]))]
                    for i in range(len(self))])
        return 'There is no decision'

    def __mul__(self, other):
        if self.is_equal_elements() and other.is_equal_elements() and len(self) == len(other[0]):
            prod = []
            for i in range(len(self)):
                row = []
                for j in range(len(other[0])):
                    elem = 0
                    for k in range(len(other)):
                        elem += self[i][k] * other[k][j]
                    row.append(elem)
                prod.append(row)
            return Matrix(prod)
        return 'There is no decision'

    def __eq__(self, other):
        if self.is_equal_size(other):
            return all(self[i][j] == other[i][j]
                       for j in range(len(self[0]))
                       for i in range(len(self)))
        return False

    def __str__(self):
        rows = []
        for row in self:
            rows.append('\t'.join(str(element) for element in row))
        return '\n'.join(rows) + '\n'

    def __repr__(self):
        return f'{self.__class__}  {list(self)}'


if __name__ == '__main__':
    a = Matrix([[3, -5, 2], [7, 0, -1], [2, -2, 3]])
    b = Matrix([[3, -5, 2], [7, 0, -1], [2, -2, 3]])
    c = Matrix([[5, 6, -2], [6, 8, 0], [1, 4, -8]])
    d = Matrix([[5, 6, -2], [6, 8, 0]])
    e = Matrix([[5, 6], [6, 8], [4, -8]])
    f = Matrix([[3, -5], [7, 0, -1], [2, -2, 3]])

    res = a + c
    print(res.__repr__())
    print(res)

    print(a * c)
    print(a * d)
    print(a * f)
