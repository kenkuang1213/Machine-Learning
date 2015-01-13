import sys
import random
import re
            
data = [re.split('\s', line) for line in open('data.dat', 'r')]
w = [0.0, 0.0, 0.0,0.0]

times = 0
	
change = True;
while change:	
            change=False
	for i in range(0, len(data)):
	            x = [float(t) for t in data[i][0:4]]
	            y=int(data[i][4])
	            ans = 0
	            for j in range(0, len(x)):
	                        ans += w[j] * x[j]	      
	            if (ans > 0 and y < 0) or (ans < 0 and y> 0) or (ans== 0  and y > 0):
			print(w)
			print(x)
			times += 1
			change =True
			w = [w[k] + x[k] * float(data[i][4])	     for k in range(0, len(x))]
      change=False

      	             	
print("naive cycle update " + str(times) + " times")
print(w)
avgtimes = 0
for num in range(0, 2000):
            start = random.randint(0, len(data) - 1)
            w = [float(i) for i in data[start][0:4]]
            tmpTimes = 0

            for i in range(start, len(data)):
                        x = [float(t) for t in data[i][0:4]]
                        ans = 0
                        for j in range(0, len(x)):
                                    ans += float(w[j]) * float(x[j])
                        if (ans > 0 and (int(data[i][4])) < 0) or (ans < 0 and (int(data[i][4])) > 0):
                                    tmpTimes += 1
                        w = [w[k] + x[k] * float(data[i][4])
                             for k in range(0, len(x))]
            for i in range(0, start):
                        x = [float(t) for t in data[i][0:4]]
                        ans = 0
                        for j in range(0, len(x)):
                                    ans += float(w[j]) * float(x[j])
                        if (ans > 0 and (int(data[i][4])) < 0) or (ans < 0 and (int(data[i][4])) > 0):
                                    tmpTimes += 1
                                    w = [w[k] + x[k] * float(data[i][4])
                                         for k in range(0, len(x))]

            avgtimes += tmpTimes
print("random cycle update " + str(avgtimes / 2000) + " times")
	