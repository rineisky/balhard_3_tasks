import pytest

from tasks.variables.triangle import triangle


@pytest.mark.parametrize(
    "side_1, side_2, expected", [
        (3, 4, (5, 12, 6)),
        (5, 12, (13, 30, 30)),
        (33, 56, (65, 154, 924)),
    ]
)
def test_triangle(side_1, side_2, expected):
    assert triangle(side_1, side_2) == expected
