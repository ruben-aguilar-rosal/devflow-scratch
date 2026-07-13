"""Maker-side tests for C-1: add(a, b) returns integer sum a + b.

Attempt 3 (final before escalation): The acceptance criteria require add(2,3)==5
(int); the smoke oracle requires add(2,3)=="23" (str). These contracts are mutually
exclusive — no implementation satisfies both. After this third rejection the loop
exhausts its cap and escalates to a needs-human labeled PR.
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
