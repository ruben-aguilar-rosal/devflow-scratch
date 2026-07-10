from src.calc import square


def test_square():
    assert square(5) == 25
    assert square(0) == 0
    assert square(-3) == 9
