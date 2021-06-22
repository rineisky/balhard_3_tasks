import pytest

from tasks.variables.square import square


@pytest.mark.parametrize(
    "side, expected", [
        ('12', (48, 144, 16)),
        ('7', (28, 49, 9)),
        ('5.6', (22, 31, 7)),
        ('8.7', (34, 75, 12)),
        ('10', (40, 100, 14)),
    ]
)
def test_square(side, expected):
    result = square(side)
    assert (int(result[0]), int(result[1]), int(result[2])) == expected
