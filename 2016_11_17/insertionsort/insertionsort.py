#!/usr/bin/python3.5

import random, sys, time

def insertion(a):
	for i in range(1, len(a)):
		t = a[i]
		k = i
		for j in range(i, 0, -1):
			if t < a[j-1]:
				a[j] = a[j-1]
				k -= 1
			else:
				break
		a[k] = t

size = int(sys.argv[1])
test = [] #list(range(size))
#random.shuffle(test)
for i in range(size):
	test.append(random.randrange(size))

print(test)
insertion(test)
print(test)









