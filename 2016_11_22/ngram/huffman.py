#!/usr/bin/python3.5

import Heap
import queue, sys

def unigram_count(t):
	out = dict()
	for i in t:
		if i in out:
			out[i] += 1
		else:
			out[i] = 1
	return out

t = sys.argv[1]
out = unigram_count(t)
pq = Heap.Heap()
for i in out:
	print(out[i], ":", i)
	pq.put(out[i], i)

while pq.size() > 1:
	t1 = pq.get()
	t2 = pq.get()
	k = t1['key'] + t2['key']
	pq.put(k, [t1, t2])

print(pq.get())









