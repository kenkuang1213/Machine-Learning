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
		y=float(data[i][4])
		ans = 0
		for j in range(0, len(x)):
			ans += w[j] * x[j]	      
		if (ans > 0 and y < 0) or (ans < 0 and y> 0) or (ans== 0  and y > 0):
			# print(w)
			# print(x)
			# print(y)
			times += 1
			change =True
			w = [w[k] + (x[k] * y)	     for k in range(0, len(x))]
	# change=False
print("naive cycle update " + str(times) + " times")


