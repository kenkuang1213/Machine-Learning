import sys
import random
import re
import numpy


def transDataToInt(datas):
    for i in range(0, len(datas)):
        datas[i] = datas[i][0:5]
        for j in range(0, 4):
            datas[i][j] = float(datas[i][j])
        datas[i][4] = int(datas[i][4])
    return datas


def checkErrors(datas, w):
    errors = 0
    for data in datas:
        x = data[0:4]
        y = data[4]
        x.insert(0, 1)
        if (numpy.dot(x, w) > 0 and y < 0) or (numpy.dot(x, w) <= 0 and y > 0):
            errors += 1
    return errors


datas = [re.split('\s|\t1', line) for line in open('data.dat', 'r')]
datas = transDataToInt(datas)
testDatas = [re.split('\s|\t1', line) for line in open('data_test.dat', 'r')]
testDatas = transDataToInt(testDatas)
w = [0.0, 0.0, 0.0, 0.0, 0.0]

TotalErrorRate = 0

for i in range(0, 200):
    change = True
    ranDatas = datas
    random.shuffle(ranDatas)
    w = [0.0, 0.0, 0.0, 0.0, 0.0]
    updates = 0
    wErrors = sys.maxint
    while updates <= 50:
        for data in ranDatas:
            x = data[0:4]
            x.insert(0, 1)
            y = data[4]
            if (numpy.dot(x, w) > 0 and y < 0) or (numpy.dot(x, w) <= 0 and y > 0):
                updates += 1
                if(updates > 49):
                    break
                wt = [w[k] + (x[k] * y) for k in range(0, len(x))]
                temp = checkErrors(testDatas, wt)
                if(temp < wErrors):
                    w = wt
                    wErrors = temp

    TotalErrorRate += float(wErrors) / len(testDatas)
print("avg Error Rate " + str(TotalErrorRate / 2000))
