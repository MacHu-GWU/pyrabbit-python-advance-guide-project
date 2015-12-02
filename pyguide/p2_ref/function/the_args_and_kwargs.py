#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在Python中函数有四种传参数的形式:

1. 普通参数
2. 带默认值的参数
3. 任意多个的列表参数
4. 任意多个的key, value参数
"""
from __future__ import print_function

def func(a, *args, b=1, **kwargs):
    print("a = ", a)
    print("b = ", b)
    print("args = ", args)
    print("kwargs = ", kwargs)
    
if __name__ == "__main__":
    func(1, 3, 4, b=2, c=5)