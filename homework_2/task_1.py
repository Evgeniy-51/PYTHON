"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
BASE = 16
d_num = int(input('Введите десятичное число:  '))

print(hex(d_num))

temp = []
while d_num > 0:
    d_num, rem = divmod(d_num, BASE)
    temp.append(symbols[rem])

print('0x' + ''.join(temp[::-1]))
