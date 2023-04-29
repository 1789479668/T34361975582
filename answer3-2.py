import numpy as np
def objective_function(v, theta, w, phi, a, b, c, d):
    return a * v**2 + b * theta**2 + c * w**2 + d * phi**2
def gradient_descent(v_init, theta_init, w_init, phi_init, a, b, c, d, lr, max_iter):
    v = v_init
    theta = theta_init
    w = w_init
    phi = phi_init
    for _ in range(max_iter):
        dv = 2 * a * v
        dtheta = 2 * b * theta
        dw = 2 * c * w
        dphi = 2 * d * phi
        v -= lr * dv
        theta -= lr * dtheta
        w -= lr * dw
        phi -= lr * dphi

        if objective_function(v, theta, w, phi, a, b, c, d) < 1e-6:
            break
    return v, theta, w, phi
# 初始化参数
v_init = 300 / 3.6
theta_init = np.radians(45)
w_init = 6
phi_init = np.radians()
a, b, c, d = 1, 1, 1, 1
lr = 0.001
max_iter = 1000
# 执行梯度下降
v_opt, theta_opt, w_opt, phi_opt = gradient_descent(v_init, theta_init, w_init, phi_init, a, b, c, d, lr, max_iter)
# 将速度和角度转换回对应的单位
v_opt_kmh = v_opt * 3.6
theta_opt_deg = np.degrees(theta_opt)
print(f"Optimal flight speed: {v_opt_kmh:.2f} km/h")
print(f"Optimal dive angle: {theta_opt_deg:.2f} degrees")
print(f"Optimal wind speed: {w_opt:.2f} m/s")
print(f"Optimal wind direction: {phi_opt:.2f} radians")