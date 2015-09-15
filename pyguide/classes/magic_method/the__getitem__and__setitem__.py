#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- ``__getitem__`` 实现了 x[i] 的行为
- ``__setitem__`` 实现了 x[i] = j 的行为
"""

from __future__ import print_function

class MyListClass(object):
    """A custom list class, which support set value by index, even the index
    is out of range. (automatically pad None value)
    
    **中文文档**
    
    本例实现了一个自定义的list对象。提供了在 ``x[i] = j`` 赋值时当index超出范围时, 
    自动填充None值的功能。 
    """
    def __init__(self):
        self.data = list()
        
    def append(self, value):
        self.data.append(value)
    
    def __setitem__(self, index, value):
        if isinstance(index, int) and index > -1:
            if (index + 1) <= len(self.data): # index is in range
                self.data[index] = value
            else: # index is out of range, pad None value
                for i in range(index - len(self.data)):
                    self.data.append(None)
                self.data.append(value)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        return str(self.data)

if __name__ == "__main__":
    my_list = MyListClass()
    my_list.append(0)
    print(my_list[0])
    
    my_list[1] = 1
    print(my_list)
    my_list[1] = 1.1
    print(my_list)
    my_list[5] = 5
    print(my_list)