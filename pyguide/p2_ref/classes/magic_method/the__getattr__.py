#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

class Form(object):
    """一个表格的抽象类。
    """
    def __init__(self, name):
        self.name = name # 表名
        self.info = dict() # 表单数据
        
    def __str__(self):
        return str(self.info)
    
    def __getattr__(self, attr):
        if attr in self.info: # 定义了属性存在的情况
            return self.info[attr]
        else: # 定义了属性不存在的情况, 返回None
            return None

if __name__ == "__main__":
    def example1():
        print("{:=^100}".format("example1"))
        
        f = Form("I-20")
        f.info = {"fullname": "Mac Donald",
                  "name": "Mac", # name和固有属性重名
                  "age" : 25,
                  "gender" : "male"}
    
        print(f.name) # I-20
        print(f.fullname) # Mac
        print(f.height) # 未定义, 根据 __getattr__ 的定义, 返回None
        
        # 问: 如果 __getattr__(attr) 的属性名称是类中自带的属性名, 那么是直接
        # 返回 Form.attr 的值呢还是返回 Form.__getattr__(attr) 的值呢? 
        # 答: 会调用默认的属性。因为系统会优先在属性__dir__中找, 如果找不到, 
        # 再去调用__getattr__
        print(f.name)

    example1()
