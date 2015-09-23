#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
当用户需要自定义列表类型时, 请继承collections.UserList

Reference: https://docs.python.org/3.3/library/collections.html#userlist-objects
"""

from __future__ import print_function
import sys
if sys.version_info.major == 2:
    from UserList import UserList
else:
    from collections import UserList

class MyList(UserList):
    pass

if __name__ == "__main__":
    l = [1, 2, 3]
    
    mylist = MyList([1, 2, 3])
    print(mylist)
    print(mylist.data)
    print(dir(mylist))