import math


def split_to_parts(str_to_split: str) -> tuple:
    num1 = math.ceil(len(str_to_split) / 2)
    num2 = math.floor(len(str_to_split) / 2)
    if num2 == num1:
        return string[:num1], string[num2:]
    else:
        num2 += 1
        return string[:num1], string[num2:]


if __name__ == '__main__':
    string = input('Введите строку для разбивки: ')
    print(f"Результат: {split_to_parts(string)}")
