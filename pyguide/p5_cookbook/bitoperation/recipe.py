#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
本模块提供了一些用位运算实现的高性能计算算法。在实际应用时, 请单独把函数主体拿出
来使用, 而不要直接import函数。因为既然要追求极致性能, 就不该在调用函数上浪费时间。
"""

def get_the_last_bit(x):
    """求最后一位是0还是1。
    
    解: 跟1求 位与
    """
    return x & 1

def get_the_last_k_bit(x, k):
    """求倒数第k位是0还是1。
    
    解: 跟100...0 (k-1个0) 求位与, 看是不是等于0
    """
    return (x & 1 << (k - 1)) != 0

def is_two_power(x):
    """检查是否是2的整数幂。
    
    解: 跟 -1 的值求 位与, 如果为0说明是
    """
    return (x & (x - 1)) == 0

def howmany_one(x):
    """求一共有多少位是1。
    
    解: 利用 x &= x - 1 每次消除一位最后的1的特性
    """
    ans = 0
    while x:
        ans += 1
        x &= x - 1
    return ans

def howmany_different(x, y):
    """求有多少位不相同。
    
    解: 先位异或, 然后求1的个数
    """
    difference = x ^ y
    ans = 0
    while difference:
        ans += 1
        difference &= difference - 1
    return ans

def create_bitmap(array):
    """生成集合的bitmap。
    
    Example::
    
        >>> array = [1, 3, 5]
        >>> create_bitmap(array)
        0b10101
    """
    x = 0
    for i in array:
        x += 1 << (i-1)
    return x

def parse_bitmap(x):
    """根据bitmap, 解析出集合。
    
    Example:
    
        >>> bitmap = 0b10101
        >>> parse_bitmap(bitmap)
        [1, 3, 5]
    """
    array = list()
    counter = 1
    while x:
        if x & 1:
            array.append(counter)
        x = x >> 1
        counter += 1
    return array

def union_bitmap(x, y):
    """求x, y的交集, x, y是集合各自的bitmap。
    """
    return x | y

def intersect_bitmap(x, y):
    """求并集, x, y是集合各自的bitmap。
    """
    return x & y

def difference_bitmap(x, y):
    """从x中丢弃所有y中的元素, x, y是集合各自的bitmap。
    """
    return x & (~ y)


if __name__ == "__main__":
    import unittest
    import time
    import random
    
    class BitMathUnittest(unittest.TestCase):
        """测试位运算的一些技巧的函数是否工作正常。
        """
        def test_all(self):
            self.assertEqual(get_the_last_bit(1), 1)
            self.assertEqual(get_the_last_bit(-1), 1)
            
            self.assertEqual(get_the_last_k_bit(5, 3), 1)

            self.assertEqual(is_two_power(4), True)
            self.assertEqual(is_two_power(5), False)
            
            self.assertEqual(howmany_one(5), 2)
            
            self.assertEqual(howmany_different(7, 0), 3)
            
            self.assertEqual(create_bitmap([1, 3, 5]), 21)
            self.assertListEqual(parse_bitmap(21), [1, 3, 5])
            
#     unittest.main()
    
    complexity = 1000
    
    def test_find_isodd_performance():
        """测试利用位运算实现计算是否是奇数的性能。
        """
        x = random.randint(0, 2**32)
        
        st = time.clock()
        for i in range(complexity):
            x % 2
        print("check is odd: math method takes %.6f sec." % (time.clock() - st,))
        
        st = time.clock()
        for i in range(complexity):
            x & 1
        print("check is odd: bit method takes %.6f sec." % (time.clock() - st,))
    
#     test_find_isodd_performance()

    def test_get_the_last_k_bit_performance():
        """测试用位运算求二进制形式倒数第N位的值的性能。
        """
        x = random.randint(0, 2**32)
        k = 44
        st = time.clock()
        for _ in range(complexity):
            div = x
            for _ in range(k):
                div, mod = divmod(div, 2)
        print("get the last k bit: math method takes %.6f seconds" % (time.clock() - st,))
        
        st = time.clock()
        for i in range(complexity):
            (x & 1 << (k - 1)) != 0
        print("get the last k bit: bit method takes %.6f seconds" % (time.clock() - st,))
      
#     test_get_the_last_k_bit_performance()

    def test_howmany_one_performance():
        x = random.randint(0, 2**32)
        testdata = [x for i in range(complexity)]
        
        st = time.clock()
        for x in testdata:
            ans = 0
            div = x
            while div:
                div, mod = divmod(div, 2)
                ans += mod
        print("howmany one: bit method takes %.6f seconds" % (time.clock() - st,))
        
        st = time.clock()
        for x in testdata:
            ans = 0
            while x:
                ans += 1
                x &= x - 1
        print("howmany one: bit method takes %.6f seconds" % (time.clock() - st,))
    
#     test_howmany_one_performance()

    def test_howmany_difference_performance():
        x = 8237548927358942735
        y = 1738575893482930758

        testdata_x = [x for i in range(complexity)]
        testdata_y = [y for i in range(complexity)]
        
        st = time.clock()
        for x, y in zip(testdata_x, testdata_y):
            ans = 0
            div_x = x
            div_y = y
            while (div_x or div_y):
                div_x, mod_x = divmod(div_x, 2)
                div_y, mod_y = divmod(div_y, 2)
                ans += (mod_x != mod_y)
        print("howmany difference: bit method takes %.6f seconds" % (time.clock() - st,))
        
        st = time.clock()
        for x, y in zip(testdata_x, testdata_y):
            difference = x ^ y
            ans = 0
            while difference:
                ans += 1
                difference &= difference - 1
        print("howmany difference: bit method takes %.6f seconds" % (time.clock() - st,))
    
#     test_howmany_difference_performance()

    def test_bitmap_set_performance():
        """测试使用bitmap作为集合的容器在进行交, 并, 补时候的性能。
        """
        x = set([1, 7, 8, 19, 24])
        y = set([5, 8, 19, 33, 67])
        x1 = create_bitmap(x)
        y1 = create_bitmap(y)
        
        st = time.clock()
        for i in range(complexity):
            x.union(y)
        print("set union: Naive set method takes %.6f sec." % (time.clock() - st,))
        
        st = time.clock()
        for i in range(complexity):
            x1 | y1
        print("set union: Bit math method takes %.6f sec." % (time.clock() - st,))
    
        st = time.clock()
        for i in range(complexity):
            x.intersection(y)
        print("set intersect: Naive set method takes %.6f sec." % (time.clock() - st,))
        
        st = time.clock()
        for i in range(complexity):
            x1 & y1
        print("set intersect: Bit math method takes %.6f sec." % (time.clock() - st,))
        
        st = time.clock()
        for i in range(complexity):
            x.difference(y)
        print("set difference: Naive set method takes %.6f sec." % (time.clock() - st,))
        
        st = time.clock()
        for i in range(complexity):
            x1 & (~ y1)
        print("set difference: Bit math method takes %.6f sec." % (time.clock() - st,))
    
#     test_bitmap_set_performance()
     
    def test_create_and_parse_bitmap_set_performance():
        """测试使用bitmap作为集合的容器在进行交, 并, 补时候的性能。
        
        注: 如果算上创建集合和解析集合的时间, bitmap作为集合的方法是不如
        原生set的。但是作为计算次数远远多于创建集合的次数的情况, bitmap性能
        要优于原生set。
        """
        array = [1, 6, 17, 22, 37, 48]
    
        st = time.clock()
        for i in range(complexity):
            set(array)
        print("construct set takes %.6f sec." % (time.clock() - st,))    
    
        st = time.clock()
        for i in range(complexity):
            create_bitmap(array)
        print("create_bigmap takes %.6f sec." % (time.clock() - st,))
         
        x = random.randint(0, 2**32)
        st = time.clock()
        for i in range(complexity):
            parse_bitmap(x)
        print("parse_bitmap takes %.6f sec." % (time.clock() - st,))
        
#     test_create_and_parse_bitmap_set_performance()