#!/usr/bin/python3

import random

def selection(a):
	for i in range(len(a)-1):
		c = i
		for j in range(i+1, len(a)):
			if a[j] < a[c]:
				c = j
		a[i], a[c] = a[c], a[i]

test = list(range(20))
random.shuffle(test)
print(test)
selection(test)
print(test)
