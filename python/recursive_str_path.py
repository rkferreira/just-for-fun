#!/usr/bin/python

import os, sys, string

begin = [  ['A', 'B', 'C', 'E'], ['S','F','C','S'],['A','D','E','E'] ]
word = 'ASA'
#word = 'BCCED'
#word = 'ACCED'

listWord = list(word)

maxrow = len(begin)
maxcol = len(begin[0])
maxval = [maxrow, maxcol]


def findCoordinates(pos=None, start=None, maxval=None):
	lcoord = []

	print "Begin:"
	print lcoord

	if start is not None:
		print "start isnt None"
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
		for idx1, k in enumerate( begin ):
			print k
			for idx2, j in enumerate( k ):
				print j
				print idx1
				print idx2
				if (idx1 >= rMin and idx1 < rMax):
					if (idx2 >= cMin and idx2 < cMax):
						if (j == listWord[pos]):
							print "FOUND CHAR"
							print listWord[pos]
							start = [idx1, idx2]
							print "Start1:"
							print start
							print "pos " + str(pos)
							if ( pos+1 < len(listWord) ):
								print "Dentro do POS 1"
								lcoord = [idx1, idx2] + findCoordinates(pos+1, start, maxval)
							else:
								lcoord = [idx1, idx2]
							a = a + 1

	else:
		print "Start is None"
		a = 0
		for idx1, i in enumerate(begin):
			print i
			print idx1
			for idx2, j in enumerate(i):
				print j
				print idx2
				if (j == listWord[pos]):
					print "FOUND CHAR"
					print listWord[pos]
					start = [idx1, idx2]
					print "Start"
					print start
					print "pos " + str(pos)
					if ( pos+1 < len(listWord) ):
						print "Dentro do POS 2"
						lcoord = [idx1, idx2] + findCoordinates(pos+1, start, maxval)
					else:
						lcoord = [idx1, idx2]
					a = a + 1
	
	print "final lcoord"
	print lcoord
	return lcoord


print "Final result"
a = findCoordinates(0, None, maxval)
print a
