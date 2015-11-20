#!/usr/bin/python

begin = [2, 3, 4, 2, 6, 2, 5, 1]
window = 3
final = []

for idx1, i in enumerate(begin):
	##print "Begin\n"
	##print "idx1: %s" % idx1
	n1 = None
	n2 = None
	##print "i: %s" % i

	for idx2, j in enumerate( begin[idx1+1:idx1+3] ):
		##print "second for\n"
		##print "j: %s" % j
		if n1:
			n2 = j
		else:
			n1 = j

	##print "first for\n"
	if ( n1 is not None and n2 is not None ):
		res = [i, n1, n2]
		res.sort()
		##print res
		final = final + [ res[2] ]
		##print final


print final
