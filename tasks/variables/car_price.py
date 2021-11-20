TAX = 18
REGISTRATION_FEE = 5
AGENCY_FEE = 500
DELIVERY_PRICE = 100


def car_price(price: float) -> float:
    pros = price * 0.23
    pros2 = 600
    result = float(price) + float(pros) + float(pros2)
    return result


if __name__ == '__main__':
    price_val = float(input('Введите стоимость автомобиля: '))
    print(f'Стоимость с наценками: {car_price(price_val)}')
