#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
本模块详细的剖析了Python中以**双下划线**开头的的成员名的特殊意义。

请看下面的代码, 判断最终的输出应该是什么::

    from __future__ import print_function
    
    class A(object):
        def __init__(self):
            self.__private()
            self.public()
               
        def __private(self):
            print("A.__private()")
               
        def public(self):
            print("A.public()")
              
    class B(A):
        def __private(self):
            print("B.__private()")
              
        def public(self):
            print("B.public()")
              
    b = B() # guess what is the output
    b._B__private() # guess what is the output
    b.public() # guess what is the output

最终的结果实际是::

    A.__private()
    B.public()
    B.__private()
    B.public()

类B从A继承了 ``__init__`` 方法, 但是覆盖了 ``__private`` 和 ``public`` 方法。但为什么
最终只有 ``public`` 被成功覆盖了, 而 ``__private`` 却没有呢? 这是因为以双下划线开头
的变量或者方法, 在Python中称作class-private members。其特性是, 在被继承的子类中
原有的成员会成为父类的私有成员, 无法在子类中被覆盖。那么也许你会问了, 那么方法
``B.__private`` 难道是被吞掉了吗? 这就要谈到Python中的私有变量轧压(Private name 
mangling)的机制。

为了同时保留 ``A.__private`` 和 ``B.__private``, 编译器在生成代码前, 会对私有成员
进行变量轧压, 已解决名称冲突的问题。具体的做法是在前面加上类名, 最后再加上一个
下划线。例如::

    from __future__ import print_function
    
    class A(object):
        def __init__(self):
            self.__private()
            self.public()
              
        def _A__private(self): # Private name mangling
            print("A.__private()")
              
        def public(self):
            print("A.public()")
              
    class B(A):
        def _B__private(self): # Private name mangling
            print("B.__private()")
              
        def public(self):
            print("B.public()")
              
这个机制达到了以下几个目的:

1. Python中没有真正意义上的私有成员, 所以其实 ``A.__private`` 方法还是能通过
  ``A._A__private`` 从外部访问的。这样以另一种形式避免了直接从外部进行访问。
2. 解决了命名空间冲突的问题。使得父类和子类中同名的私有成员可以共存。

有两点需要注意的是:

1. 因为轧压会使标识符变长，当超过255的时候，Python会切断，要注意因此引起的命名
  冲突。
2. 当类名全部以下划线命名的时候，Python就不再执行轧压。如::

    from __future__ import print_function
    
    class ____(object):
        def __init__(self):
            self.__method()
            
        def __method(self):
            print("____.__method()")

下面我们来看一个 `官方的例子 <https://docs.python.org/3.3/tutorial/classes.html#private-variables>`_
判断最终的输出结果应该是什么::

    from __future__ import print_function
    
    class Mapping:
        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)
    
        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)
    
        __update = update   # private copy of original update() method
    
    class MappingSubclass(Mapping):
    
        def update(self, keys, values):
            # provides new signature for update()
            # but does not break __init__()
            for item in zip(keys, values):
                self.items_list.append(item)
                
    m = MappingSubclass([1, 2, 3])
    m.update("abc", [1, 2, 3])
    print(m.items_list) # guess what is the output

最终输出的结果是::

    [1, 2, 3, ('a', 1), ('b', 2), ('c', 3)]

在 ``m = MappingSubclass([1, 2, 3])`` 初始化时, 调用的是 ``Mapping.__init__`` 中的
``Mapping.update`` 方法。而在 ``m.update("abc", [1, 2, 3])`` 中, 调用的是
``MappingSubclass.update`` 方法。这样就保证了 ``Mapping.__init__`` 中的
``Mapping.update`` 方法依然有效。

参考文章: http://blog.csdn.net/gudesheng/article/details/2169038
"""

from __future__ import print_function

if __name__ == "__main__":
    # a simple example
    class A(object):
        def __init__(self):
            self.__private()
            self.public()
               
        def __private(self):
            print("A.__private()")
               
        def public(self):
            print("A.public()")
              
    class B(A):
        def __private(self):
            print("B.__private()")
              
        def public(self):
            print("B.public()")
              
    b = B() # guess what is the output
    b._B__private() # guess what is the output
    b.public() # guess what is the output
    
    # an application example
    class Mapping:
        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)
    
        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)
    
        __update = update   # private copy of original update() method
    
    class MappingSubclass(Mapping):
    
        def update(self, keys, values):
            # provides new signature for update()
            # but does not break __init__()
            for item in zip(keys, values):
                self.items_list.append(item)
                
    m = MappingSubclass([1, 2, 3])
    m.update("abc", [1, 2, 3])
    print(m.items_list) # guess what is the output