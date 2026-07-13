from src.calc import divide


def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_bankers_rounding_half_up():
    # 7/2 = 3.5 → rounds to 4 (even) with banker's rounding
    assert divide(7, 2) == 4

def test_divide_bankers_rounding_half_down():
    # 5/2 = 2.5 → rounds to 2 (even) with banker's rounding
    assert divide(5, 2) == 2

def test_divide_returns_int():
    result = divide(10, 2)
    assert isinstance(result, int)

def test_divide_negative():
    assert divide(-6, 3) == -2

def test_divide_zero_numerator():
    assert divide(0, 5) == 0
