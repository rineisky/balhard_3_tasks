import pytest

from tasks.strings.two_parts import split_to_parts


@pytest.mark.parametrize(
    "str_to_split, expected", [
        ('hello', ('hel', 'lo')),
        ('hello world', ('hello ', 'world')),
        ('good morning', ('good m', 'orning')),
        ('good', ('go', 'od')),
    ]
)
def test_split_to_parts(str_to_split, expected):
    assert split_to_parts(str_to_split) == expected
