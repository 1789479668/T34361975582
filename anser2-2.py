import math

# 设置参数
g = 9.8     # 重力加速度
rho = 1.29   # 空气密度kg/m^3，ρ
C = 0.5    # 风阻系数，球体为0.5
m = 5     # 物资质量kg
r = 0.08    # 物资半径m
A = math.pi * (r ** 2)    # 横截面积m^2

# 目标点坐标
x_target = 10000
y_target = 0
# 范围限制
L_min = 1000
L_max = 3000
H0_min = 300
H0_max = 800
alpha_min = 0.01
alpha_max = math.pi/2

# 设置遍历步长
step_h = 1
step_alpha = 0.01
dt = 0.01

# 速度
v0 = 300/3.6    # 飞行速度
u0 = 900/3.6    # 发射速度
vf = 6          # 风速
beta = 0        # 风速与vx的夹角

# 最优解初始化
best_t = float("inf")
best_h0 = 0
best_alpha = 0
best_x1 = 0
best_x2 = 0
best_x3 = 0
best_t1 = 0
best_t2 = 0
best_t3 = 0
best_L = 0

def calc_L(v,vf,beta,H0,alpha):
    # 初始时间
    t3 = 0
    # 初始位置
    x = 0
    y = H0
    #作速度修正
    vx = v*math.cos(alpha)
    vy = -v*math.sin(alpha)


    while y>0:
        # 计算空气阻力以及各方向的加速度
        # 相对于空气的速度
        vx_a = vx - vf * math.cos(beta)
        vy_a = vy - vf * math.sin(beta)
        v_a = math.sqrt(vx_a**2 + vy_a**2)
        # 计算v_a与x正半轴的夹角θ
        theta = math.acos(vx_a/v_a)
        # 计算空气阻力
        F_air_resistance = 0.5 * rho * v_a ** 2 * C * A
        a_y = -g + F_air_resistance*math.sin(theta) / m
        a_x = -F_air_resistance*math.cos(theta)/m
        # 根据欧拉法计算下一时刻的速度和位移
        vy = vy + a_y * dt
        y = y + vy * dt
        vx = vx + a_x * dt
        x = x + vx * dt
        # 更新时间
        t3 = t3 + dt
    L = math.sqrt(x**2 + H0**2)
    return L,t3,x

#遍历搜索，不同h0和alpha的值的影响
for h0 in range(H0_min, H0_max+1, step_h):
    for alpha in range(int(alpha_min*100), int(alpha_max*100)+1, int(step_alpha*100)):
        alpha = alpha/100
        # 计算L和x的大小
        L,t3,x3 = calc_L(v0+u0, vf, beta, h0, alpha)
        # 若L满足1000到3000则继续
        if L_min <= L <= L_max:
            t2 = (800 - h0) / (v0 * math.sin(alpha))
            x2 = (800 - h0) / math.tan(alpha)
            x1 = 10000 - x2 - x3
            # 当x1>0
            if x1 > 0:
                t1 = x1/v0
                t = t1+t2+t3
                if t < best_t:
                    best_t = t
                    best_h0 = h0
                    best_alpha = alpha
                    best_x1 = x1
                    best_x2 = x2
                    best_x3 = x3
                    best_t1 = t1
                    best_t2 = t2
                    best_t3 = t3
                    best_L = L

print("最优解：h0 = %.2f，alpha = %.2f, t = %.2f, L = %.2f" % (best_h0, best_alpha,best_t,best_L))
print("最优解：t1 = %.2f, t2 = %.2f, t3 = %.2f" % (best_t1,best_t2,best_t3))
print("最优解：x1 = %.2f, x2 = %.2f, x3 = %.2f" % (best_x1,best_x2,best_x3))