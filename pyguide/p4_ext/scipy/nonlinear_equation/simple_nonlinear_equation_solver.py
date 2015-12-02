#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
一个x, 一个y的非线性方程数值求解法

Ref: http://docs.scipy.org/doc/scipy/reference/optimize.nonlin.html
"""

import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    """原方程
    y = f(x) = cos(x) + exp(x) + abs(x)
    """
    return np.cos(x) + np.exp(x) + np.abs(x)

def F(x):
    """求解方程
    """
    return np.array([func(i) for i in x]) - [
        4.2585841343271849, 8.9729092623835083, 22.095544426587221, 57.944506412280624]

if __name__ == "__main__":
    expect = [1, 2, 3, 4] # func(expect) = [4.258584, 8.972909, 22.095544, 57.944506]
#     print([func(i) for i in expect])
    res = scipy.optimize.root(F, [0, 1, 2, 3], tol=1e-14)
    error = res.x - expect
    print(error) # almost zero
    
    x = np.arange(-5.0, 2.0, 0.1)
    y = func(x)
    plt.plot(x, y)
    plt.show()