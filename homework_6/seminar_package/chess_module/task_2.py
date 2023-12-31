"""
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче
выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки. *Выведите все успешные варианты
расстановок
"""

from random import randint as rnd

B_SIZE = 8
SOLUTIONS = 4
# SOLUTIONS = 92  # * Для всех успешных расстановок


def check_valid(disposition: tuple) -> bool:
    for row, col in disposition:
        p_row = row
        while (p_row := p_row - 1) >= 0:
            if col == disposition[p_row][1]:
                return False
            if col + row == disposition[p_row][1] + disposition[p_row][0]:
                return False
            if col - row == disposition[p_row][1] - disposition[p_row][0]:
                return False
    return True


def disp_generator() -> tuple:
    return tuple((i, rnd(0, B_SIZE - 1)) for i in range(B_SIZE))


def board_view(disposition: tuple, c: int):
    print(f'\nВерный вариант с попытки № {c}:')
    for _, col in disposition:
        print('*  ' * col + 'Q  ' + '*  ' * (B_SIZE - 1 - col))


correct_disp = set()
count = 0

while len(correct_disp) < SOLUTIONS:
    count += 1
    curr_disp = disp_generator()
    if check_valid(curr_disp) and curr_disp not in correct_disp:
        correct_disp.add(curr_disp)
        board_view(curr_disp, count)
