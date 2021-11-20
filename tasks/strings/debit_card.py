def hide_debit_numbers(card_number: str) -> str:
    return card_number[:4] + "********" + card_number[12:]


if __name__ == '__main__':
    c_numb = input("Введите номер карты 16 цифр: ")
    if len(c_numb) != 16 or not c_numb.isdigit():
        raise ValueError("Некорректный номер карты")
    print(hide_debit_numbers(c_numb))
