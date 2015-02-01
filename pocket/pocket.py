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


def checkErrors(Datas, w):
    errors = 0
    for data in Datas:
        x = data[0:4]
        y = data[4]
        x.insert(0, 1)
        if (numpy.dot(x, w) > 0 and y < 0) or (numpy.dot(x, w) <= 0 and y > 0):
            errors += 1
    return errors


testNum = 20

datas = [re.split('\s|\t1', line) for line in open('hw1_18_train.dat', 'r')]
datas = transDataToInt(datas)
testDatas = [re.split('\s|\t1', line) for line in open('hw1_18_test.dat', 'r')]
testDatas = transDataToInt(testDatas)


TotalErrorRate = 0.0

for i in range(0, testNum):
    change = True
    ranDatas = datas
    random.shuffle(ranDatas)
    w = [0.0, 0.0, 0.0, 0.0, 0.0]
    pockW = w
    updates = 0
    wErrors = checkErrors(datas, w)
    while updates < 50:
        for data in ranDatas:
            x = data[0:4]
            x.insert(0, 1)
            y = data[4]
            if (numpy.dot(x, w) > 0 and y < 0) or (numpy.dot(x, w) <= 0 and y > 0):
                updates += 1
                w = [w[k] + (x[k] * y) for k in range(0, len(x))]
                temp = checkErrors(ranDatas, w)
                if(temp < wErrors):
                    pockW = w
                    wErrors = temp
    TotalErrorRate += float(checkErrors(testDatas, w)
                            ) / float(len(testDatas))
    # TotalErrorRate += float(wErrors) / len(testDatas)
print("avg Error Rate " + str(TotalErrorRate / testNum))
