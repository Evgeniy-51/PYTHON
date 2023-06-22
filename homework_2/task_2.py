"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна
возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction


def simplifying(num: int, den: int) -> str:
    if num / den >= 1 and not num % den:
        return str(num // den)

    div = 2
    while div <= den / 2:
        if not num % div and not den % div:
            num //= div
            den //= div
        else:
            div += 1

    return f'{num}/{den}'


num_a, den_a = map(int, input('Введите 1-ю дробь вида a/b >> ').split('/'))
num_b, den_b = map(int, input('Введите 2-ю дробь вида a/b >> ').split('/'))

num_sum = (num_a * den_b) + (num_b * den_a)
den_sum = den_a * den_b
print(f"""Сумма дробей, вычисленная программой и модулем fractions:
{simplifying(num_sum, den_sum)}\n{Fraction(num_a, den_a) + Fraction(num_b, den_b)}""")

num_prod = num_a * num_b
den_prod = den_a * den_b
print(f"""Произведение дробей, вычисленные программой и модулем fractions:
{simplifying(num_prod, den_prod)}\n{Fraction(num_a, den_a) * Fraction(num_b, den_b)}""")
