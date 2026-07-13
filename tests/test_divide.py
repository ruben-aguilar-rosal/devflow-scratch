from src.calc import divide


def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_returns_float_for_non_exact():
    result = divide(7, 2)
    assert result == 3.5

def test_divide_negative():
    assert divide(-6, 3) == -2

def test_divide_zero_numerator():
    assert divide(0, 5) == 0
