import numpy as np
import random
import anser3pause

beta = np.radians(random.randint(0,90))

v = 400/3.6      # 无人机发射速度，在300~400之间，dv为定值
alpha = np.radians(45)   # 俯冲角度，dalpha为定制
u = 6           # 风速

#v、alpha和b的关系
with open('output3-2.txt','w') as f:
    for beta in np.radians(range(90)):
        n = 1000
        lr = 0.0001
        factor = 0.05
        v_opt, alpha_opt = anser3pause.grad_descend(v, alpha, u, beta, lr, n)
        v_opt_kmh = v_opt * 3.6
        alpha_opt_deg = np.degrees(alpha_opt)
        f.write(f'{v_opt_kmh} {alpha_opt_deg} {np.degrees(beta)}\n')