#!/usr/bin/python3

import random, sys, time

def selection(a):
	for i in range(len(a)):
		min = a[i]
		k = i
		for j in range(i, len(a)):
			if a[j] < min:
				min = a[j]
				k = j
		a[i], a[k] = a[k], a[i]

size = int(sys.argv[1])
test = [] #list(range(size))
#random.shuffle(test)
for i in range(size):
	test.append(random.randrange(size))

print(test)
selection(test)
print(test)
