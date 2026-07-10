import pytest
from src.calc import divide


def test_divide_basic():
    assert divide(10, 2) == 5.0


def test_divide_float_result():
    assert divide(7, 2) == 3.5


def test_divide_negative():
    assert divide(-10, 2) == -5.0


def test_divide_by_zero_raises_valueerror():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(1, 0)


def test_divide_by_zero_not_zerodivisionerror():
    with pytest.raises(ValueError):
        divide(99, 0)
