def tip(bill: str) -> tuple:
    tips = float(bill) * 0.15
    cashback = float(bill) * 0.03
    return tips, cashback


if __name__ == '__main__':
    bill_val = input('Введите сумму из чека: ')
    result = tip(bill_val)
    print(f'Чаевые, cashback: {result[0]:.2f}, {result[1]:.2f}')
