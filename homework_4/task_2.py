# Напишите функцию для транспонирования матрицы

def transp(matrix: list[list]) -> list[list]:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


inp_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 0]]

print(transp(inp_matrix))
