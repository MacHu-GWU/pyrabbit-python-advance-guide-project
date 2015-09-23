#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LRU (least recently used) cache这种缓存能将函数最近N次被调用的输入参数和返回值
缓存起来, 每次有新的访问时, 会首先到缓存保存过的输入参数中查找, 如果找不到再真正
执行函数。

LRU缓存的典型作用就是新闻客户端, 例如缓存保存最新的20篇文章。用户每次登陆, 服务
器就不需要去读取数据库, 而可以直接把缓存中的内容推送给用户。

注: 此模块在Python3.2之后才出现

Reference: https://docs.python.org/3.3/library/functools.html#functools.lru_cache
"""

from __future__ import print_function
from functools import lru_cache
import time

def fib1(n):
    """recursive solution for fibonacci(n).
    """
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)

def fib2(n):
    """dynamic programming solution for fibonacci(n).
    """
    if n <= 2:
        return 1
    i, res = 1, 1
    for _ in range(n - 2):
        i, res = res, res + i
    return res

@lru_cache(maxsize=5)
def fib3(n):
    """use LRU cache and recursive solution for fibonacci(n).
    """
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)

if __name__ == "__main__":
    complexity = 20
    
    print("call fib once...")
    st = time.clock()
    fib1(complexity)
    print("%.6f" % (time.clock() - st))
    
    st = time.clock()
    fib2(complexity)
    print("%.6f" % (time.clock() - st))
    
    st = time.clock()
    fib3(complexity)
    print("%.6f" % (time.clock() - st))
    
    print("call fib 1 to n...")
    st = time.clock()
    [fib1(i) for i in range(1, complexity+1)]
    print("%.6f" % (time.clock() - st))
    
    st = time.clock()
    [fib2(i) for i in range(1, complexity+1)]
    print("%.6f" % (time.clock() - st))
    
    st = time.clock()
    [fib3(i) for i in range(1, complexity+1)]
    print("%.6f" % (time.clock() - st))
    
    print("call fib n many times...")
    st = time.clock()
    [fib1(complexity) for i in range(1, complexity+1)]
    print("%.6f" % (time.clock() - st))
    
    st = time.clock()
    [fib2(complexity) for i in range(1, complexity+1)]
    print("%.6f" % (time.clock() - st))
    
    st = time.clock()
    [fib3(complexity) for i in range(1, complexity+1)]
    print("%.6f" % (time.clock() - st))
