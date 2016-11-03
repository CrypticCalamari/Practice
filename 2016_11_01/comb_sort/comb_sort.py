#!/usr/bin/python3

import random

def comb(a):
	swap = True
	g = len(a)
	while g > 1 or swap:
		swap = False
		g = max(1,int(g/1.3))
		for i in range(len(a)-g):
			if a[i] > a[i+g]:
				a[i],a[i+g] = a[i+g],a[i]
				swap = True

test = list(range(20))
random.shuffle(test)
print(test)
comb(test)
print(test)
