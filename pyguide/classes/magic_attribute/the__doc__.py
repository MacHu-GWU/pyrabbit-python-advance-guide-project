#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``__doc__`` 变量中储存的是该对象的文档字符串。例如: package, module, function,
class, method 都有其对应的文档字符串。

- 对于package: ``package.__init__`` 文件的docstr就是它的 ``package.__doc__``
- 对于module: 在脚本最前面出现的docstr就是它的 ``module.__doc__``
- 对于function, class, method, 在定义后出现的字符串就是它们的 ``__doc__``

(下面的文字是作为docstr本身的存在, 起到例子的作用)

this is module doc
"""

def func():
    """this is func doc
    """
    
class MyClass():
    """this is class doc
    """
    def method(self):
        """this is method doc
        """

if __name__ == "__main__":
    pass