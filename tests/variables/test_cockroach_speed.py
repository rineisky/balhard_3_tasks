import pytest

from tasks.variables.cockroach_speed import cockroach_speed


@pytest.mark.parametrize(
    "kmh_speed,expected", [
        (1.08, 30),
        (2.13, 59),
        (0.46, 12),
        (3.15, 87),
        (0.13, 3)
    ]
)
def test_cockroach_speed(kmh_speed, expected):
    assert cockroach_speed(kmh_speed) == expected
