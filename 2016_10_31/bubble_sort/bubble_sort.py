#!/usr/bin/python3

import random

def bubble(a):
	for i in range(len(a)):
		swapped = False
		for j in range(1,len(a)-i):
			if a[j] < a[j-1]:
				swapped = True
				a[j], a[j-1] = a[j-1], a[j]
		if not swapped:
			break
test = list(range(20))
random.shuffle(test)
print(test)
bubble(test)
print(test)
