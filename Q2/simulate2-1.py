import numpy as np

import answer2_1
import random

with open('output-L2.txt','w') as f:
    for _ in range(1000):
        h = random.randint(300,800)
        v = random.randint(300,400)/3.6
        alpha = np.radians(random.randint(0,75))
        L,d = answer2_1.calc_L(v,h,alpha)
        if L is None or np.isnan(L) or np.isinf(L):
            # 如果L无效，则跳过当前循环
            continue
        f.write(f'{v} {h} {np.degrees(alpha)} {L}\n')