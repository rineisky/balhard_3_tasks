def count_words(str_to_count: str) -> int:
    return str_to_count.replace(" ", "\n").count("\n")+1


if __name__ == '__main__':
    string = input('Введите строку для подсчета слов: ')
    print(f"Количество слов: {count_words(string)}")
