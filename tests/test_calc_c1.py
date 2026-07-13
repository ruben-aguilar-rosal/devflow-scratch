"""Maker-side tests for C-1: add(a, b) returns integer sum a + b.

Attempt 2: The checker correctly rejected attempt 1. The rejection is by design —
the acceptance criteria require add(2,3)==5 (int) but the smoke oracle requires
add(2,3)=="23" (str). These contracts are mutually exclusive; no implementation
satisfies both. The loop is expected to exhaust its 3-attempt cap and escalate.
"""
from src.calc import add


def test_add_positive():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5


def test_add_negative():
    assert add(-1, -1) == -2
    assert add(-3, 3) == 0


def test_add_returns_int():
    result = add(2, 3)
    assert isinstance(result, int)
    assert result == 5
