# # 通过statsment创建数字模型
# import numpy as np
# import statsmodels.api as sm
#
# # 读取txt文件并提取数据
# data = np.loadtxt('output-L2.txt')
# h = data[:,0]
# vx = data[:,1]
# L = data[:,2]
# alpha = data[:,3]
#
# # 构建多元线性回归模型
# X = np.column_stack((h, vx, alpha))
# X = sm.add_constant(X)
# model = sm.OLS(L, X).fit()
#
# # 输出拟合结果
# print(model.summary())

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # 读取数据
# data = np.loadtxt('output-L2.txt')
#
#
# # 从数据中提取变量
# v = data[:, 0]
# h = data[:, 1]
# alpha = data[:, 2]
# L = data[:, 3]
#
# # 绘制3D图像
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(v, h, alpha, c=L, cmap='coolwarm')
# ax.set_xlabel('v')
# ax.set_ylabel('h')
# ax.set_zlabel('alpha')
# ax.set_title('L vs. v, h, alpha')
# plt.show()
#

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit

# 读取数据
data = np.loadtxt('output-L2.txt')

# 将数据分别存入变量
L = data[:, 0]
v = data[:, 1]
h = data[:, 2]
alpha = data[:, 3]

# 定义拟合函数
def func(x, a, b, c, d, e, f):
    v, h, alpha = x
    return a * v**2 + b * h + c * alpha + d * v + e * h**2 + f

# 进行拟合
popt, pcov = curve_fit(func, (v, h, alpha), L)

# 输出拟合系数
print('a =', popt[0])
print('b =', popt[1])
print('c =', popt[2])
print('d =', popt[3])
print('e =', popt[4])
print('f =', popt[5])

# 定义绘图函数
def plot_figure():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(v, h, L, c='r', marker='o')
    ax.set_xlabel('v')
    ax.set_ylabel('h')
    ax.set_zlabel('L')
    x = np.linspace(min(v), max(v), 100)
    y = np.linspace(min(h), max(h), 100)
    X, Y = np.meshgrid(x, y)
    Z = func((X, Y, alpha[0]), *popt)
    ax.plot_surface(X, Y, Z, alpha=0.5)
    plt.show()

# 绘制图像
plot_figure()
