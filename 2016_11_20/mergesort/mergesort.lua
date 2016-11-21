#!/usr/bin/lua

function merge(left, right)
	local i = 1
	local j = 1
	local m = {}
	while i <= #left and j <= #right do
		if left[i] <= right[j] then
			table.insert(m, left[i])
			i = i + 1
		else
			table.insert(m, right[j])
			j = j + 1
		end
	end
	while i <= #left do
		table.insert(m, left[i])
		i = i + 1
	end
	while j <= #right do
		table.insert(m, right[j])
		j = j + 1
	end
	return m
end

function mergesort(a)
	if #a <= 1 then return a end
	local mid = math.floor(#a / 2)
	local left = mergesort({table.unpack(a, 1, mid)})
	local right = mergesort({table.unpack(a, mid+1, #a)})
	return merge(left, right)
end

local size = tonumber(arg[1])
local test = {}

for i = 1,size do
	test[i] = i
end

math.randomseed(os.time())
for i = 1,size do
	local r = math.random(i, size)
	test[i], test[r] = test[r], test[i]
end

print(table.concat(test, " "))
local out = mergesort(test)
print(table.concat(out, " "))








