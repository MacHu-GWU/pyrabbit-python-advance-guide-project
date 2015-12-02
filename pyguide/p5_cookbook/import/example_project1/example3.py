#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
模块之间互相调用
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

同级模块调用:

例如我们想要在 ``testpackage.module1`` 中调用 ``testpackage.module2.func2``, 那么
我们只需要在 ``testpackage.module1.py`` 中加入如下代码::

    from .module2 import func2
    
    # do something with func2
    

下级模块调用:

例如我们想要在 ``testpackage.module1`` 中调用 ``testpackage.subpackage1.module11.func11``
我们只需要在 ``testpackage.module1.py`` 中加入如下代码::

    from .subpackage1.module11 import func11
    
    # do something with func11


上级模块调用: 慎用!

例如我们想要在 ``testpackage.subpackage1.module11`` 中调用 ``testpackage.subpackage2.module21.func21``
我们只需要在 ``testpackage.subpackage1.module11.py`` 中加入如下代码::

    from ..subpackage2.module21 import func21
    
    # do something with func21


注意!!

1. 两个模块不可以同时你调用我, 我调用你。因为这样会在初始化中, 造成无限死循环。
2. 模块内部之间的调用, 最好只调用平级和下级模块中的内容, 即: 子包中的模块尽量
不要调用母包中的模块。

"""

from testpackage.subpackage1.module11 import func1
print(func1)