#!/usr/bin/python
#

import sys

def printHead() :
	"""print out an HTML header"""

		# the handshaking.  Need BOTH newlines.  Hmmm.  Actually, only one,
		#		since print will send one too
	print "Content-type: text/html\n"
	print """<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN'>
<html>
<head>
	<meta http-equiv='content-language' content='en-us'>
	<meta http-equiv='content-type' content='text/html; charset=iso-8859-1'>
	<meta name='Author' content='Kurt Schmidt'>
	<title>Quick CGI Example</title>
</head>
<body>"""

def printTail() :
	"""print the closing HTML tags"""

	print """</body>
</html>
"""

# On to the actual file

printHead()

print "<h1>Result of a POST operation</h1>\n";

print """<p>This is how a CGI process gets the data as a result of a POST
operation.  All of the form data is read from standard input.</p>"""

for l in sys.stdin :
	print l.rstrip() + "<br>"		# note that the newlines are there

printTail()

