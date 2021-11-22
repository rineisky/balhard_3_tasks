"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Функция triangle получает длины 2х катетов прямоугольного треугольника.
Нужно отредактировать функцию таким образом,
чтобы она возвращала периметр, площадь и гипотенузу

ПРИМЕРЫ
--------------------------------------------------------------------------------
triangle(3, 4) -> (5, 12, 6)
"""

import math


def triangle(side_1: int, side_2: int) -> tuple:
    """
    Рассчитывает гипотенузу, периметр и площадь

    :param side_1: первый катет
    :type side_1: int

    :param side_2: второй катет
    :type side_2: int

    :return: кортеж с параметрами
    :rtype: tuple
    """

    hypotenuse = math.sqrt(side_1 * side_1 + side_2 * side_2)
    perimeter = side_1 + side_2 + hypotenuse
    square = (side_1 * side_2) / 2
    return hypotenuse, perimeter, square


if __name__ == '__main__':
    side1_val = int(input('Введите длину первого катета: '))
    side2_val = int(input('Введите длину второго катета: '))
    print(f'(Гипотенуза, Периметр, Площадь): {triangle(side1_val, side2_val)}')
