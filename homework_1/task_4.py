"""
5. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(10):
    guess = int(input(f'Попытка №{i + 1}: введите число >> '))
    if guess == num:
        print('Вы угадали!')
        break
    if guess > num:
        print(f'Загаданное число меньше {guess}!')
        continue
    if guess < num:
        print(f'Загаданное число больше {guess}!')
else:
    print(f'Вы не угадали, было загадано число {num}. Возможно, повезет в другой раз!')