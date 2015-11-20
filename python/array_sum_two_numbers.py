#!/usr/bin/python

import os, sys, string

#Target sum is 15

target = 18
begining = [1, 2, 4, 7, 11, 15]

def findSum(a=None, items=None):
	print a
	print items
	if ( sum(a) == target ):
		print "Found: %s" % (a)
		items = items + 1;
	return items

items=0;
size = len(begining)
for idx, i in enumerate(begining):
	if (items < 2):
		##print str(idx)
		##print str(i)
		##print begining[idx+1]
		##print "ok\n"
		try:
			items = findSum( [i, begining[idx+1]], items  )
		except IndexError:
			continue
