import pytest

from src.calc import divide


def test_divide_basic():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_valueerror():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(1, 0)
