#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np, pandas as pd
import unittest

class Unittest(unittest.TestCase):
    """本测试用于展示如何对df.index, df.columns进行修改, 重命名
    """
    def setUp(self):
        """准备测试数据
        """
        columns = ["employee_id", "lastname", "firstname", 
                   "date_of_birth", "height in cm", "role_code"]
        data = [
            ["E-001", "Barrack", "Obama", "08/04/1961", 183.5, 1],
            ["E-002", "Jackson", "Mickael", "08/29/1958", 175.3, 5],
        ]
        self.df = pd.DataFrame(data, columns=columns)
    
    def test_rename_column_solution1(self):
        """直接替换整个df.columns
        """
        new_columns = ["employee_id", "lastname", "firstname", 
                       "dob", "height", "role_code"]
        self.df.columns = new_columns
        print(self.df.columns.tolist())
        
    def test_rename_column_solution2(self):
        """使用字典的形式根据映射替换df.columns
        """
        self.df.rename(columns={"date_of_birth": "dob",
                                "height in cm": "height",}, inplace=True)
        print(self.df.columns.tolist())
        
    def test_rename_column_solution3(self):
        """使用函数的形式对所有column进行转换
        """
        self.df.rename(columns=lambda x: "Col-" + x, inplace=True)
        print(self.df.columns.tolist())
    
    def test_rename_index_solution1(self):
        """直接替换整个df.index
        """
        new_index = ["a", "b"]
        self.df.index = new_index
        print(self.df.index.tolist())
        
    def test_rename_index_solution2(self):
        """使用字典的形式对替换指定的若干个index
        """
        self.df.rename(index={1: 100}, inplace=True)
        print(self.df.index.tolist())
            
if __name__ == "__main__":
    unittest.main()