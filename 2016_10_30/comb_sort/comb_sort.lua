#!/usr/bin/lua

function comb(a)
	local c = 0
	local gap = #a
	local swaps = true
	while gap > 1 or swaps do
		gap = math.max(1, math.floor(gap / 1.3))
		swaps = false
		for i = 1, #a - gap do
			c = c + 1
			j = i + gap
			if a[i] > a[j] then
				a[i], a[j] = a[j], a[i]
				swaps = true
			end
		end
	end
	print("Comparisons: ", c)
end

local size = tonumber(arg[1])
local test = {}
math.randomseed(os.time())
for i = 1, size do test[i] = math.random(0,size) end
print(table.concat(test, " "))
comb(test)
print(table.concat(test, " "))
