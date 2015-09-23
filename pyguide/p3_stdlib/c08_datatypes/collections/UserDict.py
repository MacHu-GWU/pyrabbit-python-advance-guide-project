#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
当用户需要自定义字典类型时, 请继承collections.UserDict

Reference: https://docs.python.org/3.3/library/collections.html#userdict-objects
"""

from __future__ import print_function
import sys
if sys.version_info.major == 2:
    from UserDict import UserDict
else:
    from collections import UserDict
    
class MyDict(UserDict):
    pass

if __name__ == "__main__":
    d = {"a": 1, "b": 2}
    
    mydict = MyDict({"a": 1, "b": 2})
    print(mydict)
    print(mydict.data)
    print(dir(mydict))