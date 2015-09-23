#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
base64是一种将任何二进制数据编码成ASCII字符的方法。其中Python提供了urlsafe的版本,
使得编码结果中 ``-`` 会被 ``+`` 取代, ``_`` 会被 ``/`` 取代。

Reference: https://docs.python.org/3.3/library/base64.html
"""

from __future__ import print_function
import pickle
import base64

def example():
    """一个简单的用base64对数字编码的用例。
    """
    b = pickle.dumps([1, 2, 3])
    
    print(base64.b16encode(b))
    print(base64.b32encode(b))
    print(base64.b64encode(b))
    
    print(base64.standard_b64encode(b))
    print(base64.urlsafe_b64encode(b))
    
if __name__ == "__main__":    
    example()
        