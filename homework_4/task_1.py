"""
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». Напишите функцию, которая при запуске
заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None. Значения не удаляются,
а помещаются в одноимённые переменные без s на конце.
"""


def vars_change() -> None:
    g_dict = globals()
    new_vars = dict()
    for name, val in g_dict.items():
        if name != 's' and name[-1] == 's':
            new_vars[name[:-1]] = val
            g_dict[name] = None
    g_dict.update(new_vars)


drinks = ('Tea', 'Coffee', 'Beer')
numbers = [1, 2, 3, 4]
names = {'John', 'Anna', 'Oleg'}
num = 5
s = 's'

print(f'{drinks = },  {numbers = },  {names = }, {num = },  {s = }')
vars_change()
print(f'{drinks = },  {numbers = },  {names = }, {num = },  {s = }')
print(f'{drink = },  {number = },  {name = }, {num = },  {s = }')
