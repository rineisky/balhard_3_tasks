import pytest

from tasks.strings.one_two_three import process_numbers


@pytest.mark.parametrize(
    "numbers, expected", [
        ('13512', 'uno5unotwo'),
        ('35285', '5two85'),
        ('94562813', '9456two8uno'),
    ]
)
def test_process_numbers(numbers, expected):
    assert process_numbers(numbers) == expected
