"""  数学建模|飞蛾扑火|Model_2
    date  : 2022-11-11
    author: zhang jia jun
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import mpl
import random
from sympy import *
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

# 距离函数
def distance(x, y):
    d1 = np.sqrt(((x-1)**2 + y**2))
    d2 = np.sqrt(((x+1)**2 + y**2))
    # D = d1 - d2 > 0 离光源2近
    # D = d1 - d2 < 0 离光源1近
    my_index = [0]
    D = d1 - d2
    for i in range(len(D)):
        if D[i]>0:
            my_index.append(i)
            print(my_index)
    return D, my_index

# 随机数0-1
def my_rand():
    out = random.randint(0, 1)
    return out

# 求交点的函数
def jiaodian(x):
    index = []
    for i in range(1000):
        if x[i] == 0:
            index.append(i)
    return index

# 螺旋函数
def luoxuan(a, b, theta):
    r = a * np.exp(theta * b)
    x = r * np.cos(theta) - 1
    y = r * np.sin(theta) - 0
    return x, y

# 求角Alpha
def Alpha(y, alpha1):
    if y ==0:
        y = 0.001
        Alpha2 = alpha1 - 2 * np.arctan(1 / y)
    else:
        Alpha2 = alpha1 - 2 * np.arctan(1 / y)
    return Alpha2

def circle(r):
    theta_circle = np.linspace(0, 2 * np.pi, 1000)

if __name__ == '__main__':
    plt.axis("equal")
    start = [5, 0]  # 飞蛾起点
    plt.plot([1], [0], c='red', marker='+', markersize=10)  # 光源右
    plt.plot([-1], [0], c='red', marker='+', markersize=10)  # 光源左
    plt.plot([start[0]], [start[1]], c='blue', marker='+', markersize=10)  # 起点

    theta = np.linspace(0, 6 * 2 * np.pi, 1000)  # 绘图行向量
    # theta1 = np.arange(0,100*np.pi,0.01*np.pi)

    # 曲线1
    r1 = 4 * np.exp(theta * -0.1)
    x1 = r1 * np.cos(theta) + 1
    x1[abs(x1) < 0.03] = 0  # 零点
    y1 = r1 * np.sin(theta) - 0
    index1 = jiaodian(x1)  # 得到焦点的index0
    print(x1[index1], y1[index1])
    print(np.rad2deg(theta[index1[0]]))
    x1 = x1[0:index1[0] + 1]
    y1 = y1[0:index1[0] + 1]

    # 求下个曲线初相角
    end_x1 = 0
    end_y1 = y1[-1]
    theta_start2 = np.arctan(end_y1 / 1)  # 曲线2的初相角
    theta2 = np.linspace(theta_start2, 6 * 2 * np.pi, 1000)
    b2 = 1.0 / np.tan(Alpha(end_y1, np.arctan(10)))
    a2 = y1[index1[0]] / (np.exp(-b2 * theta_start2) * np.sin(theta_start2))
    x2, y2 = luoxuan(a2, -b2, theta2)
    print(a2, b2)
    plt.plot(x1, y1, c='blue', label='曲线1')
    plt.plot(x2, y2, c='c', label='曲线2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()
