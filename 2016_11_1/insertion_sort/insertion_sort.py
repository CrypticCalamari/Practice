#!/usr/bin/python3

import random

# Simpler, but more elegant, just with more swaps
def insertion(a):
	for i in range(len(a)):
		for j in range(i, 0, -1):
			if a[j] < a[j-1]:
				a[j],a[j-1] = a[j-1],a[j]
			else:
				break

# More efficient; fewer swaps; slightly less elegant
def insertion2(a):
	for i in range(len(a)):
		t = a[i]
		k = i
		for j in range(i,0,-1):
			if t < a[j-1]:
				a[j] = a[j-1]
				k = j-1
			else:
				break
		a[k] = t

test = list(range(20))
random.shuffle(test)
print("Insertion sort test: slower yet more elegant")
print(test)
insertion(test)
print(test)

random.shuffle(test)
print("Insertion sort test: fewer swaps")
print(test)
insertion2(test)
print(test)
