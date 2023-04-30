import random
import answer1

# L与h0.vx间的关系
with open('output-L.txt','w') as f:
    for _ in range(100):
        h = random.randint(300,800)
        vx = random.randint(300,400)/3.6
        L,d = answer1.calc_L(h,vx)
        f.write(f'{h} {vx} {L}\n')


