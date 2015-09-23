#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
binascii这个库主要提供了binary数据和ascii数据之间的各种转化。

Reference:

- binascii: https://docs.python.org/3.3/library/binascii.html
- int.from_bytes: https://docs.python.org/3/library/stdtypes.html#int.from_bytes
"""

from __future__ import print_function
import pickle
import hashlib
import binascii

def example_bytes_to_int():
    """本例提供了将任意的字符串, bytes和整数相互转换的方法。
    
    有的时候我们希望将bytes进行位操作, 进行一定的计算。比如在simhash中我们就要
    用到这个操作。这个时候就需要将任意对象转化为整数。
    """
    md5 = hashlib.md5()
    md5.update(pickle.dumps([1, 2, 3]))
    b = md5.digest()
    
    # 方法1, 使用binascii.b2a_hex
    h = binascii.b2a_hex(b)
    print(int(h, 16))
    
    # 方法2, 使用in.from_bytes(bytes, "big")
    print(int.from_bytes(b, "big"))
    
if __name__ == "__main__":
    example_bytes_to_int()