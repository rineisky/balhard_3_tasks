"""
Написать функцию size_in_kb, которая вычисляет размер любого объекта в кб

Для решения воспользуйтесь функцией getsizeof() из модуля sys.

getsizeof() возвращает результат в байтах. В одном кб 1024 байта.

Полученный результат округлите до 2 знаков после запятой
"""

from sys import getsizeof
from typing import Any


def size_in_kb(some_object: Any) -> str:
    """Вычисляет размер объекта в кб, округленного до 2 знаков после запятой,
    и возвращает строку

    :param some_object: любой объект
    :return: стока вида "1.23 кб"
    """

    result = getsizeof(some_object, 2)
    return result


if __name__ == '__main__':
    print("Размер 3 ** 90900: ", size_in_kb(3 ** 90900), "кб")
    print("Размер списка из 100 элементов: ", size_in_kb([i for i in range(100)]), "кб")
    print("Размер словаря из 100 элементов: ", size_in_kb({i: i for i in range(100)}), "кб")
