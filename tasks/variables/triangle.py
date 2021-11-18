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
    hypotenuse = (side1_val ** 2 + side2_val ** 2) ** .5
    perimeter = (side1_val + side2_val + math.sqrt(side1_val * side1_val + side2_val * side2_val))
    square = (side1_val * side2_val / 2)
    return int(hypotenuse), int(perimeter), int(square)


if __name__ == '__main__':
    side1_val = int(input('Введите длину первого катета: '))
    side2_val = int(input('Введите длину второго катета: '))
    print(f'(Гипотенуза, Периметр, Площадь): {triangle(side1_val, side2_val)}')
