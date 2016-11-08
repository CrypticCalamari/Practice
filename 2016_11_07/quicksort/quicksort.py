#!/usr/bin/python3

import random, sys, time

def partition(a, lo, hi):
	p = a[lo]
	i = lo
	j = hi
	if i < j:
		while i < len(a) and a[i] <= p:
			i += 1
		while a[j] > p:
			j -= 1
		if i < j:
			a[i], a[j] = a[j], a[i]
	a[lo], a[j] = a[j], a[lo]
	return j

def quicksort(a, lo, hi):
	if lo < hi:
		p = partition(a, lo, hi)
		quicksort(a, lo, p-1)
		quicksort(a, p+1, hi)


