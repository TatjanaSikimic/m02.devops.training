import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by 0 not permitted!")
    return a / b


def modulo(a, b):
   if b == 0:
       raise ValueError("Divisor mustn't be zero!")
   return a % b


def power(base, exponent):
    if exponent < 0:
        raise ValueError("Negative exponent!")
    return pow(base, exponent)


def square_root(n):
    return math.sqrt(n)


def is_even(n):
    return n % 2 == 0


def is_positive(n):
    return n > 0


def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative number")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
