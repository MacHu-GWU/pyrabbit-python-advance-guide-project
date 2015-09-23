#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
本模块详细的剖析了Python中以**单下划线**开头的的成员名的特殊意义。

官方文档中提到了, 在Python中不存在所谓在C, Java中的私有变量(即除了从类的内部就
无法方位的变量)。官方文档可以参考: https://docs.python.org/3.3/tutorial/classes.html#private-variables

原话是这么说的: "'Private' instance variables that cannot be accessed except 
from inside an object don’t exist in Python."

在Python中, 以单下划线的开始的 ``变量``, ``函数``, ``类`` 有一个统称叫做 non-public 
part of the API. 其具体的含义是: 如果名字以单下划线开头, 那么就无法被
``from module_name import *`` 所导入。但是仍然可以被 "import module_name", 然后
通过 ``module_name._var_name`` 所访问到。请看下面的例子::

    _non_public_var = "_non_public_var" # cannot be imported by from xx import *
    public_var = "public_var"
    
    def _non_public_func(): # cannot be imported by from xx import *
        return "_non_public_func"
    
    def public_func():
        return "public_func"
    
    class _NonPublicClass(object): # cannot be imported by from xx import *
        def _non_public_method(self):
            return "_non_public_method"
    
        def public_method(self):
            return "public_method"
        
    class PublicClass(object):
        def _non_public_method(self): # can be accessed by PublicClass._non_public_method
            return "_non_public_method"
    
        def public_method(self):
            return "public_method"

在类中使用下划线开头的方法名并没有实际意义, 只能从视觉上提醒用户, 该变量/方法
尽量只从内部进行访问, 而无法强制阻止其从外部访问。

而这一特性的主要应用是: 在module中, 把不希望通过 ``from module_name import *``
所导入的对象用单下划线的命名所保护起来。例如在module中你有一个方法, 这个方法需要
用到一些常数变量, 或者另外的辅助方法。而这些在外部是用不到的。那么此时就可以使用
单下划线开头的命名空间。
"""

from __future__ import print_function

_non_public_var = "_non_public_var" # cannot be imported by from xx import *
public_var = "public_var"

def _non_public_func(): # cannot be imported by from xx import *
    return "_non_public_func"

def public_func():
    return "public_func"

class _NonPublicClass(object): # cannot be imported by from xx import *
    def _non_public_method(self):
        return "_non_public_method"

    def public_method(self):
        return "public_method"
    
class PublicClass(object):
    def _non_public_method(self): # can be accessed by PublicClass._non_public_method
        return "_non_public_method"

    def public_method(self):
        return "public_method"