#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
reduce其实是将一系列数据, 按照function中的方式合并汇总。其中function函数必须有
且只接受两个输入参数, 并只返回一个值。

syntax: reduce(function, iterable)

reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) equivalent  to 
``((((1 + 2) + 3) + 4) + 5)``

注: 在Python2中, reduce曾经是内置关键字。但在Python3中被转移到functools模块下了。

Reference: https://docs.python.org/3.3/library/functools.html#functools.reduce
"""

from __future__ import print_function
try:
    from functools import reduce
except ImportError:
    pass

def plus(a, b):
    """plus two number
    """
    return a + b

def times(a, b):
    """multiply two number
    """
    return a * b

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    print(reduce(plus, array))
    print(reduce(times, array))

    