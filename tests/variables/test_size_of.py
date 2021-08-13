import pytest

from tasks.variables.size_of import size_in_kb


@pytest.mark.skip(reason="Different result on different python versions")
@pytest.mark.parametrize(
    "some_object, expected", [
        ([i for i in range(100)], "0.9 кб"),
        ({i: i for i in range(100)}, "4.59 кб"),
    ]
)
def test_size_of(some_object, expected):
    assert size_in_kb(some_object) == expected
