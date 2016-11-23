class Heap:
	def __init__(self):
		self.heap = []

	def empty(self):
		return not len(self.heap)
	def size(self):
		return len(self.heap)

	def put(self, key, item):
		self.heap.append({'key':key, 'item':item})
		Heap.bubbleup(self.heap)

	def get(self):
		if len(self.heap):
			a, end = self.heap, len(self.heap)-1

			a[0], a[end] = a[end], a[0]

			Heap.bubbledown(a, 0, end-1)

			return a.pop()

	def top(self):
		if len(self.heap):
			return self.heap[0]

	@staticmethod
	def bubbleup(a):
		child = len(a)-1
		parent = (child-1)//2

		while parent >= 0:
			if a[parent]['key'] > a[child]['key']:
				a[parent], a[child] = a[child], a[parent]
				child = parent
				parent = (child-1)//2
			else:
				return

	@staticmethod
	def bubbledown(a, begin, end):
		parent = begin
		child = parent * 2 + 1

		while child <= end:
			if (child + 1 <= end) and (a[child]['key'] > a[child + 1]['key']):
				child += 1

			if a[parent]['key'] > a[child]['key']:
				a[parent], a[child] = a[child], a[parent]
				parent = child
				child = parent * 2 + 1
			else:
				return

