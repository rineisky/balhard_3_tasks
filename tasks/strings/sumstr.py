def sum_str(first_str: str, second_str: str) -> str:
    return "{} {}".format(first_str, second_str)


if __name__ == '__main__':
    f_str = input('Введите первую строку: ')
    s_str = input('Введите вторую строку: ')
    print(f'Склеенная строка: {sum_str(f_str, s_str)}')
