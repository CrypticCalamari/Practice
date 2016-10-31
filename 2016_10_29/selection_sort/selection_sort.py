#!/usr/bin/python3

import random

def selection_sort(a):
	for i in range(len(a)):
		cur_min = i
		for j in range(i+1,len(a)):
			if a[j] < a[cur_min]:
				cur_min = j
		a[i], a[cur_min] = a[cur_min], a[i]
		print(a)

test = []
for i in range(20):
	test.append(i)
random.shuffle(test)

print(test)
selection_sort(test)
print(test)
