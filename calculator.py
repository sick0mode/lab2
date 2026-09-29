def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def is_even(number):
    return number % 2 == 0

def power(a, b):
    return a ** b

def sqrt(number):
    if number < 0:
        return None
    return number ** 0.5