from operator import gt, lt

class Heap:
	def __init__(self, min_heap=True):
		self.heap = []
		if min_heap:
			self.op = gt
		else:
			self.op = lt
	def empty(self):
		return not len(self.heap)
	def size(self):
		return len(self.heap)
	def clear(self):
		self.heap = []

	def top(self):
		if len(self.heap):
			return self.heap[0]

	def put(self, key, item):
		self.heap.append([key, item])
		Heap.bubbleup(self.heap, self.op)

	def get(self):
		if len(self.heap):
			a, end = self.heap, len(self.heap)-1
			a[0], a[end] = a[end], a[0]

			Heap.bubbledown(a, 0, end-1, self.op)
			return a.pop()

	@staticmethod
	def bubbleup(a, op):
		child = len(a)-1
		parent = (child-1)//2

		while parent >= 0:
			if op(a[parent][0], a[child][0]):
				a[parent], a[child] = a[child], a[parent]
				child = parent
				parent = (child-1)//2
			else:
				return

	@staticmethod
	def bubbledown(a, begin, end, op):
		parent = begin
		child = parent * 2 + 1

		while child <= end:
			if child + 1 <= end and op(a[child][0], a[child+1][0]):
				child += 1

			if op(a[parent][0], a[child][0]):
				a[parent], a[child] = a[child], a[parent]
				parent = child
				child = parent * 2 + 1
			else:
				return
