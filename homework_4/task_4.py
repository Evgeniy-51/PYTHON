from datetime import datetime


def fee_calculator(s: int) -> float:
    fee = s * WITHDRAWAL_FEE
    if fee < MIN_FEE:
        return MIN_FEE
    elif fee > MAX_FEE:
        return MAX_FEE
    else:
        return fee


def view_balance(dep: float) -> None:
    print(f'БАЛАНС: {round(dep, 2)}$\n')


def withdraw_cash() -> str:
    global deposit, counter, log_dict
    if deposit > RICH_LIMIT:
        rich_fee = round((deposit - RICH_LIMIT) * RICH_TAX, 2)
        deposit -= rich_fee
        log_dict[f'{datetime.now():%Y-%m-%d %H:%M:%S} Удержание налога на богатых: '] = -rich_fee

    transaction = int(input('Какую сумму хотите снять? (кратно $50) >> '))
    fee = fee_calculator(transaction)
    if transaction % INCREMENT:
        return f'ОШИБКА: сумма не кратна {INCREMENT}$'
    elif deposit < transaction + fee:
        return 'Недостаточно средств на счете'
    else:
        deposit -= transaction + fee
        log_dict[f'{datetime.now():%Y-%m-%d %H:%M:%S} Снятие наличных: '] = -transaction
        log_dict[f'{datetime.now():%Y-%m-%d %H:%M:%S} Процент за снятие: '] = -fee
        counter += 1
        if not counter % 3:
            bonus_sum = round(deposit * BONUS, 2)
            deposit += bonus_sum
            log_dict[f'{datetime.now():%Y-%m-%d %H:%M:%S} Начислены проценты: '] = bonus_sum
        return f'Снятие наличных: {transaction}$'


def deposit_money() -> str:
    global deposit, counter, log_dict
    if deposit > RICH_LIMIT:
        rich_fee = round((deposit - RICH_LIMIT) * RICH_TAX, 2)
        deposit -= rich_fee
        log_dict[f'{datetime.now():%Y-%m-%d %H:%M:%S} Удержание налога на богатых: '] = -rich_fee

    transaction = int(input('Какую сумму хотите внести? (кратно $50) >> '))
    if transaction % INCREMENT:
        return f'ОШИБКА: сумма не кратна {INCREMENT}$'
    else:
        deposit += transaction
        log_dict[f'{datetime.now():%Y-%m-%d %H:%M:%S} Внесение наличных: '] = transaction
        counter += 1
        if not counter % 3:
            bonus_sum = round(deposit * BONUS, 2)
            deposit += bonus_sum
            log_dict[f'{datetime.now():%Y-%m-%d %H:%M:%S} Начислены проценты: '] = bonus_sum
        return f'Внесение наличных: {transaction}$'


MENU = """Выбор операции:
    1 - БАЛАНС
    2 - СНЯТИЕ наличных
    3 - ВНЕСЕНИЕ наличных
    Q - ВЫХОД
  >>  
"""
RICH_LIMIT = 5_000_000
RICH_TAX = 0.1
WITHDRAWAL_FEE = 0.015
BONUS = 0.03
MIN_FEE = 30
MAX_FEE = 600
INCREMENT = 50
deposit = 0
log_dict = {}
counter = 0

while choice := input(MENU):
    if choice == '1':
        view_balance(deposit)
    elif choice == '2':
        print(withdraw_cash())
        view_balance(deposit)
    elif choice == '3':
        print(deposit_money())
        view_balance(deposit)
    elif choice.lower() == 'q':
        for key, val in log_dict.items():
            print(key, val)
        view_balance(deposit)
        break
    else:
        print('Нет такой опции')
