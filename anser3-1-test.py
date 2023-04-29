import numpy as np
import math as m
from sympy import diff
from sympy import symbols

# 无人机参数(正方体)
g = 9.8     # 重力加速度
rho = 1.29   # 空气密度kg/m^3，ρ
C = 0.8    # 风阻系数，球体为0.5
M = 50     # 无人机重量
D = 0.4   # 无人机边长

# alpha在0~pi/2，beta没有限制
v = 300/3.6      # 无人机发射速度，在300~400之间，dv为定值
alpha = m.pi/4   # 俯冲角度，dalpha为定制
u = 6           # 风速
beta = m.pi/6    # 风向

#俯冲角度alpha与飞行速度V的变化率dalpha、dv为定值
def object_func(v,alpha,u,beta):
    # 为阻力不为零，使用exp来保证A始终大于0，指数部分为|math.cos(alpha-beta)|，越小越好，（也即横截面积越小越好）
    A = D ** 2 * m.exp(abs(m.cos(alpha - beta)))

    vx_a = v * m.cos(alpha) - u * m.cos(beta)
    vy_a = v * m.sin(alpha) - u * m.sin(beta)
    va = m.sqrt(vx_a ** 2 + vy_a ** 2)
    # 外界因素影响,俯冲角度alpha、飞行速度V、风速u、风向beta
    # 也即目标函数
    F = 0.5*(rho**2)*(va**2)*C*A
    return F
# 先用梯度算法找到最佳点，在通过恒定的dv和dalpha去计算在300以前能改变多少值。
def grad_descend(v_init,alpha_init,u,beta,lr,n):
    for _ in range(n):
        dv = 2*v_init
        dalpha = v_init**2*m.exp(abs(m.cos(alpha_init - beta))*(-abs(m.sin(alpha_init-beta))))
        v = v_init - lr*dv
        alpha =alpha_init - lr*dalpha

        v = max(min(v,400/3.6),300/3.6)
        alpha = max(min(alpha,m.pi/2),0)

        if  object_func(v,alpha,u,beta) < object_func(v_init,alpha_init,u,beta):
            break
    return v,alpha

n=1000
lr = 0.0001
v_opt,alpha_opt = grad_descend(v,alpha,u,beta,lr,n)
v_opt_kmh = v_opt * 3.6
alpha_opt_deg = np.degrees(alpha_opt)
print(f"Optimal flight speed: {v_opt_kmh:.2f} km/h")
print(f"Optimal dive angle: {alpha_opt_deg:.2f} degrees")
