#!/usr/bin/python

import sys, os, string

begin = [  ['A', 'B', 'C', 'E'], ['S','F','C','S'],['A','D','E','E'] ]
#word = 'BCCED'
word = 'ACCED'

#row, col
def findCoordinates(letter=None, start=None, maxval=None):
	lcoord = []

	if start is not None:
		for idx, i in enumerate(start):
			if idx == 0:
				if i == 0:
					rMin = 0
					rMax = 1
				else:
					if ( i - 1 >= 0 ):
						rMin = i - 1
					if ( i + 1 <= maxval[0] ):
						rMax = i + 2
					else:
						rMax = maxval[0]
				
			if idx == 1:
				if i == 0:
					cMin = 0
					cMax = 1
				else:
					if ( i - 1 >= 0 ):
						cMin = i - 1
					if ( i + 1 <=maxval[1] ):
						cMax = i +2
					else:
						cMax = maxval[0]
		a = 0
		print rMin
		print rMax
		print cMin
		print cMax
		for idx1, k in enumerate( begin[rMin:rMax] ):
			print k
			for idx2, j in enumerate( k[cMin:cMax] ):
				print j
				print idx1
				print idx2
				if (j == letter):
					lcoord.append([])
					lcoord[a] = [idx1, idx2] 
					a = a + 1

	else:
		a = 0
		for idx1, i in enumerate(begin):
			for idx2, j in enumerate(i):
				if (j == letter):
					lcoord.append([])	
					lcoord[a] = [idx1, idx2]
					a = a + 1
	print lcoord
	return lcoord



listWord = list(word)

maxrow = len(begin)
maxcol = len(begin[0])
maxval = [maxrow, maxcol]

res = findCoordinates(listWord[0],None, maxval)
print res
start = [0,1]
res = findCoordinates(listWord[1], start, maxval)
print res

got = None
for idx1, i in enumerate(listWord):
	got = findCoordinates(i, got, maxval)
	for idx2, j enumerate(got):
		result
