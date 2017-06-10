#!/usr/bin/env python
#
# s1.py - prints student name and their average from students
#
# Joseph Haggerty

import sys

argc = len( sys.argv )

if argc != 2:
	print 'Specify exactly one file, the students file'
	quit()

infile = file(sys.argv[1], 'r')
for line in infile:
	name = line.split()[0]
	scores = line.strip('\n').split()[1:]
	scores = map(int,scores)
	average = sum(scores) / float(len(scores))
	print name, average
