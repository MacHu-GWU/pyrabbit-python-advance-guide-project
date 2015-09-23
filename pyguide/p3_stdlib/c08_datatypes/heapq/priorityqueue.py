#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
本模块是一个用heapq实现priority queue数据结构的例子。
"""

from __future__ import print_function
from heapq import *
import itertools

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = "<removed-task>"      # placeholder for a removed task
counter = itertools.count()     # unique sequence count
    
def add_task(task, priority=0):
    "Add a new task or update the priority of an existing task"
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    "Mark an existing task as REMOVED.  Raise KeyError if not found."
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    "Remove and return the lowest priority task. Raise KeyError if empty."
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError("pop from an empty priority queue")

if __name__ == "__main__":
    import string
    import random
    import time
    
    def randstr():
        res = list()
        for _ in range(8):
            res.append(random.choice(string.ascii_letters))
        return "".join(res)
    
    tasks = [(randstr(), random.randint(1, 5))for i in range(1000)]

    st = time.clock()
    
    for task in tasks:
        add_task(*task)
        
    for _ in range(len(pq)):
        pop_task()
        
    print("heap takes %.6f sec." % (time.clock() - st,))
    

    