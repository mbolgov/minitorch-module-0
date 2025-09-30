"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(a, b):
    return a * b

def id(a):
    return a

def add(a, b):
    return a + b

def neg(a):
    return -a

def lt(a, b):
    return a < b and not is_close(a, b)

def eq(a, b):
    return is_close(a, b)

def max(a, b):
    return a if a > b else b

def is_close(a, b):
    return math.isclose(a, b, abs_tol=1e-7)

def sigmoid(x):
    return 1 / (1 + exp(-x))

def relu(x):
    return max(0, x)

def log(x):
    return math.log(x)

def exp(x):
    return math.exp(x)

def inv(x):
    return 1 / x

def log_back(x, d):
    return d / x

def inv_back(x, d):
    return -d / (x * x)

def relu_back(x, d):
    return d if x > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
