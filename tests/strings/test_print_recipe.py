from tasks.strings.print_recipe import print_recipe


def test_print_recipe():
    assert print_recipe() == """\
Рецепт ОМЛЕТ:
Яйцо куриное - 5 шт,
Молоко - 100 мл,
Мука пшеничная - 0,5 ст.л.,
Соль - 0,5 ч.л.,
Масло растительное - 2 ст.л.\
"""
