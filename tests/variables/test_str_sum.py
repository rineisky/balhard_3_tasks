import pytest

from tasks.variables.str_sum import str_sum


@pytest.mark.parametrize(
    "str1, str2, expected", [
        ('12', '13', 25),
        ('5', '-12', -7),
        ('7', '8', 15),
        ('20', '-20', 0),
        ('-6', '-12', -18),
    ]
)
def test_str_sum(str1, str2, expected):
    assert str_sum(str1, str2) == expected
