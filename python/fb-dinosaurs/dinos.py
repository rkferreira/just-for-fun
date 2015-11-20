#!/usr/bin/python

import re
from operator import itemgetter, attrgetter, methodcaller
from math import *

GRAV=9.8

files = [ 'dataset1.csv', 'dataset2.csv' ]
res   = [ None, None]

def calcSpeed(leg, stride):
	speed = ((stride / leg) - 1) * (sqrt(leg * GRAV))
	return speed


def concatFiles(arr01, arr02):
	#concat 02 in 01
	res = []
	for idx, i in enumerate(arr01):
		res.append(None)
		tgt = i.split(",")
		for idx2, j in enumerate(arr02):
			tgt2 = j.split(",")
			if tgt[0] == tgt2[0]:
				res[idx] = tgt + tgt2
				break

	return res
			


def readFile(f):
	fd = open(f, 'r')
	txt = fd.readlines()
	fd.close()
	return txt


def isBipedal(arr):
	pattern = re.compile("bipedal")
	for idx, i in enumerate(arr):
		if pattern.search(i):
			return True
	return False


### MAIN ###

for idx, i in enumerate(files):
	res[idx] = readFile(i)

data = concatFiles(res[0], res[1])

bipedals = []
for idx, i in enumerate(data):
	if isBipedal(i):
		sp = calcSpeed(float(i[1]), float(i[4]))
		i.append(sp)
		bipedals = bipedals + [i]

final = sorted(bipedals, key=itemgetter(6), reverse=True)
for idx, i in enumerate(final):
	print i[0]
