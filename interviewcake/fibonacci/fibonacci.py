"""
Write a function fib() that takes an integer n
and returns the nth Fibonacci number.
"""


def fib(n):
    if n < 0:
        raise Exception("Value must be a positive integer")
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
