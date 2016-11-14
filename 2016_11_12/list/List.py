#!/usr/bin/python3

import random, sys, time

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class List:
	def __init__(self):
		self.begin = None
		self.end = None
	def append(self, x):
		n = Node(x)
		if self.end is None:
			self.begin = n
			self.end = n
		else
			self.end.next = n
			n.prev = self.end
			self.end = n
	def insert(self, i, x):
		if not self.begin:
			self.append(x)
			return
		n = Node(x)
		if i == 0:
			self.begin.prev = n
			n.next = self.begin
			self.begin = n
		elif i > 0:
			c = self.begin
			j = 1
			while j < i and c.next:
				c = c.next
				j += 1
			if c is self.end:
				
			

t = DoublyLinkedList()
for i in range(10):
	t.insert_front(Node(i))

for i in t.iterate():
	print(i)












