#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import binascii
import base64
import pickle
import random
import time

def functionality():
    """Test how 'bytes to string and string to bytes' is been done.
    
    Conclusion: binascii.b2a_base64 and base64.b64encode are doing same things.
    """
    d = {random.randint(1, 10 ** 6): random.randint(1, 10 ** 3) for i in range(3)} 
    b = pickle.dumps(d)

    s = binascii.b2a_base64(b).decode("utf-8") # string
    b_recovered =binascii.a2b_base64(s.encode("utf-8")) # bytes
    
    print("=== module binascii ===")
    print(b)
    print(type(s), s.strip()) # b2a_base64 has a 'newline' at the end
    print(b_recovered)
    
    s = base64.b64encode(b).decode("utf-8") # string
    b_recovered = base64.b64decode(s.encode("utf-8")) # bytes
    
    print("=== module base64 ===")
    print(b)
    print(type(s), s)
    print(b_recovered)

functionality()

def performance_test():
    """Module binascii vs base64.
    
    Conclusion: binascii is faster than base64.
    """
    complexity = 1000
    
    d = {random.randint(1, 10 ** 6): random.randint(1, 10 ** 3) for i in range(3)} 
    b = pickle.dumps(d)

    st = time.clock()
    for i in range(complexity):
        binascii.b2a_base64(b)
    print("binascii.b2a_base64 %.6f sec" % (time.clock() - st))
    
    st = time.clock()
    for i in range(complexity):
        base64.b64encode(b)
    print("base64.b64encode %.6f sec" % (time.clock() - st))
    
performance_test()