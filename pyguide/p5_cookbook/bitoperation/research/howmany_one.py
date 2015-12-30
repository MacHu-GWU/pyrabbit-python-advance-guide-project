#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
题目: 给定一个正整数, 判断该整数的二进制形式有多少个1。
本脚本python2, 3兼容
"""

from __future__ import print_function, unicode_literals
import time

def howmany_one_method1(x):
	"""解法1, 对每一位二进制进行遍历, 如果是1就将计数器+1。复杂度等于x的总位数, 且恒定。
	"""
	ans = 0
	while x:
		x, m = divmod(x, 2)
		ans += m
	return ans

def howmany_one_method2(x):
	"""解法2, 利用x &= x -1计算的性质, 每次将最后的一个1变成0
	例如:
		100 & 011 => 000, 
		110 & 101 => 100,
		101 & 100 => 100,
	没计算一次即可将最后的一个1变成0, 那么复杂度等于x中1的个数。
	非常巧妙的算法。
	"""
	ans = 0
	while x:
		ans += 1
		x &= x - 1
	return ans

if __name__ == "__main__":
	x = 815637813459082348957132894617849012337588917394
	
	st = time.clock()
	ans = howmany_one_method1(x)
	print("elapse %.6f sec" % (time.clock() - st))
	print(ans)
	
	st = time.clock()
	ans = howmany_one_method2(x)
	print("elapse %.6f sec" % (time.clock() - st))
	print(ans)