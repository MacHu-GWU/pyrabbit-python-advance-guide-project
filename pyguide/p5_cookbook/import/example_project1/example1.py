#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
如何导入模块中的方法?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

方法1::

    import package.module
    
    package.module.func()
    
方法2::

    import package.module as module
    
    module.func()
    
方法3::

    from package.module import func
    
    funct()
"""

if __name__ == "__main__":
    import testpackage.module1
    testpackage.module1.func1()
    
    import testpackage.module1 as module1
    module1.func1()
    
    from testpackage.module2 import func2
    func2()