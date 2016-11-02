#!/usr/bin/python3

import random

# Simple version without early end in no swap case
def bubble(a):
	for i in range(len(a)):
		for j in range(1, len(a) - i):
			if a[j] < a[j-1]:
				a[j],a[j-1] = a[j-1],a[j]

def bubble2(a):
	for i in range(len(a)):
		swap = False
		for j in range(1, len(a) - i):
			if a[j] < a[j-1]:
				a[j],a[j-1] = a[j-1],a[j]
				swap = True
		if not swap:
			break


test = list(range(20))
random.shuffle(test)
print("Simple version")
print(test)
bubble(test)
print(test)

random.shuffle(test)
print("End early when no swaps.")
print(test)
bubble2(test)
print(test)

