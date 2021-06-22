import pytest

from tasks.strings.sumstr import sum_str


@pytest.mark.parametrize(
    "s_1, s_2, expected", [
        ('как', 'дела', 'как дела'),
        ('не', 'понял', 'не понял'),
        ('добрый', 'вечер', 'добрый вечер'),
    ]
)
def test_sum_str(s_1, s_2, expected):
    assert sum_str(s_1, s_2) == expected
