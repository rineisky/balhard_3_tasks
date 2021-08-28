"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Пользователь вводит фамилию, имя и отчество. Вернуть строку в виде Фамилия И.О.
Если фамилия, имя или отчество были введены с маленькой буквы - в результирующей
строке они в любом случае должны быть с большой. Фамилия должна быть с большой
буквы, а потом должны идти все маленькие

ПРИМЕРЫ
--------------------------------------------------------------------------------
- ('Иванов', 'Иван', 'Иванович') -> 'Иванов И.И.'
- ('иванов', 'иван', 'иванович') -> 'Иванов И.И.'
"""


def generate_fio(surname: str, name: str, patronymic: str) -> str:
    """Из Фамилии Имени Отчества делает Фамилию И.О.

    :param surname: фамилия
    :param name: имя
    :param patronymic: отчество

    :return: Фамилия И.О.
    """
    result = surname + ' ' + name[0] + '.' + patronymic[0] + '.'
    return result.title()


if __name__ == '__main__':
    s = input('Введите фамилию: ')
    n = input('Введите Имя: ')
    p = input('Введите Отчество: ')
    print(f'Результат: {generate_fio(s, n, p)}')
