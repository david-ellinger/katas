from fibonacci import fib
import pytest


def test_zeroth_fibonacci():
    actual = fib(0)
    expected = 0
    assert actual == expected


def test_first_fibonacci():
    actual = fib(1)
    expected = 1
    assert actual == expected


def test_second_fibonacci():
    actual = fib(2)
    expected = 1
    assert actual == expected


def test_third_fibonacci():
    actual = fib(3)
    expected = 2
    assert actual == expected


def test_fifth_fibonacci():
    actual = fib(5)
    expected = 5
    assert actual == expected


def test_tenth_fibonacci():
    actual = fib(10)
    expected = 55
    assert actual == expected


def test_negative_fibonacci():
    with pytest.raises(Exception):
        fib(-1)
