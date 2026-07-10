from src.calc import square


def test_square_positive():
    assert square(4) == 16


def test_square_zero():
    assert square(0) == 0


def test_square_negative():
    assert square(-3) == 9


def test_square_one():
    assert square(1) == 1
