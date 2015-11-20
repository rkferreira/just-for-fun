#!/usr/bin/python

import os, sys, string

target = 15
begining = [1, 2, 4, 5, 7, 10, 11, 15]
begining.sort()

found = 0;
bsize = len(begining)
for idx, i in enumerate(begining):
	if found == 0:
		#for idx2, j in enumerate(begining[idx+1:bsize-1]):
		for idx2, j in enumerate(begining[idx+1:-1]):
			if (i+j == target):
				print "%s + %s" % (i,j)
				found = found + 1;

