#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
defaultdict在初始化时候, 接受一个default_factory对象(请注意, 是对象而不是实例)
作为其给字典的key赋值时, 的初始值。请看下面例子::

    # 在对key对应的值进行访问时, 如果没有找到, 则会初始化一个list()
    d = defaultdict(list) 
    
    d["a"]
    print(d) # {"a": []}
    
Reference: https://docs.python.org/3.3/library/collections.html#defaultdict-objects
"""

from __future__ import print_function
from collections import defaultdict
import random
import time

def example1():
    """本例展示了如何使用一个空列表作为字典每个key的初始值。
    """
    s = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)

    print(list(d.items()))

def example2():
    """将defaultdict作为一个频率计数器使用。
    
    本例中的代码相当于使用了dict中setdefault的技巧, 但defaultdict更快。
    
        d = {}
        for k, v in s:
            d.setdefault(k, []).append(v)
        
        list(d.items())
    """
    s = "mississippi"
    d = defaultdict(int)
    for k in s:
        d[k] += 1
    
    print(list(d.items()))

def example3():
    """default_factory初始化之后会生成一个常量(在初始化时, default_factory不接受
    任何变量)。那我们就需要一个类, 使得它初始化的结果是一个常量。那如果我们难道
    要为所有的常量都要创造一个类或者函数吗? 不需要。请仔细阅读下面的代码...
    
    解说: constant_factory这个函数将常量封装在一个匿名函数lambda中返回, 所以在
    ``d = defaultdict(constant_factory("<missing>"))`` 中, 
    ``constant_factory("<missing>")`` 返回的是一个匿名函数, 这个函数的调用结果就是
    返回我们定义的常数 "<missing>"
    """
    def constant_factory(value):
        return lambda: value
    
    d = defaultdict(constant_factory("<missing>"))
    d.update(name="John", action="ran")
    print("%(name)s %(action)s to %(object)s" % d)

def defaultdict_as_counter_performance_test():
    """比较用defaultdict做频率统计和用普通字典做频率统计的时间性能。
    
    结论: defaultdict更快。
    """
    data = [random.randint(1, 1000) for i in range(1000000)]

    st = time.clock()
    d1 = defaultdict(int)
    for k in data:
        d1[k] += 1
    print(time.clock() - st)

    st = time.clock()
    d2 = dict()
    for k in data:
        try:
            d2[k] += 1
        except:
            d2[k] = 1
    print(time.clock() - st)

if __name__ == "__main__":
    example1()
    example2()
    example3()
    defaultdict_as_counter_performance_test()