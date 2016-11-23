def merge(left, right):
	i = 0
	j = 0
	m = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			m.append(left[i])
			i += 1
		else:
			m.append(right[j])
			j += 1
	m += left[i:]
	m += right[j:]
	return m

def mergesort(a):
	if len(a) <= 1:
		return a
	mid = len(a) // 2
	left = mergesort(a[:mid])
	right = mergesort(a[mid:])
	return merge(left, right)
