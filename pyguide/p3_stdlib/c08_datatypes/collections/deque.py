#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
双向环装链表deque可以理解为一个:

1. 支持头尾插入, 删除操作的链表
2. 支持循环位移的环形链表

而在初始化的时候, 语句是: `d = deque(iterable_object, max)`。d是一个大小为 ``max`` 
的双头FIFO，然后将 ``iterable_object`` 中的值填充到FIFO中。

Reference: https://docs.python.org/3.3/library/collections.html#deque-objects
"""

from __future__ import print_function
from collections import deque
import itertools
import sys

def demo_deque1():
    """deque 的初始化,
    """
    l = [1,2,3]
    d = deque([1,2,3])
    print("print d = %s" % d)
    print("原始列表占用内存大小为: %s" % sys.getsizeof(l)) ## 普通列表占用空间小
    print("高级列表占用内存大小为: %s" % sys.getsizeof(d)) ## 高级列表占用空间大，插入删除速度快
    d1 = deque([1,2,3,4], 3) ## 像一个大小为3的fifo一样，按照顺序填充deque
    print(d1)
    d1.append(4)
    print(d1) # left append
    d1.appendleft(5)
    print(d1)

def demo_deque2(): ## [注意]请每次解除注销掉一个方法的代码进行演示
    """deque方法演示,
    """
    
    """a1 从后面插入"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    d.append(4) # append
    print("之后是%s" % d)
    
    """a2 从前面插入"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    d.appendleft(4) # appendleft
    print("之后是%s" % d)
    
    """b1 从后面取出"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    print(d.pop()) # pop
    print("之后是%s" % d)
    
    """b2 从前面取出"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    print(d.popleft()) # popleft
    print("之后是%s" % d)
    
    """c1 从后面批量插入"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    print(d.extend([4,5])) # extend
    print("之后是%s" % d)
    
    """c2 从前面批量插入"""
    d = deque([1,2,3])
    print("之前是%s" % d)
    print(d.extendleft([4,5])) # extendleft
    print("之后是%s" % d)
    
    """d 全列表循环向右边移 """
    d = deque([1,2,3])
    print("之前是%s" % d)
    d.rotate(1)
    print("之后是%s" % d)

def recipe_deque1():
    """利用deque实现 求平滑平均值函数。
    
    reference: https://docs.python.org/3.3/library/collections.html#deque-recipes
    """
    def moving_average(iterable, n=3):
        # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
        # http://en.wikipedia.org/wiki/Moving_average
        it = iter(iterable)
        d = deque(itertools.islice(it, n-1))
        d.appendleft(0)
        s = sum(d)
        for elem in it:
            s += elem - d.popleft()
            d.append(elem)
            yield s / n
    
    for i in moving_average([40, 30, 50, 46, 39, 44], 3):
        print(i)
        
def recipe_deque2():
    """利用deque实现 定长滑窗函数。
    """
    def slide_window(iterable, size):
        fifo = deque(maxlen=size)
        for i in iterable:
            fifo.append(i)
            if len(fifo) == size:
                yield fifo
                
    array = [1,2,3,4,5,6,7,8,9,10]
    for window in slide_window(array, 3):
        print(window)

if __name__ == "__main__":
    demo_deque1()
    demo_deque2()
    recipe_deque1()
    recipe_deque2()