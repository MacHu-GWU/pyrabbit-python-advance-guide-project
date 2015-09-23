#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
classmethod经常被拿来和staticmethod比较。他们之间相似之处是: 都可以不需要实例化
类就可以调用该方法。但是staticmethod完完全全是被当做一个函数来使用。但
classmethod需要将第一个参数作为一个类对象(注意不是实例)传入。

诚然, 我们也可以定义staticmethod中的第一个参数必须是某一个类对象。但classmethod
能从功能上更好地将其区分开。(或许还有别的目的, 笔者还不知道)
"""

from __future__ import print_function

class ClassMaker(object):
    """A class instance constructor.
    """
    @classmethod
    def make(self, cls, *args, **kwargs):
        i = cls(*args, **kwargs)
        return i
    
class MyClass(object):
    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    myclass = ClassMaker.make(MyClass, 1)
    print(myclass.value)