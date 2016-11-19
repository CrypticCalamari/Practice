#!/usr/bin/python3.5

import random, sys

class List:
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail
	def cons(self, data):
		L = List(self.head, self.tail)
		self.head = data
		self.tail = L
		return self
	def car(self):
		return self.head
	def cdr(self):
		return self.tail

size = int(sys.argv[1])
L = List()
L.cons(5).cons(10).cons(20)

for i in range(size):
	L.cons(random.randrange(size))

c = L
while c:
	if c.car():
		print(c.car())
	c = c.cdr()


