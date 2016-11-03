#!/usr/bin/python3

import random
import sys
import time

def shell(a):
	g = len(a) // 2
	while g > 0:
		for i in range(g, len(a)):
			t = a[i]
			k = i
			for j in range(i,0,-g):
				if t < a[j-g]:
					a[j] = a[j-g]
					k -= g
				else:
					break
			a[k] = t
		g //= 2

size = int(sys.argv[1])
test = [] #list(range(size))
#random.shuffle(test)
for i in range(size):
	test.append(random.randrange(size))
	
if size < 32: print(test)

begin = time.time()
shell(test)
end = time.time()

if size < 32: print(test)
print("Micro Elapsed: ", int(round((end - begin) * 1000000)))







