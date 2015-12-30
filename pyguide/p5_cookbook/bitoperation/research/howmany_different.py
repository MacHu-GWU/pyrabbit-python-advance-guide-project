#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
题目: 计算两个整数的二进制形式的有多少位是不相同的
"""

from __future__ import print_function
from count_howmany_one import count_howmany_one_method2
import time

def howmany_different_method1(a, b):
    """解法1, 从最后一位开始, 一一比较两个数。
    """
    ans = 0
    if a > b:
        while a:
            a, m_a = divmod(a, 2)
            b, m_b = divmod(b, 2)
            if m_a != m_b:
                ans += 1
    else:
        while b:
            a, m_a = divmod(a, 2)
            b, m_b = divmod(b, 2)
            if m_a != m_b:
                ans += 1
    return ans

def howmany_different_method2(a, b):
    """利用位异或操作, 然后统计结果中1的个数(利用count_howmany_one中的结论)
    """
    return count_howmany_one_method2(a ^ b)

if __name__ == "__main__":
    a = 7814578243756243758918945123461784689753
    b = 2389147891375917438978971237146357816412
    
    st = time.clock()
    ans = howmany_different_method1(a, b)
    print("elapse %.6f sec" % (time.clock() - st))
    print(ans)
    
    st = time.clock()
    ans = howmany_different_method2(a, b)
    print("elapse %.6f sec" % (time.clock() - st))
    print(ans)