"""  数学建模|飞蛾扑火|Model_4-1
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

ax = plt.axes(projection='3d')

alpha = np.pi - np.arctan(np.sqrt(2))
b1 = Parameter_b(alpha)
a1 = 5
theta = np.linspace(0, 6 * 2 * np.pi, 1000)  # 绘图行向量
r = a1 * np.exp(theta * b1)
x = r * np.cos(theta)
y = r * np.sin(theta) * (np.sqrt(2)/2)
z = r * np.sin(theta) * (np.sqrt(2)/2)

ax.plot3D(5, 0, 0, marker='+', markersize=10)
ax.plot3D(0, 0, 0, marker='*', markersize=10)
ax.plot3D(x, y, z, label='轨迹')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# ax.set_xlim(-5,10)
# ax.set_ylim(-10,10)
# ax.set_zlim(-10,10)
ax.legend()
plt.show()