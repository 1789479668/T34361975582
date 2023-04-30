import numpy as np
'''
km/h = m/s *3.6
alpha都是弧度，acos返回的也是弧度
'''
# 设置参数
g = 9.8     # 重力加速度
rho = 1.29   # 空气密度kg/m^3，ρ
C = 0.5    # 风阻系数，球体为0.5
m = 50     # 物资质量kg
r = 0.20   # 物资半径m
A = np.pi * (r ** 2)    # 横截面积m^2

# 初始条件
h0 = 300    # 初始高度m
vx = 300/3.6     # 水平速度m/s
vf = 5      # 风速大小m/s
alpha = np.pi/2   # 与初始速度夹角，逆时针旋转计，°，同向0，竖直向下math.pi/2，相反math.pi，竖直向上math.pi*3/2，
            # 运动过程中外风方向不变，自己运动的风速改变，单位是弧度

# 时间步长
dt = 0.01

# 计算投放距离
def calc_L(h0, vx):
    # 初始竖直速度为零
    vy0 = 0
    # 初始时间为零
    t = 0
    # 初始位置为无人机位置
    x = 0
    y = h0
    with open('output-F.txt', 'w') as f:
        while y > 0:
            # 计算空气阻力以及各方向的加速度
            # 物资相对于空气的速度
            vx_a = vx - vf*np.cos(alpha)
            vy_a = vy0 - vf*np.sin(alpha)
            v_a = np.sqrt(vx_a ** 2 + vy_a ** 2)
            # 计算v_a与x正半轴的夹角θ
            theta = np.arccos(vx_a/v_a)
            # 由物资相对于空气的速度计算空气阻力
            F_air_resistance = 0.5 * rho * v_a ** 2 * C * A
            a_y = -g + F_air_resistance*np.sin(theta) / m
            a_x = -F_air_resistance*np.cos(theta)/m
            # 根据欧拉法计算下一时刻的速度和位移
            # 由相对于地面的速度计算位移，相对于地面的水平速度vx，相对于地面的竖直速度vy
            vy = vy0 + a_y * dt
            y = y + vy * dt
            vx = vx + a_x * dt
            x = x + vx * dt
            # 更新竖直速度和时间
            vy0 = vy
            t = t + dt

            f.write(f'{F_air_resistance} {np.degrees(theta)} {t}\n')
    d = x
    L = np.sqrt(x**2 + h0**2)
    return L,d

# 测试程序
L,d= calc_L(h0, vx)
print(f"飞行高度h:  {h0}m\n"
      f"飞行速度vx: {vx}m/s\n"
      f"风速vf:    {vf}m/s\n"
      f"vf与vx夹角α:{alpha}rad\n"
      f"物资水平距离:{d}m\n"
      f"投放距离L   {L}m")
