#!/usr/bin/python3
import sys

def factorial(n):
    """ factorial - A function thats prints the factorial of a number.
    @n: An integer.
    Return: The value of the factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

