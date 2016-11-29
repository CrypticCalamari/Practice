#!/usr/bin/python3

import random, sys

def mean(series):
	n = len(series)
	m = 0
	for x in series:
		m += x / n
	return m

def moving_mean(series, n):
	m = mean(series[:n])
	mm = []
	mm.append(round(m, 4))
	
	for x in range(n, len(series)):
		m -= series[x-n] / n
		m += series[x] / n
		mm.append(round(m, 4))
		print(round(m,4))
	return mm

s = []
for i in range(50):
	s.append(random.randrange(100))

print(s)
print(round(mean(s[:10]), 4))
print(moving_mean(s, 10))








