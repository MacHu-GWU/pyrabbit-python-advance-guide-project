#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
total_ordering的功能是: 只要用户实现了 __lt__, __le__, __gt__, __ge__ 中的一个和
__eq__, 就可以代替用户直线剩余的4个比较方法。
"""

from __future__ import print_function
from functools import total_ordering

@total_ordering
class Student:
    """an example of using ``total_ordering``
    """
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))