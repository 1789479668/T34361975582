import math
# 设置参数
g = 9.8     # 重力加速度
rho = 1.29   # 空气密度kg/m^3，ρ
C = 0.5    # 风阻系数，球体为0.5
m = 5     # 物资质量kg
r = 0.08    # 物资半径m
A = math.pi * (r ** 2)    # 横截面积m^2

#目标点坐标
x_target = 10000
y_target = 0
#范围限制
L_min = 1000
L_max = 3000
H0_min = 300
H0_max = 800
alpha_min = 0.1
alpha_max = math.pi/2

#设置遍历步长
step_h = 1
step_alpha = 0.1
dt = 0.01

#速度
v0 = 300/3.6    # 飞行速度
u0 = 900/3.6    # 发射速度
vf = 6          # 风速
beta = 0        # 风速与vx的夹角
v = v0 + u0     # 因为必然同向，故直接相加

def calc_L(v,vf,beta,H0,alpha):
    # 初始时间
    t = 0
    # 初始位置
    x = 0
    y = H0
    #作速度修正
    vx = v*math.cos(alpha) - vf*math.cos(beta)
    vy = -v*math.sin(alpha) - vf*math.cos(beta)


    while y>0:
        v = math.sqrt(vx**2 + vy**2)
        # 计算vx与v的夹角θ
        theta = math.acos(vx/v)
        # 计算空气阻力以及各方向的加速度
        F_air_resistance = 0.5 * rho * v ** 2 * C * A
        a_y = -g + F_air_resistance*math.sin(theta) / m
        a_x = -F_air_resistance*math.cos(theta)/m
        # 根据欧拉法计算下一时刻的速度和位移
        vy = vy + a_y * dt
        y = y + vy * dt
        vx = vx + a_x * dt
        x = x + vx * dt
        # 更新时间
        t = t + dt
    L = math.sqrt(x**2 + H0**2)
    return L,x

for H0 in range(H0_min,H0_max,step_h):
    for alpha in range(int(alpha_min*10),int(alpha_max*10),int(step_alpha*10)):
        alpha = alpha/10
        L,x = calc_L(v,vf,beta,H0,alpha)
        if L >= L_min and L <= L_max and 10000 -(800-H0)/math.tan(alpha) <= x <= 10000 -(800-H0)/math.tan(alpha):
            optimize_H0 = H0
            optimize_alpha = alpha
            print(optimize_H0,optimize_alpha)
