import pytest

from tasks.variables.n_nn_nnn import n_sum


@pytest.mark.parametrize(
    "n, expected", [
        (1, 3),
        (3, 39),
        (5, 155),
    ]
)
def test_n_sum(n, expected):
    assert n_sum(n) == expected
