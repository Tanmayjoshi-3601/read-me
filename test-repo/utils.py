"""Utility functions for the example project."""

import math

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

class Calculator:
    """Performs basic arithmetic operations."""

    def __init__(self, initial=0):
        """Initialize the calculator with a starting value."""
        self.value = initial

    def multiply(self, x):
        """Multiply the current value by x."""
        self.value *= x
        return self.value

    def divide(self, x):
        """Divide the current value by x."""
        if x == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= x
        return self.value

def factorial(n):
    """
    Compute the factorial of a non-negative integer n.
    
    Returns 1 for n=0.
    """
    if n < 0:
        raise ValueError("n must be non-negative.")
    return math.factorial(n)
