#!/usr/bin/python

import sys, os, string

begin = '0123456789101112131415'


def getDigit(pos=None, data=None):
	llist = list(data)
	return llist[pos]


print getDigit(1, begin)
print getDigit(5, begin)
print getDigit(13, begin)
print getDigit(19, begin)
