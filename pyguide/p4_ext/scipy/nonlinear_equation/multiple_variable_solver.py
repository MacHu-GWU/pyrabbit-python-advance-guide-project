#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
多元非线性方程组

Ref: http://docs.scipy.org/doc/scipy/reference/optimize.nonlin.html
"""

import scipy.optimize
import numpy as np
from scipy.optimize import curve_fit

def func(x1, x2, a1, a2):
    """原方程
    y = f(x1, x2) = x1 * x2 + (x1 + x2) ^ 2
    """
    return a1 * x1 * x2 + (x1 + x2) ** a2

if __name__ == "__main__":
    expect = [2.0, 4.0] # func(expect) = [  4.25858413   8.97290926  22.09554443  57.94450641]
    x = np.array([[1, 2], [3, 4]])
    y = np.array([func(arg[0], arg[1], expect[0], expect[1]) + np.random.rand() - 0.5 for arg in x]) 

    def F(a):
        """求解方程
        """
        return a[0] * np.product(x, axis=1) + np.power(np.sum(x, axis=1), a[1]) - y

    x0 = [1.3, 0.7, 0.8, 1.9, 1.2]
    res = scipy.optimize.minimize(scipy.optimize.rosen, x0, method='Nelder-Mead')
    print(res.x)
    print(scipy.optimize.rosen(res.x))
#     print(F(expect))
#     res = scipy.optimize.minimize(F, [2, 4], method="Nelder-Mead")
#     print(res)

#     res = scipy.optimize.root(F, [0, 1, 2, 3], tol=1e-14)
#     error = res.x - expect
#     print(error)
#     
#     x = np.arange(-5.0, 2.0, 0.1)
#     y = func(x)
#     plt.plot(x, y)
#     plt.show()