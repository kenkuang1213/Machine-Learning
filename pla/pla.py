import sys
import random
import re
import numpy

datas = [re.split('\s|\t1', line) for line in open('data.dat', 'r')]
for i in range(0, len(datas)):
    datas[i] = datas[i][0:5]
    for j in range(0, 4):
        datas[i][j] = float(datas[i][j])
    datas[i][4] = int(datas[i][4])

w = [0.0, 0.0, 0.0, 0.0, 0.0]

times = 0
change = True
while change:
    change = False
    for data in datas:
        x = data[0:4]
        # add X0 to Xn(t)
        x.insert(0, 1)
        y = data[4]
        if (numpy.dot(x, w) > 0 and y < 0) or (numpy.dot(x, w) <= 0 and y > 0):
            times += 1
            change = True
            wt = [w[k] + (x[k] * y) for k in range(0, len(x))]
            w = wt

print("naive cycle update " + str(times) + " times")
