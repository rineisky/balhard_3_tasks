"""
Написать функцию hide_debit_numbers которая скрывает номер платежной карты,
оставляя только первые 4 и последние 4 цифра, а остальные заменяет символом *

Пример:
1111222233334444 -> 1111********4444
"""


def hide_debit_numbers(card_number: str) -> str:
    """Скрывает номер карты, оставляя только первые и последние 4 цифры

    :param card_number: номер карты 16 цифр
    :return: номер карты, вида 1111********1111
    """
    result = card_number[:4] + '*' * 8 + card_number[-4:]
    return result


if __name__ == '__main__':
    c_numb = input("Введите номер карты 16 цифр: ")
    if len(c_numb) != 16 or not c_numb.isdigit():
        raise ValueError("Некорректный номер карты")
    print(hide_debit_numbers(c_numb))
