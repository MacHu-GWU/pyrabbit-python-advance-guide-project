#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
base64是一种将任何二进制数据编码成ASCII字符的方法。其中Python提供了urlsafe的版本,
使得编码结果中 ``-`` 会被 ``+`` 取代, ``_`` 会被 ``/`` 取代。

Reference: https://docs.python.org/3.3/library/base64.html
"""

from __future__ import print_function
import pickle
import binhex

def example():
    """一个简单的用base64对数字编码的用例。
    """
#     with open("__init__.py", "rb") as f1:
#         with open("output.txt", "wb") as f2:
#             binhex.binhex(f1, f2)
    
    
if __name__ == "__main__":    
    example()