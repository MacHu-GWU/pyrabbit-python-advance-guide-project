#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``__name__`` 变量对于 package, module, function, class, method 都是作为一个默认
属性, 储存着它们的全名(包含父子关系的全名)

- 对于package: 是package name
- 对于module: 是module name
- 对于function: 是function name
- 对于class: 是class name
- 对于method: 是method name

对于module脚本而言, 变量 ``__name__`` 的值在脚本内是: ``__main__``, 而在脚本外被
import时是 ``module``。这一特性常常用来使得一些代码只有在本脚本作为主脚本运行时
才会被执行, 而在被import时不会被执行。具体方法如下::

    if __name__ == "__main__":
        # put your code here
        pass

该特性常用来作为单元测试。也就是将本模块中的代码的单元测试部分放在if语句之下,
保证每个模块作为主脚本执行时是执行单元测试, 而被导入时是作为模块被导入。
"""

from __future__ import print_function
import string

def func():
    pass

class MyClass(object):
    def method(self):
        pass

if __name__ == "__main__":
    print("func __name__ = '%s'" % func.__name__)
    print("MyClass __name__ = '%s'" % MyClass.__name__)
    print("MyClass.method __name__ = '%s'" % MyClass.method.__name__)
    print("This script __name__ = '%s'" % __name__)
    print("module `string` __name__ attribute = '%s'", string.__name__)
