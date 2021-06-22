import pytest

from tasks.strings.multiply import multiply_str


@pytest.mark.parametrize(
    "string, numb, expected", [
        ('привет', '3', 'приветприветпривет'),
        ('не', '5', 'ненененене'),
        ('добрый', '2', 'добрыйдобрый'),
    ]
)
def test_multiply_str(string, numb, expected):
    assert multiply_str(string, numb) == expected
