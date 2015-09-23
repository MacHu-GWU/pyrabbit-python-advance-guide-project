#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在默认情况下, 所有的类都会有一个特殊属性: ``__dict__`` 用于以字典的形式保存类的
所有属性的: {属性名: 值} 的数据。方便了我们可以很容易的获得类的数据的字典形式。
但这么做相当于在内存中为类开辟了一段内存保存其值, 还需要为 ``__dict__`` 再开辟一个
内存, 在字典中保存其值。请注意, 字典的实现是哈希表, 而哈希表的储存效率只有50%。
那么在我们需要创建成千上万个类实例的时候, 就会浪费大量的内存空间。

这一问题的解决方法请参考 :mod:`__slots__ <pyguide.classes.magic_attribute.the__slots__>`
"""

from __future__ import print_function

class MyClass(object):
    """An example.
    """
    pass
    
if __name__ == "__main__":
    myclass = MyClass()
    myclass.a = 1
    myclass.b = 2
    myclass.c = 3
    print(myclass.__dict__)