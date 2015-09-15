#!/usr/bin/env python
# -*- coding: utf-8 -*-

from startwith_single_underscore import *
 
# regular name can be imported
print(public_var)
print(public_func)
print(PublicClass)
print(PublicClass._non_public_method) # can be accessed by classname.methodname
print(PublicClass.public_method)
 
# name start with single underscore cannot be imported
try:
    print(_non_public_var)
except Exception as e:
    print(e)
try:
    print(_non_public_func)
except Exception as e:
    print(e)
try:
    print(_NonPublicClass)
except Exception as e:
    print(e)
try:
    print(_NonPublicClass._non_public_method)
except Exception as e:
    print(e)
try:
    print(_NonPublicClass.public_method)
except Exception as e:
    print(e)
 
# name start with single underscore can be accessed by parent_object.name
# for example: module_name.variable_name, module_name.function_name
# module_name.class_name
import startwith_single_underscore
 
print(startwith_single_underscore._non_public_var)
print(startwith_single_underscore._non_public_func)
print(startwith_single_underscore._NonPublicClass)
print(startwith_single_underscore._NonPublicClass._non_public_method)