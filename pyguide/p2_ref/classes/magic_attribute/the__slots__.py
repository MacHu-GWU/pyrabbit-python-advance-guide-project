#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``__slots__`` 是在 new style class 中出现的新概念。为此为了保障代码对Python2/3的
兼容性, 所有的类都要继承自 ``object``。在默认情况下, 所有的类都会有一个特殊属性:
``__dict__`` 用于以字典的形式保存类的所有属性的: {属性名: 值} 的数据。这么做相当于
在内存中为类开辟了一段内存保存其值, 还需要为 ``__dict__`` 再开辟一个内存, 在字典
中保存其值。请注意, 字典的实现是哈希表, 而哈希表的储存效率只有50%。那么在我们
需要创建成千上万个类实例的时候, 就会浪费大量的内存空间。

而一旦我们定义了 ``__slots__``, 那么Python就不会为类创建 ``__dict__`` 属性, 节约了
内存空间。并且, 只有在 ``__slots__`` 中被定义了的属性名被允许赋值。相当于限制了
可用的属性名。这样能够更佳地保持类属性不会被错误地修改。
"""

from __future__ import print_function

class MyClass(object):
    """A class with pre-defined available attributes.
    """
    __slots__ = ["a", "b", "c"]
    
    def to_dict(self):
        """虽然如果定义了 ``__slots__`` 就不会有 ``__dict__`` 这个属性。但是我们仍然
        可以自定义一个方法将对象中的数据字典化。
        """
        d = dict()
        for key in self.__slots__:
            try:
                d[key] = self.__getattribute__(key)
            except:
                pass
        return d

if __name__ == "__main__":
    myclass = MyClass()
    myclass.a = 1 # allow
    myclass.b = 2 # allow
    myclass.c = 3 # allow
    try:
        myclass.d = 4 # not allow
    except AttributeError as e:
        print(e)
    try:
        print(myclass.__dict__) # there's no __dict
    except AttributeError as e:
        print(e)
    print(myclass.to_dict())