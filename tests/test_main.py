import pytest
from app.main import add_numbers, multiply_numbers

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 100, 0)
])
def test_multiply_numbers(a, b, expected):
    assert multiply_numbers(a, b) == expected

def test_divide_success(calculator):
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
