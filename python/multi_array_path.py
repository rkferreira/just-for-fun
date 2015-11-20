#!/usr/bin/python


matrix = [  ['A','B','C','E'], ['S','F','C','S'],['A','D','E','E'] ]
word_path = 'EECFS'
list_word = list(word_path)

def findElement(pos=None, start=None, matrix_min=[0,0], matrix_max=None, known_path=None):
	print "\n\nStarting findElement"
	print "POS " + str(pos)
	print "start " + str(start)
	print "matrix_min " + str(matrix_min)
	print "matrix_max " + str(matrix_max)
	print "known_path " + str(known_path)
	if known_path is None:
		print "known_path is NONE"
		#First round, find what you want
		
		found = 0
		known_path = []
		for idx1, i in enumerate(matrix):
			if found: break
			for idx2, j in enumerate(i):
				if ( list_word[pos] == j ):
					start = [idx1, idx2]
					known_path.append(start)
					print "1 Current value of known_path " + str(known_path)
					known_path.append( findElement(pos+1, start, matrix_min, matrix_max, known_path) )
					if len(known_path) >= len(list_word):
						found = 1
						break
					else:
						found = 0
		return known_path
					


	else:
		#We already have some elements, be cafeful
		limit = getBoundaries(start, matrix_max)
		found = 0
		for idx1, i in enumerate(matrix):
			if found: break
			for idx2, j in enumerate(i):
				if found: break
				if (idx1 >= limit[0] and idx1 <= limit[2]) and (idx2 >= limit[1] and idx2 <= limit[3]):
					if (idx1 == start[0]) or (idx2 == start[1]):
						if ( list_word[pos] == j ):
							tmp = [idx1, idx2]
							if (matchLists(known_path, tmp)):
								print "nothing to do"
							else:
								start = [idx1, idx2]
								print "2 start " + str(start)
								known_path.append(start)
								print "2 Current value of known_path " + str(known_path)
								print "pos+1 " + str(pos+1)
								print "len " + str(len(list_word))
								if pos+1 < len(list_word):
									print "opening a new recursion"
									found = 1
									known_path.append( findElement(pos+1, start, matrix_min ,matrix_max, known_path) )
									if len(known_path) >= pos+1:
										found = 1
									break
								else:
									print "pos is now " + str(pos)
									print "len " + str(len(list_word))
									break
		return known_path
								
				


def getBoundaries(value=None, maxvalue=None):
	print "Starting getBoundaries"
	print "value " + str(value)
	print "maxvalue " + str(maxvalue)
	rMin = 0
	rMax = 0
	cMin = 0
	cMax = 0

	if value[0] == 0:
		rMin = 0
		rMax = 1
	else:
		if (value[0] - 1 >= 0):
			rMin = value[0] - 1
		if (value[0] + 1 < maxvalue[0]):
			rMax = value[0] + 1
		else:
			rMax = value[0]

	if value[1] == 0:
		cMin = 0
		cMax = 1
	else:
		if (value[1] - 1 >= 0):
			cMin = value[1] - 1
		if (value[1] + 1 < maxvalue[1]):
			cMax = value[1] + 1
		else:
			cMax = value[1]

	print rMin, cMin, rMax, cMax
	return [rMin, cMin, rMax, cMax]



def matchLists(list1=None, list2=None):
	print "Starting matchLists"
	print "list1 " + str(list1)
	print "list2 " + str(list2)
	for idx1, i in enumerate(list1):
		if i == list2:
			print "Math!"
			return True

	print "no Match!"
	return False



minmat = [0,0]
maxr   = len(matrix)
maxc   = len(matrix[0])
maxmat = [maxr, maxc]

print "\n\nfinal Result"
print "\n\nLALALALALLALAL " + str ( findElement(0, None, minmat, maxmat, None) )
print "\n\ndone"
