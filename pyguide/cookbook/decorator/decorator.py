#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
"""

def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func
 
@deco
def myfunc():
    print(" myfunc() called.")
    
myfunc()