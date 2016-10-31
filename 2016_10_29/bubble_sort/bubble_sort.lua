#!/usr/bin/lua

function bubble_sort(a)
	for x,v in ipairs(a) do
		for y = 2,(#a - x + 1) do
			if a[y] < a[y-1] then
				a[y],a[y-1] = a[y-1],a[y]
			end
		end
	end
end

local test = {};
for i = 1,20 do
	table.insert(test, i)
end

math.randomseed(os.time())
for i = 1,19 do
	local n = math.random(i+1, 20)
	test[i],test[n] = test[n],test[i]
end

print(table.concat(test, " "))
bubble_sort(test)
print(table.concat(test, " "))

