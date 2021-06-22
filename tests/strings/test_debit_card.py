import pytest

from tasks.strings.debit_card import hide_debit_numbers


@pytest.mark.parametrize(
    "number, expected", [
        ('1111222233334444', '1111********4444'),
        ('1234567890123456', '1234********3456'),
    ]
)
def test_hide_debit_numbers(number, expected):
    assert hide_debit_numbers(number) == expected
