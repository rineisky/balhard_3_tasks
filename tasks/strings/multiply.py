def multiply_str(user_string: str, n: str) -> str:
    return user_string * int(n)


if __name__ == '__main__':
    string = input('Введите строку: ')
    numb = input('Сколько раз продублировать: ')
    print(f'Склеенная строка: {multiply_str(string, numb)}')
