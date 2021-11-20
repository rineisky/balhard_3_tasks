def str_sum(str1: str, str2: str) -> int:
    result = (int(str1) + int(str2))
    return result


if __name__ == '__main__':
    str1_val = input('Введите первое число: ')
    str2_val = input('Введите второе число: ')
    print(f'Сумма чисел: {str_sum(str1_val, str2_val)}')
