#!/usr/bin/python3.5

import random, sys, time

def gnome(a):
	i = 1
	j = 2
	while i < len(a):
		if i == 0 or a[i] >= a[i-1]:
			i = j
			j += 1
		else:
			a[i], a[i-1] = a[i-1], a[i]
			i -= 1

def gnome2(a):
	i = 1
	while i < len(a):
		if i == 0 or a[i] >= a[i-1]:
			i += 1
		else:
			a[i], a[i-1] = a[i-1], a[i]
			i -= 1

size = int(sys.argv[1])
test = [] #list(range(size))
#random.shuffle(test)
for i in range(size):
	test.append(random.randrange(size))

print(test)
gnome(test)
print(test)
