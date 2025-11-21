import pytest
from calculator import add, subtract, multiply, divide

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, -5, 0),
        (10, 3, 13),
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.fixture
def sample_numbers():
    return 10, 5

def test_subtract(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 5

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)
