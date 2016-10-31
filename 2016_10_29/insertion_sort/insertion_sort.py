#!/usr/bin/python3

import random

def insertion_sort(a):
	for i in range(1,len(a)):
		for j in range(i,0,-1):
			if a[j] < a[j-1]:
				a[j], a[j-1] = a[j-1], a[j]
			else:
				break

test = list(range(20))
random.shuffle(test)
print(test)
insertion_sort(test)
print(test)
