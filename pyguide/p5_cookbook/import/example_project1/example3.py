#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
模块之间互相调用
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

例如我们想要在 ``module1`` 中调用 ``module2.func2``, 那么我们只需要在 ``module1.py`` 
中加入如下代码::

    from module2 import func2
    
    # do something with func2

注意!! 两个模块不可以同时你调用我, 我调用你。因为这样会在初始化中, 造成无限死
循环。
"""
