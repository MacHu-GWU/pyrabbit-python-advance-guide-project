#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
题目: 给定一个正整数, 判断该整数从右数起第nth位是否为1
本脚本python2, 3兼容
"""

from __future__ import print_function, unicode_literals
import time

def get_the_last_k_bit_is_one_method1(x, nth):
    for _ in range(nth):
        x, m = divmod(x, 2)
    return bool(m)

def get_the_last_k_bit_is_one_method2(x, nth):
    return bool(x & 1 << (nth -1))

if __name__ == "__main__":
    x = 815637813459082348957132894617849012337588917394
    nth = 60
    
    st = time.clock()
    ans = get_the_last_k_bit_is_one_method1(x, nth)
    print("elapse %.6f sec" % (time.clock() - st))
    print(ans)
    
    st = time.clock()
    ans = get_the_last_k_bit_is_one_method2(x, nth)
    print("elapse %.6f sec" % (time.clock() - st))
    print(ans)