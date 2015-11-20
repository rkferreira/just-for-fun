#!/usr/bin/python

a = [ 1, 2, 3, 4 , 5 ]

def b():
	for idx, i in enumerate(a):
		if idx == 1:
			return idx


print b()
