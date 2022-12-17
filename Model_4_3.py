"""  数学建模|飞蛾扑火|Model_4-2
    date  : 2022-11-13
    author: zhang jia jun
"""
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
#求参数b
def Parameter_b(alpha):
    b = 1 / np.tan(alpha)
    return b

# 求参数a
def Parameter_a(y, b, theta):
    a = y/(np.exp(b*theta) * np.sin(theta))
    return a

# 螺旋函数
def luoxuan(a, b, theta):
    r = a * np.exp(theta * b)
    x = r * np.cos(theta) - 1
    y = r * np.sin(theta) * (np.sqrt(2) / 2)
    z = r * np.sin(theta) * (np.sqrt(2) / 2)
    return x, y, z

# 求交点的函数
def jiaodian(x):
    index = []
    for i in range(1000):
        if x[i] == 0:
            index.append(i)
    return index

# 求角Alpha
def Alpha(y, alpha1):
    if y ==0:
        y = 0.001
        Alpha2 = alpha1 - 2 * np.arctan(1 / y)
    else:
        Alpha2 = alpha1 - 2 * np.arctan(1 / y)
    return Alpha2

# 球体
def solid():
    center = [3, 0, 0]
    r = 2*np.sqrt(2)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = r * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = r * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = r * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
    return x, y, z

if __name__ == '__main__':
    ax = plt.axes(projection='3d')
    alpha = np.pi - np.arctan(np.sqrt(2))
    b1 = Parameter_b(alpha)
    a1 = 4
    theta = np.linspace(0, 10 * 2 * np.pi, 1000)  # 绘图行向量
    r = a1 * np.exp(theta * b1)
    x1 = r * np.cos(theta) + 1
    y1 = r * np.sin(theta) * (np.sqrt(2) / 2)
    z1 = r * np.sin(theta) * (np.sqrt(2) / 2)

    #球
    x2, y2, z2 = solid()

    # 求方程近似解
    solve_1 = x1**2 - 6*x1 + 1 + y1**2 + z1**2
    solve_1[abs(solve_1) < 0.04] = 0
    ax.plot3D(5, 0, 0, marker='+', markersize=10)
    ax.plot3D(1, 0, 0, marker='*', markersize=10)
    ax.plot3D(-1, 0, 0, marker='*', markersize=10)
    ax.plot3D(x1, y1, z1, label='曲线1',c='r')
    ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, color='b',linewidth=0, alpha=0.5)
    # ax.scatter(x2, y2, z2,c='b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # ax.set_xlim(-5,10)
    # ax.set_ylim(-10,10)
    # ax.set_zlim(-10,10)
    ax.legend()
    plt.show()