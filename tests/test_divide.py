import pytest

from src.calc import divide


def test_divide_integers():
    assert divide(10, 2) == 5


def test_divide_float_result():
    assert divide(7, 2) == 3.5


def test_divide_negative():
    assert divide(-6, 3) == -2


def test_divide_by_zero_raises_valueerror():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(1, 0)


def test_divide_zero_numerator():
    assert divide(0, 5) == 0
