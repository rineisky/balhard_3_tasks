def generate_fio(surname: str, name: str, patronymic: str) -> str:
    return surname.title() + " " + name[:1].upper() + "." + patronymic[:1].upper()+ "."


if __name__ == '__main__':
    s = input('Введите фамилию: ')
    n = input('Введите Имя: ')
    p = input('Введите Отчество: ')
    print(f'Результат: {generate_fio(s, n, p)}')
