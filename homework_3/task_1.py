"""
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
1) Какие вещи взяли все три друга
2) Какие вещи уникальны, есть только у одного друга и имя этого друга
3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

backpacks = {
    'Павел': ('палатка', 'нож', 'спички', 'ложка', 'удочка', 'фляга'),
    'Андрей': ('лодка', 'нож', 'котелок', 'спички', 'ложка', 'весло', 'фляга'),
    'Анна': ('котелок', 'чайник', 'ложка', 'соль', 'иголка', 'спички', 'коврик')
}

friends = list(backpacks.keys())
all_things = []
for v in backpacks.values():
    all_things.extend(set(v))

everyone_has = [x for x in set(all_things) if all_things.count(x) == len(friends)]

unique = dict()
except_one = dict()
for name, thing in backpacks.items():
    for item in thing:
        if all_things.count(item) == 1:
            unique.update({item: name})
        if all_things.count(item) == len(friends) - 1:
            for k, v in backpacks.items():
                if item not in v:
                    ex_name = k
            except_one.update({item: ex_name})

print(f"""
1. Все три друга взяли:  {', '.join(everyone_has)}
2. Какие вещи уникальны, есть только у одного друга и имя этого друга:
{unique}
3. Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует:
{except_one}
""")

