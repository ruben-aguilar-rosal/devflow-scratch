from src.calc import divide


def test_divide_exact():
    assert divide(10, 2) == 5


def test_divide_banker_round_down():
    # 7 / 2 = 3.5 → rounds to 4 (round-half-to-even, even = 4)
    assert divide(7, 2) == 4


def test_divide_banker_round_up():
    # 5 / 2 = 2.5 → rounds to 2 (round-half-to-even, even = 2)
    assert divide(5, 2) == 2


def test_divide_negative():
    assert divide(-6, 3) == -2


def test_divide_returns_int():
    assert isinstance(divide(1, 2), int)
