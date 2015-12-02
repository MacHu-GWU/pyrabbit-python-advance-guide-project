#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np, pandas as pd
import unittest

class Unittest(unittest.TestCase):
    def setUp(self):
        pass
    
    
#     def test_all(self):
#         df1 = pd.DataFrame([[1, 2], [3, 4]])
#         df2 = pd.DataFrame([[5, 6], [7, 8]])
#         print(pd.concat([df1, df2], axis=0))
#         print(pd.concat([df1, df2], axis=1))
    
#     def test_merge(self):
#         left = pd.DataFrame({"key": ["k1", "k2", "k3"],
#                              "value": [1, 2 ,3]})
#         right = pd.DataFrame({"key": ["k2", "k3", "k4"],
#                               "value": [4, 5 ,6]})
#         result = pd.merge(left, right, on="key")
#         print(result)
        
    def test_join(self):
        left = pd.DataFrame({"key": ["k1", "k2", "k3"],
                             "value": [1, 2 ,3]})
        right = pd.DataFrame({"key": ["k2", "k3", "k4"],
                              "value": [4, 5 ,6]})
        print(left.join([right,]))
        
#     def test_update(self):
#         df1 = pd.DataFrame(np.ones((4, 4)))
#         df2 = pd.DataFrame(np.random.randn(4, 4))
#         df2.loc[1, 2] = None
#         
#         df1.update(df2)
#         print(df1)
        
if __name__ == "__main__":
    unittest.main()