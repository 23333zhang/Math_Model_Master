"""  数学建模|飞蛾扑火|Model_4-2
    date  : 2022-11-12
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

if __name__ == '__main__':
    ax = plt.axes(projection='3d')
    alpha = np.pi - np.arctan(np.sqrt(2))
    b1 = Parameter_b(alpha)
    a1 = 4
    theta = np.linspace(0, 6 * 2 * np.pi, 1000)  # 绘图行向量
    r = a1 * np.exp(theta * b1)
    x1 = r * np.cos(theta) + 1
    x1[abs(x1) < 0.03] = 0  # 零点
    index1 = jiaodian(x1)  # 得到焦点的index0
    y1 = r * np.sin(theta) * (np.sqrt(2) / 2)
    z1 = r * np.sin(theta) * (np.sqrt(2) / 2)

    # # 轨迹平面坐标系下的x, y
    # x = x1
    # y = r * np.sin(theta)
    # x = x[0:index1[0] + 1]
    # y = y[0:index1[0] + 1]
    #
    # # 三维坐标系下的曲线1
    # x1 = x1[0:index1[0] + 1]
    # y1 = y1[0:index1[0] + 1]
    # z1 = z1[0:index1[0] + 1]

    # 曲线1的终点
    # end_x1 = 0
    # end_y1 = y1[-1]
    # end_z1 = z1[-1]
    # end_y = y[-1]

    # theta_start2 = np.arctan(end_y / 1)  # 曲线2的初相角
    # theta2 = np.linspace(theta_start2, 6 * 2 * np.pi, 1000)
    # b2 = 1.0 / np.tan(Alpha(end_y, np.arctan(10)))
    # a2 = y[index1[0]] / (np.exp(-b2 * theta_start2) * np.sin(theta_start2))
    # x2, y2, z2 = luoxuan(a2, -b2, theta2)
    x = np.linspace(-3, 5, 1000)
    y = x * np.sin(np.pi/6)
    z = y
    ax.plot3D(5, 0, 0, marker='+', markersize=10)
    ax.plot3D(1, 0, 0, marker='*', markersize=10)
    ax.plot3D(-1, 0, 0, marker='*', markersize=10)
    ax.plot3D(x1, y1, z1, label='曲线1')
    # ax.plot3D(x, y, z)
    # ax.plot3D(x2, y2, z2, label='曲线2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # ax.set_xlim(-5,10)
    # ax.set_ylim(-10,10)
    # ax.set_zlim(-10,10)
    ax.legend()
    plt.show()