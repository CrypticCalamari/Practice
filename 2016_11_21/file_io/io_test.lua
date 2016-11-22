#!/usr/bin/lua

local f = io.open("test.txt")

for i in f:lines(1) do
	if i == "\n" then
		print("NEW LINE")
	else
		print(i)
	end
end















