#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
堆是一种特殊的二叉树, 其每个父节点的值都小于等于其子节点的值。如果从上往下, 从
左往右遍历整个堆, 结果是有序的。插入复杂度在 O(log(n)), 用于排序的复杂度在
O(nlog(n))。

堆的应用范围有:

1. 有序列表数据结构。
2. 堆排序。
3. 用来求Top-K问题。

Reference: https://docs.python.org/3.3/library/heapq.html
"""

from __future__ import print_function, unicode_literals
from heapq import *
import random
import time

def performance_ordered_list():
    """一个堆在用于实现有序列表时的例子。
    """
    # initialize test data
    complexity = 1000
    array = list(range(complexity))
    random.shuffle(array)

    b = list()
    st = time.clock()
    for i in array:
        heappush(b, i)
    print("heap takes %.6f sec." % (time.clock() - st,))
    
    a = list()
    st = time.clock()
    for i in array:
        a.append(i)
        a.sort()
    print("sort takes %.6f sec." % (time.clock() - st,))

def performance_sort():
    """一个堆在用于实现排序时的例子。
    """
    # initialize test data
    complexity = 1000

    array = list(range(complexity))
    random.shuffle(array)
    
    st = time.clock()
    b = list()
    for i in array:
        heappush(b, i)
    print("heap sort takes %.6f sec." % (time.clock() - st,))
    
    array = list(range(complexity))
    random.shuffle(array)
    
    st = time.clock()
    array.sort()
    print("list sort takes %.6f sec." % (time.clock() - st,))
    
def performance_topK():
    """测试堆在求top K问题中的性能。
    """
    # initialize test data
    complexity = 1000
    array = list(range(complexity))
    random.shuffle(array)
    
    st = time.clock()
    nlargest(3, array) # 999, 998, 997
    print("heap topk takes %.6f sec." % (time.clock() - st,))
    
    st = time.clock()
    array.sort()
    array[:3]
    print("sort takes %.6f sec." % (time.clock() - st,))
    
if __name__ == "__main__":
#     performance_ordered_list()
    performance_sort()
#     performance_topK()