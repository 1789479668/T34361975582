from sympy import diff
from sympy import symbols
import math as m

g = 9.8     # 重力加速度
rho = 1.29   # 空气密度kg/m^3，ρ
C = 0.8    # 风阻系数，球体为0.5
M = 50     # 无人机重量
D = 0.4   # 无人机边长

# alpha在0~pi/2，beta没有限制
u = 6           # 风速
beta = m.pi/6    # 风向

def object_func(v,alpha,u,beta):
    return ((v * m.cos(alpha) - u * m.cos(beta))**2+(v * m.sin(alpha) - u * m.sin(beta))**2)*m.exp(abs(m.cos(alpha - beta)))

v,alpha = symbols("v,alpha")

print(diff(object_func(v,alpha,u,beta),v))
