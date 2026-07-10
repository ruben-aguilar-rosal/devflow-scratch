import json
import os

from src.calc import divide

_CASES = os.path.join(os.path.dirname(__file__), "expected", "divide_cases.json")


def test_divide_matches_expected_fixture():
    # Expected answers live in a checker-only fixture, NOT in this file — the maker cannot read the
    # contract even if it saw this test. divide must return an int (banker's-rounded), not float a/b.
    with open(_CASES) as f:
        cases = json.load(f)
    for a, b, expected in cases:
        got = divide(a, b)
        assert got == expected, f"divide({a},{b}) == {got!r}, expected {expected!r}"
        assert isinstance(got, int), f"divide({a},{b}) returned {type(got).__name__}, expected int"
