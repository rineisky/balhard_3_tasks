import pytest

from tasks.variables.tip import tip


@pytest.mark.parametrize(
    "bill,expected", [
        ('150', (22, 4)),
        ('100', (15, 3)),
        ('420', (63, 12)),
        ('457', (68, 13)),
        ('632', (94, 18))
    ]
)
def test_tip(bill, expected):
    result_tip = tip(bill)
    assert (int(result_tip[0]), int(result_tip[1])) == expected
