"""  数学建模|飞蛾扑火|Model_3
    date  : 2022-11-11
    author: zhang jia jun
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import mpl
import random
import sympy
from scipy.optimize import root

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
# 螺旋函数
def luoxuan(a, b, theta):
    r = a * np.exp(theta * b)
    x = r * np.cos(theta) - 1
    y = r * np.sin(theta) - 0
    return x, y

# 圆
def circle(r, point):
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = r*np.cos(theta) + point[0]
    y = r*np.sin(theta) + point[1]
    return x, y

# 求角Alpha
def Alpha(y, alpha1):
    if y ==0:
        y = 0.001
        Alpha2 = alpha1 - 2 * np.arctan(1 / y)
    else:
        Alpha2 = alpha1 - 2 * np.arctan(1 / y)
    return Alpha2

#求参数b
def Parameter_b(alpha):
    b = 1 / np.tan(alpha)
    return -b

def Parameter_a(y, b, theta):
    a = y/(np.exp(b*theta) * np.sin(theta))
    return a

if __name__ == '__main__':
    point1 = [1, 0]
    point2 = [-1, 0]
    circle_point = [3, 0]
    a1 = 4
    b1 = -0.1
    theta = np.linspace(0, 6 * 2 * np.pi, 1000)
    index = []
    x1 = a1 * np.exp(b1 * theta) * np.cos(theta) + 1
    y1 = a1 * np.exp(b1 * theta) * np.sin(theta) + 0

    # 求方程近似解
    solve_1 = x1**2 - 6*x1 + 1 + y1**2
    solve_1[abs(solve_1) < 0.04] = 0
    # plt.plot(theta, solve_1, c='b',label='曲线1')
    for i in range(1000):
        if abs(solve_1[i]) == 0:
            index = i
            break
    theta_end = theta[index]
    theta = theta[0:index+1]
    x1 = a1 * np.exp(b1 * theta) * np.cos(theta) + 1    # 切片后的曲线1参数方程
    y1 = a1 * np.exp(b1 * theta) * np.sin(theta) + 0
    gen_x = a1 * np.exp(b1 * theta_end) * np.cos(theta_end) + 1     # 求出临界点
    gen_y = a1 * np.exp(b1 * theta_end) * np.sin(theta_end) + 0
    theta_start = np.arctan(gen_y/(gen_x+1))    # 初相角
    alpha = np.arctan(10) - np.arctan((1+gen_x)/gen_y) + np.arctan((gen_x-1)/gen_y)
    b2 = Parameter_b(alpha)
    a2 = Parameter_a(gen_y, b2, theta_start)
    theta2 = np.linspace(theta_start, 6 * 2 * np.pi, 1000)
    x2, y2 = luoxuan(a2, b2, theta2)

    x3, y3 = circle(np.sqrt(8), circle_point)
    plt.plot(x1, y1, c='b',label='曲线1')
    plt.plot(x2, y2, c='g', label='曲线2')
    plt.plot(x3, y3, c='r', label='圆')
    plt.plot([1], [0], c='red', marker='+', markersize=10)
    plt.plot([-1], [0], c='red', marker='*', markersize=10)
    plt.plot(5, 0, c='blue', marker='+', markersize=10)  # 起点
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.show()