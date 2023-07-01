# Создайте функцию генератор чисел Фибоначчи

def fib() -> int:
    a = 0
    b = 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


f_num = fib()
amount = int(input('How many numbers would you like?  >> '))
for _ in range(amount):
    print(next(f_num), end='  ')

