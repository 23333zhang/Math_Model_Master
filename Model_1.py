"""  数学建模|飞蛾扑火|Model_1
    date  : 2022-11-11
    author: zhang jia jun
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import mpl
import random

# 螺旋函数
def luoxuan(a, b, theta):
    r = a * np.exp(theta * b)
    x = r * np.cos(theta) - 0
    y = r * np.sin(theta) - 0
    return x, y

if __name__ == '__main__':
    a = 1
    b = -0.1
    theta = np.linspace(0, 6 * 2 * np.pi, 1000)
    x, y = luoxuan(a, b, theta)
    plt.plot([1], [0], c='red', marker='+', markersize=10)
    plt.plot([0], [0], c='red', marker='*', markersize=10)
    plt.plot(x, y, c='b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()