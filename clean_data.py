import matplotlib.pyplot as pt
import random

pos = []

with open('final-30%.csv', 'r') as f:
    f.readline()
    for s in f:
        o = s.split(",")
        pos.append([float(o[1][:-1]), float(o[0])])

fig = pt.figure()

for poss in pos:
    for posss in pos:
        dis = (poss[0] - posss[0]) ** 2 + (poss[1] - posss[1]) ** 2
        print(dis)
        if dis < 0.00001:
            pos.remove(posss)


for poss in pos:
    pt.scatter(poss[1], poss[0], s=250)

pt.show()
print(len(pos))
with open('final.csv', 'w+') as f:
    for s in pos:
        tr = f'{s[1]},{s[0]}\n'
        f.write(tr)