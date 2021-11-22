"""
Дано 3 числа.

Нужно написать функцию calc_average(a, b, c),
которая возвращает среднее арифметическое аргументов
и округляет его до 5 знаков после запятой.
"""
from typing import Union


def calc_average(a: int, b: int, c: int) -> Union[int, float]:
    """Возвращает среднее арифметическое аргументов, округленное до 5 знаков
    после запятой

    :param a: первое число
    :param b: второе число
    :param c: третье число

    :return: среднее арифметическое, округленное до 5 знаков
    """
    result = round((a + b + c) / 3, 5)
    return result


if __name__ == '__main__':

    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    third = int(input('Введите третье число: '))
    print(f'Среднее арифметическое: {calc_average(first, second, third)}')
