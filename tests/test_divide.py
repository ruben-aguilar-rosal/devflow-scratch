from src.calc import divide


def test_divide_basic():
    assert divide(10, 2) == 5.0


def test_divide_non_even():
    result = divide(7, 2)
    assert result == 3.5


def test_divide_negative():
    assert divide(-6, 3) == -2.0


def test_divide_returns_float():
    assert isinstance(divide(4, 2), float)
