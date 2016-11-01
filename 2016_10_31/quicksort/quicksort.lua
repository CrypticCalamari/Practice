#!/usr/bin/lua

function partition(a, lo, hi)
	local p = a[lo]
	local i = lo
	local j = hi

	while true do
		while a[i] < p do
			i = i + 1
		end
		while a[j] > p do
			j = j - 1
		end
		if i >= j then
			return j
		end
		a[i],a[j] = a[j],a[i]
	end
end

function quicksort(a, lo, hi)
	if lo < hi then
		local p = partition(a, lo, hi)
		quicksort(a, lo, p-1)
		quicksort(a, p+1, hi)
	end
end

local test = {}
for i = 1,20 do
	table.insert(test, i)
end

math.randomseed(os.time())
for i = 1, 20 do
	local r = math.random(i,20)
	test[i], test[r] = test[r], test[i]
end

print(table.concat(test, " "))
quicksort(test, 1, #test)
print(table.concat(test, " "))
