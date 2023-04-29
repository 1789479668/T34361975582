import math
'''
km/h = m/s *3.6
'''
# 设置参数
g = 9.8     # 重力加速度
rho = 1.29   # 空气密度kg/m^3，ρ
C = 0.5    # 风阻系数，球体为0.5
m = 5     # 物资质量kg
r = 0.08    # 物资半径m
A = math.pi * (r ** 2)    # 横截面积m^2

# 初始条件
h0 = 307    # 初始高度m
v0 = 300/3.6     # 飞行速度m/s
u = 600/3.6 #发射速度m/s
alpha = 0.1  # 俯8冲角度
#风速
beta = 0     #风速夹角
vf = 6      # 风速大小m/s

#对初始速度作修正
v = v0 + u
vx = v*math.cos(alpha)
vy = -v*math.sin(alpha) #与y轴方向相反

#时间步长
dt = 0.01

def calc_L(v,alpha,h0):
    # 初始时间
    t = 0
    # 初始位置
    x = 0
    y = h0
    # 算初始相对于地面的速度
    vx = v * math.cos(alpha)
    vy = -v * math.sin(alpha)  # 与y轴方向相反

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
        t = t + dt
    d = x
    L = math.sqrt(x**2 + h0**2)
    return L,d

L,d= calc_L(v,alpha,h0)
print(f"飞行高度h:  {h0}m\n"
      f"飞行速度v: {v0}m/s\n"
      f"发射速度u: {u}m/s\n"
      f"风速vf:    {vf}m/s\n"
      f"vf与vx夹角β:{alpha}rad\n"
      f"物资水平距离:{d}m\n"
      f"投放距离L   {L}m")