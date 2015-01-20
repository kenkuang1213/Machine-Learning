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
avgTimes = 0
weight = 0.5
for i in range(0, 2000):
    tmptimes = 0
    change = True
    ranDatas = datas
    random.shuffle(ranDatas)
    w = [0.0, 0.0, 0.0, 0.0, 0.0]
    while change:
        change = False
        for data in ranDatas:
            x = data[0:4]
            x.insert(0, 1)
            y = data[4]
            if (numpy.dot(x, w) > 0 and y < 0) or (numpy.dot(x, w) <= 0 and y > 0):
                tmptimes += 1
                change = True
                w = [w[k] + weight * (x[k] * y) for k in range(0, len(x))]
    avgTimes += tmptimes
print("random cycle update " + str(avgTimes / 2000) + " times")
