#!/usr/bin/python3

a = 204

print(a)
print(type(a))

f = open('test.out', 'wb')
f.write(a.to_bytes(1, byteorder='big'))
f.close()
