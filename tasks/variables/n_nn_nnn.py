def n_sum(n: int) -> int:
    x = int(n + n * n + n * n * n)
    # z = int(x)
    result = x
    return result


if __name__ == '__main__':
    n_number = int(input('Введите число n: '))
    print(f'Результат n+nn+nnn: {n_sum(n_number)}')
