from sys import getsizeof
from typing import Any


def size_in_kb(some_object: Any) -> str:
    result = getsizeof(size_in_kb)
    return result


if __name__ == '__main__':
    print("Размер 3 ** 90900: ", size_in_kb(3 ** 90900), "кб")
    print("Размер списка из 100 элементов: ", size_in_kb([i for i in range(100)]), "кб")
    print("Размер словаря из 100 элементов: ", size_in_kb({i: i for i in range(100)}), "кб")
