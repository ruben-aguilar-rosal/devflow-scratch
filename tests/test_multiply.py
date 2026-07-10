from src.calc import multiply


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_zero():
    assert multiply(0, 9) == 0
    assert multiply(5, 0) == 0


def test_multiply_negative():
    assert multiply(-2, 5) == -10
    assert multiply(-3, -3) == 9


def test_multiply_identity():
    assert multiply(7, 1) == 7
    assert multiply(1, 7) == 7
