import numpy as np

import answer2_1

with open('output3-1.txt','w') as f:
    for v in range(300,400):
        for alpha in np.radians(range(90)):
            L,d = answer2_1.calc_L(v, alpha, 300)
            f.write(f"{v} {np.degrees(alpha)} {d}\n")