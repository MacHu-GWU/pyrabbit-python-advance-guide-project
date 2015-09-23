##encoding=UTF8

from mother_package.children1.module1 import * # 虽然经过了children1, 但是并没有执行children1.__init__.py
print(give1())
print(give2()) # <=== 还没有被导入, 所以会抛出异常