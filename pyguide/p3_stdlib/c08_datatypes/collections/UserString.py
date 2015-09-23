#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
当用户需要自定义字符串类型时, 请继承collections.UserString

Reference: https://docs.python.org/3.3/library/collections.html#userstring-objects
"""

from __future__ import print_function
import sys
if sys.version_info.major == 2:
    from UserString import UserString
else:
    from collections import UserString

class MyString(UserString):
    pass

if __name__ == "__main__":
    s = "Hello World"
    
    mystring = MyString("Hello World")
    print(mystring)
    print(mystring.data)
    print(dir(mystring))