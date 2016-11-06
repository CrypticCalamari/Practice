#!/usr/bin/lua

function partition(a, lo, hi)
	local p = a[lo]
	local i = lo
	local j = hi
	while i < j do
		while i < #a and a[i] <= p do
			i = i + 1
		end
		while a[j] > p do
			j = j - 1
		end
		if i < j then
			a[i], a[j] = a[j], a[i]
		end
	end
	a[lo], a[j] = a[j], a[lo]
	return j
end

function quicksort(a, lo, hi)
	if lo < hi then
		local p = partition(a, lo, hi)
		quicksort(a, lo, p-1)
		quicksort(a, p+1, hi)
	end
end

local size = tonumber(arg[1])
local test = {}
for i = 1, size do
	table.insert(test, i)
end
math.randomseed(os.time())
for i = 1, size do
	local r = math.random(i, size)
	test[i], test[r] = test[r], test[i]
end

print(table.concat(test, " "))
quicksort(test, 1, size)
print(table.concat(test, " "))
