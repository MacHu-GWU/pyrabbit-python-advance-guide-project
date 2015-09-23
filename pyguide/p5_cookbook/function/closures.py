#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
闭包的概念:

函数内部定义的变量, 在函数外部是不可见的。而闭包的作用就是, 从函数的外部, 对
函数内部的变量进行读取。我们来看 :func:`example1` 中的例子::

在 :func:`example1` 中, 我们定义了outer函数, 但我们无法通过像类一样, 通过outer.x来
访问x中的值。

在 :func:`example2` 中, x是一个outer函数内部的global变量, 被inner函数所引用。如果
我们让outer()返回的是一个inner函数, 那么x就作被跟inner所绑定, 就能够通过inner
访问到x中的值了。这一过程就叫做闭包。

那么闭包有些什么应用呢? 闭包在函数化编程中, 一个很大的作用就是简化编程模式。
比如说我们建立了一个数学模型, 其中接受x1, x2, x3三个变量, 同时也有a1, a2, a3三个
参数。而这个参数不是固定不变的。那么我们有以下几种方式写这个函数:

方法1:

为每一种a1, a2, a3的组合创建一个函数。(最差)

方法2:

将a1, a2, a3作为输入参数传给函数。(人类本能的想法)

方法3:

利用闭包, 用一个函数生成这个模型函数, 并将a1, a2, a3将其绑定。当我们需要改变模型
的参数, 只要另外生成一个新的模型函数即可。(闭包) 这也是 :func:`example3` 中的例子。

方法4:

使用偏函数partial, 请参考
:mod:`partial <pyguide.stdlib.c10_functional_programming.functools.partial>` 一节中的内容。
毫无疑问, 这是最好的解决方法。
"""

from __future__ import print_function

def example1():
    """A normal function.
    """
    def outer():
        x = 1
        print(x)
        
    outer()

def example2():
    """Closure function.
    """
    def outer(x):
        def inner():
            print(x)
        return inner
    
    f1 = outer(1)
    print(f1.__closure__)
    f1()
    f2 = outer(2)
    print(f2.__closure__)
    f2()

def example3():
    """An application of closure.
    """
    def create_model(a1, a2, a3):
        def model(x1, x2, x3):
            return a1 * x1 + a2 * x2 + a3 * x3
        return model
    
    m = create_model(1, 2, 3)
    print(m(1, 2, 3))
            
    def model(x1, x2, x3, param1, param2, param3):    
        return param1 * x1 + param2 * x2 + param3 * x3
    
    print(model(1, 2, 3, 1, 2, 3))

if __name__ == "__main__":
    example1()
    example2()
    example3()
    pass