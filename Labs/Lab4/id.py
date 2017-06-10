#!/usr/bin/env python
#
# id.py - reads ids, stores ids and names to a dict and prints the dict sorted by id 
#
# Joseph Haggerty

import sys

argc = len( sys.argv )

if argc != 2:
	print 'Specify exactly one file, the ids file'
	quit()

ids = []
names = []

infile = file(sys.argv[1], 'r')
for line in infile:
	ids.append(line.split()[0])
	name = line.strip('\n').split()[1:]
	names.append(' '.join(name))

pplDict = dict(zip(ids,names))

for key, value in pplDict.iteritems():
	print key, value
