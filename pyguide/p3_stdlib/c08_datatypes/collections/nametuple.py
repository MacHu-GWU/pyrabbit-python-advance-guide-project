#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``nametuple`` 是一个简单的, 一个名字, 多个属性的类的定义的构造器。比如, ``"point"`` 
是点这个类的名字, 它有 ``x`` 和 ``y`` 两个属性。
    
collections.nametuple预先封装好了这种对象的类的定义, 免去了自己写类的麻烦, 非常
地方便。下面有两种方法可以创建nametuple类。

1. 用列表定义属性, ``verbose=True`` 表示定义类时, 同时打印实现细节: 
``Point = collections.namedtuple("Point", ["x", "y"], verbose=True)``

2. 用字符串定义属性,属性名称用逗号隔开: 
``Point = collections.namedtuple("Point", "x, y", verbose=False)``

Reference: https://docs.python.org/3.3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields
"""

from __future__ import print_function
from collections import namedtuple
import sys

def example1():
    """A basic usage example.
    """
    Point = namedtuple("Point", "x, y", verbose=True)
    p = Point(x=11, y=22)
    print(p.x, p.y) # 用属性名调用值
    
    p1 = Point(33, 44)
    print(p1) # 用人类可读的语言打印Point对象

def recipe1():
    """从nametuple所继承的类自带四个非常有用的方法:
    
    - _make(iterable): 从序列中按顺序产生对象实例, 通常比用户自己实现的要快
    - _asdict(): 返回字典的数据视图
    - _replace(**kwargs): 修改属性
    - _fields: 返回所有允许的属性
    """
    Row = namedtuple("Row", "c1, c2, c3", verbose=False)
    row = Row._make([1, 2, 3])
    print(row)

if __name__ == "__main__":
    example1()
    recipe1()
    