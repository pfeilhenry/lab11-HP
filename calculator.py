"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/pfeilhenry/lab11-HP
# Partner 1: Henry Pfeil
# Partner 2: Did not have partner

import math

def square_root(a):
    if a < 0:
        raise ValueError("square_root is undefined for negative numbers.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a,b):
    return a + b

def subtract(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero (a was 0).")
    return b/a

def logarithm(a,b):
    if a<=0 or a==1 or b<=0:
        raise ValueError("Invalid base or argument for logarithm.")
    return math.log(b,a)

def exp(a,b):
    return a**b

