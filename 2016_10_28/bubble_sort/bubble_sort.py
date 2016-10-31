#!/usr/bin/python3

import random

def bubble_sort(array):
	for i in range(len(array)):
		for j in range(1, len(array) - i):
			if array[j] < array[j - 1]:
				array[j], array[j - 1] = array[j - 1], array[j]
			#print(array)









test = []
for i in range(20):
	test.append(i)

random.shuffle(test)

print(test)
bubble_sort(test)
print(test)
























