#!/usr/bin/python

import os, sys, string
from array import *

def handleFile(fname=None):
	f = open(fname, 'w')
	f.write("aaaaaaaa\n")
	f.write("bbbbbbbb\n")
	f.close()

def readFile(fname=None):
	f = open(fname, 'r')
	print f.read()
	f.close()

def testArray(arr=None):
	for i in arr:
		print i

def testList(lis=None):
	for i in lis:
		print i


lis = [1, 5, 10, 15, "pizza"]
arr = array('i', [10, 40, 50])

handleFile('a.txt')
readFile('a.txt')
testArray(arr)
testList(lis)
