#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
queuelib原本是scrapy项目中用于实现磁盘一致的任务队列管理的模块。现在这个模块被
单独拿出来作为一个库供大家使用。

queuelib的特点主要是实现磁盘一致, 使得在任务掉电中断时, 仍然能够通过重启任务接着
上一次的进度继续进行。所以 **queuelib 不适合做 priority queue 或是 FIFO, LIFO
的高性能实现。**

PyPI: https://pypi.python.org/pypi/queuelib
Github: https://github.com/scrapy/queuelib
Document: 没有
"""

from queuelib import PriorityQueue, FifoDiskQueue

if __name__ == "__main__":
    import string
    import random
    import time
    
    def randstr():
        res = list()
        for _ in range(8):
            res.append(random.choice(string.ascii_letters))
        return "".join(res).encode("utf-8")
    
    tasks = [(randstr(), random.randint(1, 5))for i in range(1000)]
    
    st = time.clock()
    
    qfactory = lambda priority: FifoDiskQueue('queue-dir-%s' % priority)
    pq = PriorityQueue(qfactory)
    for task in tasks:
        pq.push(*task)
    for _ in range(len(pq)):
        pq.pop()
        
    print("queuelib takes %.6f sec." % (time.clock() - st,))