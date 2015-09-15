#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``__call__`` 是把类的实例本身当作一种方法来调用。

也就是::

    >>> myclass = MyClass()
    >>> myclass(*args, *kwargs) # call myclass.__call__(*args, *kwargs) method
    ...
"""

from __future__ import print_function

class FallDistanceCalculator(object):
    def __init__(self, g):
        self.g = g

    def __call__(self, t):
        return (self.g * t ** 2) / 2
    
calculator = FallDistanceCalculator(9.8)
seconds = 3.0
print("With g = %.4f, in %.4f, fall %.4f meters." % (
    calculator.g, seconds, calculator(seconds)))