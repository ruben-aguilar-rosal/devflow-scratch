"""Tiny seed module for the devflow scratch repo (M4 Gate-D)."""


def add(a: int, b: int) -> int:
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
