#!/usr/bin/python3

import random

# Simple version, more swaps
def shell(a):
	g = len(a) // 2
	while g > 0:
		for i in range(g,len(a)):
			for j in range(i,0,-g):
				if a[j] < a[j-g]:
					a[j],a[j-g] = a[j-g],a[j]
				else:
					break
		g //= 2

# Fewer swap, more LoC
def shell2(a):
	g = len(a) // 2
	while g > 0:
		for i in range(g,len(a)):
			t = a[i]
			k = i
			for j in range(i,0,-g):
				if t < a[j-g]:
					a[j] = a[j-g]
					k = j-g
				else:
					break
			a[k] = t
		g //= 2

test = list(range(20))
random.shuffle(test)
print(test)
shell(test)
print(test)

random.shuffle(test)
print(test)
shell2(test)
print(test)



