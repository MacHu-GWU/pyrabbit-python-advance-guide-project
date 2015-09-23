#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
logging简介
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在logging模块中, 产生日志的类是 
`logging.Logger <https://docs.python.org/3.3/library/logging.html#logger-objects>`_。
而logging模块本身提供了跟 ``logging.Logger`` 一摸一样的API接口, 默认调用了一个
root logger (name = "")。为了在不同地方使用不同的日志行为, 我们一般不用logging,
而使用 ``logging.Logger``.

初始化 ``logging.Logger`` 的方法有两种:

1. ``logging.Logger(name)`` 
2. ``logging.getLogger(name)``

这个 ``name`` 参数, 可以使用函数名 ``func.__name__``, 方法名 ``class.method.__name__``, 
类名 ``class.__name__`` 或是模块名 ``__name__``。这样在日志中我们就可以追踪到到底是
在哪一个函数中出了问题。


logger行为的配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

下面我们来谈谈logger行为的配置。我们所关心的行为主要有这么几个:

1. 写入到哪个文件? 写入的方式是覆盖还是在后面拼接?
2. 日志信息的格式? 其中日期时间的格式是?
3. 对于各严重等级的日志如何处理?

而为了达到这一目的, 对logger行为的配置有两种方法:

1. 如果你要使用root logger, 那么可以通过调用
`logging.basicConfig <https://docs.python.org/3.3/library/logging.html#logging.basicConfig>`_
方法, 使用初始化参数对我们所关心的行为进行定义。

2. 调用 ``logging.Logger`` 中的方法, 添加 ``Handler``。具体方法可以参考本例中的代码
和官方文档。


什么是level?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

我们有下面五种方法可以用来输出日志(从最不严重到最严重排列):

- logger.debug(msg)
- logger.info(msg)
- logger.warning(msg)
- logger.error(msg)
- logger.critical(msg)

logging的规则是: 如果我们定义 ``logger.setlevel(logging.info)``, 那么只有 ``info`` 
以上包括 ``info`` 的日志会被记录。
"""

import logging

logger1 = logging.Logger("func1") # this is how we create logger in modules
logger1.setLevel(logging.DEBUG)
fh = logging.FileHandler("func1.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger1.addHandler(fh)

logger2 = logging.Logger("func2") # this is how we create logger in modules
logger2.setLevel(logging.DEBUG)
fh = logging.FileHandler("func2.log")
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger2.addHandler(fh)

def func1():
    """Function1.
    """
    try:
        a == 1
    except Exception as e:
        logger1.warning(e)

def func2():
    """Function2.
    """
    try:
        b == 1
    except Exception as e:
        logger2.warning(e)

if __name__ == "__main__":
    func1()
    func2()