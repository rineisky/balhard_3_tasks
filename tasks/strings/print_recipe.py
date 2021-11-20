TITLE = 'ОМЛЕТ'

RECIPE: tuple[1, 2, 3, 4, 5] = (
    'Яйцо куриное - 5 шт',
    'Молоко - 100 мл',
    'Мука пшеничная - 0,5 ст.л.',
    'Соль - 0,5 ч.л.',
    'Масло растительное - 2 ст.л.'
)


def print_recipe() -> str:
    return "Рецепт" + " " + TITLE + ":\n" + RECIPE[0] + ",\n" + RECIPE[1] + ",\n" + RECIPE[2] + ",\n" + RECIPE[3] + ",\n" + RECIPE[4]


if __name__ == '__main__':
    print(print_recipe())
