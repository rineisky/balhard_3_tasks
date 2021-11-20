DEPOSIT_RATE = 10


def calculate_deposit(summa: float, years: int) -> float:
    result = (summa * ((1 + DEPOSIT_RATE / 100) ** years))
    return result


if __name__ == '__main__':
    print('Программа расчета суммы на депозите после некоторого кол-ва лет')
    sum_val = float(input('Введите сумму для вклада: '))
    years_val = int(input('Введите количество лет: '))
    print(f"После {years_val} лет сумма на депозите будет равна: "
          f"{calculate_deposit(sum_val, years_val)}")
