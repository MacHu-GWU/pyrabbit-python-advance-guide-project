#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np, pandas as pd
import time

def group_by_one_key():
    df = pd.DataFrame()
    df["ID"] = np.random.randint(1, 10, 100)
    df["value"] = np.random.randn(100)
    
    st = time.clock()
    for ID in df["ID"].unique():
        sub_df = df[df["ID"] == ID]
    print(time.clock() - st)
    
    st = time.clock()
    grouped = df.groupby("ID")
    for name, group in grouped:
        pass
    print(time.clock() - st)

    grouped = df.groupby("ID")
    for name, group in grouped:
        print(group)
        
# group_by_one_key()

def group_by_two_key():
    df = pd.DataFrame()
    df["ID1"] = np.random.randint(1, 10, 100)
    df["ID2"] = np.random.randint(1, 10, 100)
    df["value"] = np.random.randn(100)
    
    grouped = df.groupby(["ID1", "ID2"])
    for name, group in grouped:
        print(group)
        
# group_by_two_key()

def group_and_aggregate():
    df = pd.DataFrame()
    df["ID"] = np.random.randint(1, 10, 100)
    df["value1"] = np.random.randn(100)
    df["value2"] = np.random.randn(100)
    grouped = df.groupby("ID")
    print(grouped.agg({"value1": np.mean, "value2": np.std}))
    
# group_and_aggregate()

def group_and_transform():
    df = pd.DataFrame()
    df["ID"] = np.random.randint(1, 10, 100)
    df["value"] = np.random.randn(100)
    zscore = lambda x: (x - x.mean()) / x.std()
    transformed = df.groupby("ID").transform(zscore)
    df["value"] = transformed["value"]
    print(df.groupby("ID").mean())
    print(df.groupby("ID").std())
        
# group_and_transform()

def group_and_apply():
    df = pd.DataFrame()
    df["ID"] = np.random.randint(1, 10, 100)
    df["A"] = np.random.randn(100)
    df["B"] = np.random.randn(100)
    grouped = df.groupby("ID").apply(lambda x: x + 100)
    for name, group in grouped:
        print(group)
        
# group_and_apply()

# index = pd.date_range('10/1/1999', periods=1100)
# ts = pd.Series(np.random.normal(0.5, 2, 1100), index)
# ts = pd.rolling_mean(ts, 100, 100).dropna()
# key = lambda x: x.year
# zscore = lambda x: (x - x.mean()) / x.std()
# transformed = ts.groupby(key).transform(zscore)
# print(transformed)
# print(ts)
