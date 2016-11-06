#!/usr/bin/python3

import random, sys, time

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
test = list(range(size))
random.shuffle(test)

print(test)
begin = time.time()
shell(test)
end = time.time()
print(test)
