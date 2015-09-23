一些术语:

- Package: 包
- Module: 模块
- __init__.py - 初始化模块

在Python的import系统中, **包** 是含有 ``__init__.py`` 文件的文件夹。 **模块** 是 ``*.py** 文件的脚本, 当该脚本被 ``import module_name`` 时, ``module_name.py`` 文件就会被以 ``import`` 的方式被执行一次, 也就是说不是以主脚本的形式被执行, 所以 ``if __name__ == "__main__":`` 下面的代码都不会被执行。 而特殊脚本 ``__init__.py`` 是用于在 ``import package_name`` 时, 被执行的文件。

在Python中包也可以理解为一种特殊的模块。

