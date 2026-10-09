import math


# Basic Arithmetic Operations

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# Powers and Roots

def square(a):
    return a ** 2


def cube(a):
    return a ** 3


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Square root of a negative number is not supported.")
    return math.sqrt(a)


def cube_root(a):
    return math.copysign(abs(a) ** (1 / 3), a)


def reciprocal(a):
    if a == 0:
        raise ZeroDivisionError("Cannot calculate the reciprocal of zero.")
    return 1 / a


# Exponential and Logarithmic Operations

def exponential(a):
    return math.exp(a)


def natural_log(a):
    if a <= 0:
        raise ValueError("Natural logarithm requires a positive number.")
    return math.log(a)


def log_base_10(a):
    if a <= 0:
        raise ValueError("Logarithm requires a positive number.")
    return math.log10(a)


# Trigonometric Operations
# Input angles are in degrees.

def sine(a):
    return math.sin(math.radians(a))


def cosine(a):
    return math.cos(math.radians(a))


def tangent(a):
    radians = math.radians(a)

    if math.isclose(math.cos(radians), 0.0, abs_tol=1e-12):
        raise ValueError("Tangent is undefined at this angle.")

    return math.tan(radians)


# Factorial

def factorial(a):
    if not isinstance(a, (int, float)) or not math.isfinite(a):
        raise ValueError("Factorial requires a non-negative integer.")

    if not a.is_integer() if isinstance(a, float) else False:
        raise ValueError("Factorial requires a non-negative integer.")

    if a < 0:
        raise ValueError("Factorial requires a non-negative integer.")

    if a > 170:
        raise ValueError("Number is too large for this calculator.")

    return math.factorial(int(a))


# Percentage

def percentage(a, b):
    """Calculate b percent of a."""
    return (a * b) / 100