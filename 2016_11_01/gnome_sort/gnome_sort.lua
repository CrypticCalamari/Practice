#!/usr/bin/lua

-- Stupid Gnome
function gnome(a)
	local i = 2
	while i <= #a do
		if i == 1 or a[i] >= a[i-1] then
			i = i + 1
		else
			a[i],a[i-1] = a[i-1],a[i]
			i = i - 1
		end
	end
end

-- Smart Gnome
function gnome2(a)
	local i = 2
	local j = 3
	while i <= #a do
		if a[i] >= a[i-1] then
			i = j
			j = j + 1
		else
			a[i],a[i-1] = a[i-1],a[i]
			i = i - 1
			if i == 1 then
				i = j
				j = j + 1
			end
		end
	end
end

local size = tonumber(arg[1])
local test = {}
for i = 1,size do
	table.insert(test, i)
end
math.randomseed(os.time())
for i = 1,size do
	local r = math.random(i,size)
	test[i],test[r] = test[r],test[i]
end

print("Stupid gnome")
print(table.concat(test, " "))
gnome(test)
print(table.concat(test, " "))

for i = 1,size do
	local r = math.random(i,size)
	test[i],test[r] = test[r],test[i]
end

print("Smart teleporting gnome")
print(table.concat(test, " "))
gnome2(test)
print(table.concat(test, " "))






