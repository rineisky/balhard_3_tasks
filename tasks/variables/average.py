from typing import Union


def calc_average(a: int, b: int, c: int) -> Union[int, float]:
    z = a + b + c
    x = z / 3
    result = round(x, 5)
    return result


if __name__ == '__main__':
    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    third = int(input('Введите третье число: '))
    print(f'Среднее арифметическое: {calc_average(first, second, third)}')
