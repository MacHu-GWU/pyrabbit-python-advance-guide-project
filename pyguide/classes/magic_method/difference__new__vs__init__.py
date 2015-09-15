#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Cite from: http://stackoverflow.com/questions/4859129/python-and-python-c-api-new-versus-init

The difference mainly arises with mutable vs immutable types.

__new__ accepts a type as the first argument, and (usually) returns a new 
instance of that type. Thus it is suitable for use with both mutable and 
immutable types.

__init__ accepts an instance as the first argument and modifies the attributes 
of that instance. This is inappropriate for an immutable type, as it would allow 
them to be modified after creation by calling obj.__init__(*args).

Compare the behaviour of tuple and list::

    >>> x = (1, 2)
    >>> x
    (1, 2)
    >>> x.__init__([3, 4])
    >>> x # tuple.__init__ does nothing
    (1, 2)
    >>> y = [1, 2]
    >>> y
    [1, 2]
    >>> y.__init__([3, 4])
    >>> y # list.__init__ reinitialises the object
    [3, 4]
    
As to why they're separate (aside from simple historical reasons): __new__ 
methods require a bunch of boilerplate to get right (the initial object 
creation, and then remembering to return the object at the end). __init__ 
methods, by contrast, are dead simple, since you just set whatever attributes 
you need to set.

Aside from __init__ methods being easier to write, and the mutable vs immutable 
distinction noted above, the separation can also be exploited to make calling 
the parent class __init__ in subclasses optional by setting up any absolutely 
required instance invariants in __new__. This is generally a dubious practice 
though - it's usually clearer to just call the parent class __init__ methods 
as necessary.

**中文文档**

- __new__: 创建对象时调用, 返回当前对象的一个实例, 相当于java里面的构造器差不多。

- __init__: 创建完对象后调用, 对当前对象的实例的一些初始化, 无返回值。
"""

from __future__ import print_function

# Compare the behaviour of tuple and list:

x = (1, 2)
print(x)

x.__init__([3, 4]) # tuple.__init__ does nothing
print(x)

y = [1, 2]
print(y)

y.__init__([3, 4]) # list.__init__ reinitialises the object
print(y) 