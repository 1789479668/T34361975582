import numpy as np
import matplotlib.pyplot as plt

# 无人机参数(正方体)
g = 9.8     # 重力加速度
rho = 1.29   # 空气密度kg/m^3，ρ
C = 0.8    # 风阻系数，球体为0.5
M = 50     # 无人机重量
D = 0.4   # 无人机边长

# alpha在0~pi/2，beta没有限制
v = 400/3.6      # 无人机发射速度，在300~400之间，dv为定值
alpha = np.radians(45)   # 俯冲角度，dalpha为定制
u = 6           # 风速
beta = np.radians(45)    # 风向

#俯冲角度alpha与飞行速度V的变化率dalpha、dv为定值
def object_func(v,alpha,u,beta):
    vx_a = v * np.cos(alpha) - u * np.cos(beta)
    vy_a = - v * np.sin(alpha) - u * np.sin(beta)
    va = np.sqrt(vx_a ** 2 + vy_a ** 2)
    # 为阻力不为零，使用exp来保证A始终大于0，指数部分为|np.sin(alpha-beta)|，越小越好，alpha-beta可以反映实际受风向的大小，即反应截面积的大小
    A = D ** 2 *np.sin(alpha-beta)
    # 外界因素影响,俯冲角度alpha、飞行速度V、风速u、风向beta
    # 也即目标函数
    F = 0.5*(rho**2)*(va**2)*C*A
    return F

F_list =[]
# 先用梯度算法找到最佳点，在通过恒定的dv和dalpha去计算在300以前能改变多少值。
def grad_descend(v_init,alpha_init,u,beta,lr,n):
    v = v_init
    alpha = alpha_init
    for _ in range(n):
        dv = 2*v
        # # dalpha = 2*(u * np.cos(beta)*np.sin(alpha)-np.sin(beta)*np.cos(alpha))*abs(np.cos(alpha - beta)) + \
        # #          v**2*abs(np.cos(alpha - beta))*(-np.sin(alpha-beta))
        if np.sin(alpha-beta)>0:
            dalpha = (v**2+u * np.cos(beta)**2+u * np.sin(beta)**2)*np.cos(alpha-beta) - \
                    2*v*(-np.sin(alpha)*u * np.cos(beta)+np.cos(alpha)*u * np.sin(beta))*np.sin(alpha-beta)-\
                    2*v*(np.cos(alpha)*u * np.cos(beta)+np.sin(alpha)*u * np.sin(beta))*np.cos(alpha-beta)
        else:
            dalpha = -(v**2+u * np.cos(beta)**2+u * np.sin(beta)**2)*np.cos(alpha-beta) + \
                    2*v*(-np.sin(alpha)*u * np.cos(beta)+np.cos(alpha)*u * np.sin(beta))*np.sin(alpha-beta)+\
                    2*v*(np.cos(alpha)*u * np.cos(beta)+np.sin(alpha)*u * np.sin(beta))*np.cos(alpha-beta)
        # dv = 2*v*np.cos(alpha)*np.cos(alpha-beta)+2*v*np.sin(alpha-beta)**2-\
        #      2*u * np.cos(beta)*np.cos(alpha)-2*u * np.sin(beta)*np.sin(alpha)*np.sin(alpha-beta)
        # dalpha = -2*v**2*np.sin(alpha-beta)*np.cos(alpha)*np.sin(alpha)+\
        #         2*v*np.cos(alpha)*np.sin(alpha-beta)*(v*np.sin(alpha)-u * np.sin(beta))-\
        #         2*u * np.cos(beta)*v*np.sin(alpha)*np.cos(alpha)
        v = v - lr*dv
        alpha = alpha -lr*dalpha*0.0001

        v = max(min(v,400/3.6),300/3.6)
        # alpha = max(min(alpha,np.radians(90)),0)

        F_list.append(object_func(v,alpha,u,beta))


    plt.plot(range(n),F_list)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Line Chart')
    plt.show()
    return v,alpha

n=1000
lr = 0.0001
v_opt,alpha_opt = grad_descend(v,alpha,u,beta,lr,n)
v_opt_kmh = v_opt * 3.6
alpha_opt_deg = np.degrees(alpha_opt)
print(f"Optimal flight speed: {v_opt_kmh:.2f} km/h")
print(f"Optimal dive angle: {alpha_opt_deg:.2f} degrees")
