#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Note: super() only works for new-style classes!!!

Reference:

- http://www.cnblogs.com/lovemo1314/archive/2011/05/03/2035005.html
- https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
"""

from __future__ import print_function

class A(object):
    def __init__(self):
        self.name = "A"
        print("enter A")
        print("leave A")
        
class B(object):
    def __init__(self):
        self.name = "B"
        print("enter B")
        print("leave B")
        
def example1():
    """在下面的例子中, 如果我们要修改C的继承父类, 那么代码段中的A.__init__(self)
    也要跟着修改。这样在代码量很大的时候会带来非常多的不便和不确定因素。
    """
    class C(A):
        def __init__(self):
            print("enter C") 
            A.__init__(self)
            print("leave C")
    
#     class C(B):
#         def __init__(self):
#             print("enter C") 
#             B.__init__(self)
#             print("leave C")
            
    c = C()
    
def example2():
    """将 ``A.__init__(self)`` 换成 ``super(C, self).__init__()`` 即可解决这一问题。
    super(C, self).__init__() 的原理。
    
    先找到C的父类B, 然后将C的self对象转换为类B的self对象, 然后再执行
    self.__init__(), 期间在B.__init__()发生的事, 也会对C产生效果。
    """
    class C(B):
        def __init__(self):
            self.name = "C"
            print("enter C")
            super(C, self).__init__()
            print("leave C")
            
    c = C()
    print(c.name)

if __name__ == "__main__":
    example1()    
    example2()