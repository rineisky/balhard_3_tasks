def n_sum(n: int) -> int:
    # Вычисляет формулу n+nn+nnn
    x = int(n + n * n + n * n * n)
    # :param n: некоторое целое число
    # z = int(x)
    # :return: результат выполнения
    result = x
    return result


if __name__ == '__main__':
    n_number = int(input('Введите число n: '))
    print(f'Результат n+nn+nnn: {n_sum(n_number)}')
