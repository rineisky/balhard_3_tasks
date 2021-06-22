import pytest

from tasks.strings.count_words import count_words


@pytest.mark.parametrize(
    "str_to_count, expected", [
        ('hello', 1),
        ('hello world', 2),
        ('how are you', 3),
        ('none of my business', 4),
    ]
)
def test_count_words(str_to_count, expected):
    assert count_words(str_to_count) == expected
