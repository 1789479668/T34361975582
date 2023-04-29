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
step_alpha = 0.01
dt = 0.01

#速度
v0 = 300/3.6    # 飞行速度
u0 = 900/3.6    # 发射速度
vf = 6          # 风速
beta = 0        # 风速与vx的夹角

best_L = float("inf")
best_h0 = 0
best_alpha = 0

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

#遍历搜索，不同h0和alpha的值的影响
for h0 in range(H0_min, H0_max+1, step_h):
    for alpha in range(int(alpha_min*100), int(alpha_max*100)+1, int(step_alpha*100)):
        alpha = alpha/100
        # 计算L和x的大小
        L,x = calc_L(v0+u0, vf, beta, h0, alpha)
        # 若L满足1000到3000则继续
        if L >= L_min and L <= L_max:
            # 计算x3，10000-x，即第一阶段的水平位移
            x3 = x_target - x
            # 当x3大于0时才继续下一步
            if x3 > 0:
                if 800 - h0 <= x3 / math.tan(alpha):
                    if L < best_L:
                        best_L = L
                        best_h0 = h0
                        best_alpha = alpha

print("最优解：h0 = %.2f，alpha = %.2f" % (best_h0, best_alpha))
