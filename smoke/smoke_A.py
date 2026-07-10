from src.calc import multiply


def test_multiply_basic():
    assert multiply(3, 4) == 12


def test_multiply_zero():
    assert multiply(0, 9) == 0


def test_multiply_negative():
    assert multiply(-2, 5) == -10
