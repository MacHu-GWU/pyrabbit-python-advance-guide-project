#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
一些参考资料: 

- logging基础文档: https://docs.python.org/3.3/library/logging.html
- Logging Levels: https://docs.python.org/3.3/library/logging.html#logging-levels
- LogRecord attributes: https://docs.python.org/3.3/library/logging.html#logrecord-attributes
- basicConfig: https://docs.python.org/3.3/library/logging.html#logging.basicConfig
- cookbook: https://docs.python.org/3.3/howto/logging-cookbook.html
"""

from pyguide.p3_stdlib.c16_generic_operation_system_services.logging.package.module import func1, func2

def example1():
    """提供了一个比较典型的用例的代码编写模式: 
    
        软件有一个主脚本作为入口, 调用了多个模块中的函数, 
        不同的函数中使用不同的 
        `logging.Logger <https://docs.python.org/3.3/library/logging.html#logging.Logger>`_
        处理日志。
        
    我们有一个模块中有两个函数 ``func1`` 和 ``func2`` 需要生成日志, 但我们希望让两个
    函数的日志有: 不同的日志等级, 写入不同的文件, 有不同的格式。
    
    ``func1`` 和 ``func2`` 函数中的代码请参考
    :mod:`pyguide.p3_stdlib.c16_generic_operation_system_services.logging.package.module`
    """
    func1()
    func2()
    
if __name__ == "__main__":
#     example1()
    pass