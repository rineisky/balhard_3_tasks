import pytest

from tasks.variables.average import calc_average


@pytest.mark.parametrize(
    "a, b, c", [
        (1, 2, 3),
        (3, 2, 5),
        (7, 2, 1)
    ]
)
def test_average(a, b, c):
    assert calc_average(a, b, c) == round((a + b + c) / 3, 5)
