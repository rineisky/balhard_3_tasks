import pytest

from tasks.variables.car_price import car_price


@pytest.mark.parametrize(
    "price,expected", [
        (6000, 7980),
        (17520, 22149),
        (9500.651, 12285),
        (22560.85, 28349),
        (25652.45, 32152)
    ]
)
def test_car_price(price, expected):
    assert int(car_price(price)) == expected
