#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Difference between shallow copy (copy.copy) and deepcopy (copy.deepcopy).

Reference: http://blog.csdn.net/lisonglisonglisong/article/details/38573269
"""

from __future__ import print_function, unicode_literals
import copy

def example():
    """一个关于shallow copy (copy.copy)和deep copy (copy.deepcopy)的区别的例子。
    """
    # since shallow copy only copy object but not its members. In this case, the
    # members are also dict, which is mutable. That's why d["a"]["a1"] is also
    # deleted when you delete d1["a"]["a1"]
    d = {"a": {"a1": 11, "a2": 12}, "b": {"b1": 21, "b2": 22}}
    d1 = copy.copy(d)
    del d1["a"]["a1"]
    print(d) 
    
    # but deepcopy not
    d = {"a": {"a1": 11, "a2": 12}, "b": {"b1": 21, "b2": 22}}
    d1 = copy.deepcopy(d)
    del d1["a"]["a1"]
    print(d)
    
if __name__ == "__main__":
    example()
