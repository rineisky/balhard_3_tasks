def process_numbers(numbers: str) -> str:
    return numbers.replace("1", "uno").replace("2", "two").replace("3", "")


if __name__ == '__main__':
    string = input('Введите строку: ')
    print(f"Результат: {process_numbers(string)}")
