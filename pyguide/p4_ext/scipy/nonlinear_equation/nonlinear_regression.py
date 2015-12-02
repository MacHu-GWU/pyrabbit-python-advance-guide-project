import numpy as np
from scipy.optimize import curve_fit

def func(x, a1, a2):
    """原方程
    y = f(x1, x2) = x1 * x2 + (x1 + x2) ^ 2
    """
    x1, x2 = x
    return a1 * x1 * x2 + (x1 + x2) ** a2

a = [2.0, 4.0] # func(expect) = [  4.25858413   8.97290926  22.09554443  57.94450641]
x = np.array([[1, 2], [3, 4]])
y = np.array([func(arg, a[0], a[1]) + np.random.rand() - 0.5 for arg in x]) 
popt, pcov = curve_fit(func, x.T, y)
print(popt)