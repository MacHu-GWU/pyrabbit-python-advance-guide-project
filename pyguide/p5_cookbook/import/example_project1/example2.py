#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
从包中导入模块中的方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
我们知道我们可以通过下面的方式导入模块中的所有变量, 函数, 类::

    from package.module import *
    
    func1()
    func2()
    ...

但如果我们想要使得仅仅使用 ``from package import *`` 就能导入package下的所有模块中
的方法, 就像实现下面的语法:

    from package import *
    
    func1()
    func2()
    ...
    
该怎么做呢? 解决方案, 在 ``package.__init__.py`` 中加入如下代码::

    from .module import *
    
很简单吧?
"""

if __name__ == "__main__":
    from testpackage import *
    
    func1()
    func2()