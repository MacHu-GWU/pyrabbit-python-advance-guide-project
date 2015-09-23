#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
一个用Python自带关键字的map, reduce写的一个word count的mapreduce应用。
"""


try:
    from functools import reduce
except:
    pass

from collections import defaultdict
import random
import string
import time

def randstr(allowed, length):
    """Generate fixed-length random string from your allowed character pool.
    
    Usage Example::
    
        >>> import string
        >>> randstr(string.ascii_letters + string.digits, 32)
        QE1UKzSrIw8z7EiEp94FJ3jwmuYNUw2N
    """
    if (not isinstance(length, int)) or (length <= 0):
        raise Exception("length parameter has to be an integer greater than 0!")
    
    res = list()
    for _ in range(length):
        res.append(random.choice(allowed))
    return "".join(res)
    
def rand_article(num_p=(4, 10), num_s=(2, 15), num_w=(5, 40)):
    """Random article text.
    """
    article = list()
    for _ in range(random.randint(*num_p)):
        p = list()
        for _ in range(random.randint(*num_s)):
            s = list()
            for _ in range(random.randint(*num_w)):
                s.append(randstr(string.ascii_lowercase, 
                                 random.randint(1, 15)))
            p.append(" ".join(s))
        article.append(". ".join(p))
    return "\n\n".join(article)

def generate_testdata():
    N = 1000
    documents = [rand_article() for _ in range(N)]
    return documents
    
def main():
    """
    
    **中文文档**
    
    一个用Python自带关键字的map, reduce写的一个word count的mapreduce应用。
    """
    def mapper(doc):
        """返回单个文档的单词频率统计字典。
        """
        d = defaultdict(int)
        
        for i in doc.replace(".", " ").split(" "):
            i = i.strip()
            if i:
                d[i] += 1
        
        return d
    
    def reducer(d1, d2):
        """合并两单词词频率统计字典。
        """
        for k, v in d2.items():
            d1[k] = d1.get(k, 0) + v
        return d1
    
    documents = generate_testdata()
    
    st = time.clock()
    res1 = reduce(reducer, map(mapper, documents))
    print("mapreduce solution takes %.6f sec." % (time.clock() - st,))
    
    st = time.clock()
    res2 = defaultdict(int)
    for doc in documents:
        for i in doc.replace(".", " ").split(" "):
            i = i.strip()
            if i:
                res2[i] += 1
    print("naive stream processing solution takes %.6f sec." % (time.clock() - st,))
    
    print(res1 == res2)

if __name__ == "__main__":
    main()