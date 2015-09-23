#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reference: https://docs.python.org/3.3/library/collections.html#collections.OrderedDict
"""

from __future__ import print_function
from collections import OrderedDict
import random
import sys

def maintain_the_order():
    """ordered dict iterate items by the order the key originally inserted
    """
    d = dict()
    d["A"] = 3
    d["B"] = 2
    d["C"] = 1
    od = OrderedDict()
    od["A"] = 3
    od["B"] = 2
    od["C"] = 1
    
    print("{:=^100}".format("key order in regular dict is random"))
    for k in d:
        print(k)
    
    print("{:=^100}".format("key order in ordered dict "
                            "is the order key been inserted"))
    for k in od:
        print(k)

def memory_efficiency():
    """比较 ``dict`` 和 ``OrderedDict`` 的内存开销。
    
    结论: 在Python2中, 使用 ``sys.getsizeof`` 得到的开销大小是一样的。但是这是因为
    ``sys.getsizeof`` 的实现机制导致的。实际的内存开销是一定会大于普通的 ``dict``.
    这一点在Python3中得以被正确地显示。
    """
    d1 = {random.randint(1, 1000): random.randint(1, 1000) for i in range(1000)}
    od1 = OrderedDict()
    for k, v in d1.items():
        od1[k] = v
    print("dict in memroy: %s" % sys.getsizeof(d1))
    print("OrderedDict in memroy: %s" % sys.getsizeof(od1))

if __name__ == "__main__":
    maintain_the_order()
    memory_efficiency()