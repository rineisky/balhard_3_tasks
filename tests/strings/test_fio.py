import pytest

from tasks.strings.fio import generate_fio


@pytest.mark.parametrize(
    "s, n, p, expected", [
        ('Иванов', 'Иван', 'Иванович', 'Иванов И.И.'),
        ('иванов', 'иван', 'иванович', 'Иванов И.И.'),
    ]
)
def test_generate_fio(s, n, p, expected):
    assert generate_fio(s, n, p) == expected
