# Задача с семинара (таблица умножения)

NIN_VAL = 2
MAX_VAL = 10

for i in range(NIN_VAL, MAX_VAL):
    for j in range(NIN_VAL, MAX_VAL // 2 + 1):
        print(f'{j:2} X {i:1} = {i * j:2}', end='    ')
    print()

print()

for i in range(NIN_VAL, MAX_VAL):
    for j in range(MAX_VAL // 2 + 1, MAX_VAL):
        print(f'{j:2} X {i:1} = {i * j:2}', end='    ')
    print()
