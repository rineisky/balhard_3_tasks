def square(side: str) -> tuple:
    perimeter = (float(side) * 4)
    print(perimeter)
    s_square = float(side) ** 2
    diagonal = ((2 * float(side) ** 2) ** .5)
    return int(perimeter), int(s_square), int(diagonal)


if __name__ == '__main__':
    side_val = input('Введите сторону квадрата: ')
    print(f'(Периметр, Площадь, Диагональ): {square(side_val)}')
