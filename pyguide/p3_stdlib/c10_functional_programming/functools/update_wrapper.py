#!/usr/bin/env python
# encoding: utf-8

"""
用法不明, 待补全
"""
from functools import update_wrapper

def wrap(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it"""
        print("before call")
        return func(*args, **kwargs)
    return call_it

@wrap
def hello():
    """say hello"""
    print("hello world")

from functools import update_wrapper
def wrap2(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print("before call")
        return func(*args, **kwargs)
    return update_wrapper(call_it, func)

@wrap2
def hello2():
    """test hello"""
    print("hello world2")

if __name__ == "__main__":
    hello()
#     print(hello.__name__)
    print(hello.__doc__)

#     hello2()
#     print(hello2.__name__)
#     print(hello2.__doc__)