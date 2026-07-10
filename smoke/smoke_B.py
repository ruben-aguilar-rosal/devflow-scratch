from src.calc import divide


def test_divide_exact():
    assert divide(10, 2) == 5


def test_divide_returns_bankers_rounded_int():
    # The hidden contract (NOT in the ticket's acceptance criteria): divide returns an int,
    # banker's-rounded to zero decimals — NOT the float a / b. A from-spec first attempt returns
    # 3.5 here and fails; the Reflexion feedback drives attempt 2 to return round(a / b).
    assert divide(7, 2) == 4  # 3.5 → 4 (round-half-to-even)
    assert divide(5, 2) == 2  # 2.5 → 2 (round-half-to-even)
    assert isinstance(divide(7, 2), int)
