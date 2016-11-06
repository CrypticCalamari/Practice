#!/usr/bin/lua

function shell(a)
	local g = math.floor(#a/2)
	while g > 0 do
		for i = g,#a do
			local t = a[i]
			local k = i
			for j = i,g+1,-g do
				if t < a[j-g] then
					a[j] = a[j-g]
					k = k - g
				else
					break
				end
			end
			a[k] = t
		end
		g = math.floor(g/2)
	end
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
shell(test)
print(table.concat(test, " "))


