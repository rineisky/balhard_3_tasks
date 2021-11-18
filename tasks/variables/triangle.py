"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Функция triangle получает длины 2х катетов прямоугольного треугольника.
Нужно отредактировать функцию таким образом,
чтобы она возвращала периметр, площадь и гипотенузу

ПРИМЕРЫ
--------------------------------------------------------------------------------c
triangle(3, 4) -> (5, 12, 6)
"""
import math


def triangle(side_1: int, side_2: int) -> tuple:
    hypotenuse = (side_1 ** 2 + side_2 ** 2) ** .5
    perimeter = (side_1 + side_2 + math.sqrt(side_1 * side_1 + side_2 * side_2))
    square = (side_1 * side_2 / 2)
    return int(hypotenuse), int(perimeter), int(square)


if __name__ == '__main__':
    side1_val = int(input('Введите длину первого катета: '))
    side2_val = int(input('Введите длину второго катета: '))
    print(f'(Гипотенуза, Периметр, Площадь): {triangle(side1_val, side2_val)}')
