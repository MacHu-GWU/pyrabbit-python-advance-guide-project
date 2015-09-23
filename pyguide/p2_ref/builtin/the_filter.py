#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
filter关键字类似于map关键字, 将一个只接受一个参数并只返回一个布尔值的函数, 对
一个数组中的所有元素进行求真值, 返回所有结果是真的元素。
"""

from __future__ import print_function
import random
import time
import math

def main():
    """
    
    **中文文档**
    
    下面这个例子测试了普通方法和使用filter方法的性能, 总体速度并没有差别。
    
    结论: **filter实际只是一个语法糖结构, 并不能带来性能上的提升。**
    """
    array = list(range(1000**2, 1000**2 + 10000))
    
    def is_odd(number):
        return number % 2
    
    def is_prime(number):
        if number < 1:
            raise Exception("number has to be greater and equal than 1.")
        elif number <= 3:
            return 1
        
        sqrt = math.floor(math.sqrt(number))
        
        for i in range(2, sqrt+1):
            if (number % i == 0):
                return 0
        return 1
    
    def test_is_odd():
        print("test is_odd")
        st = time.clock()
        for i in array:
            if is_odd(i):
                i
        print("for loop, if: %.6f sec" % (time.clock() - st))
        
        st = time.clock()
        for i in filter(is_odd, array):
            i
        print("use filter: %.6f sec" % (time.clock() - st))

    test_is_odd()

    def test_is_prime():
        print("test is_prime")
        st = time.clock()
        for i in array:
            if is_prime(i):
                i
        print("for loop, if: %.6f sec" % (time.clock() - st))
        
        st = time.clock()
        for i in filter(is_prime, array):
            i
        print("use filter: %.6f sec" % (time.clock() - st))

    test_is_prime()
    
if __name__ == "__main__":
    main()