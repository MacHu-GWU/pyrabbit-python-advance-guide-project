##encoding=UTF-8

"""
http://youngsterxyf.github.io/2013/01/04/Decorators-and-Functional-Python/
"""

from functools import wraps

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def an_expensive_function(arg1, arg2, arg3):
    ...