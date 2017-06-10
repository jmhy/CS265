#!/usr/bin/env python
#
# id2.py - reads either standard input or specified file and print out sorted dictionary
#
# Joseph Haggerty

import sys

argc = len( sys.argv )

if argc == 1:
	input = sys.stdin.readlines()
elif argc == 2:
	input = file(sys.argv[1], 'r')
else:
	print 'Specify either 0 or 1 files to process'
	quit()

ids = []
names = []

for line in input:
	ids.append(line.split()[0])
	name = line.strip('\n').split()[1:]
	names.append(' '.join(name))

pplDict = dict(zip(ids,names))

for key, value in pplDict.iteritems():
	print key, value
