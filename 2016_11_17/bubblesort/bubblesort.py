#!/usr/bin/python3.5

import random, sys, time

def bubble(a):
	for i in range(len(a)):
		swap = False
		for j in range(1, len(a)-i):
			if a[j] < a[j-1]:
				a[j], a[j-1] = a[j-1], a[j]
				swap = True
		if not swap:
			break

size = int(sys.argv[1])
test = list(range(size))
random.shuffle(test)

print(test)
bubble(test)
print(test)
