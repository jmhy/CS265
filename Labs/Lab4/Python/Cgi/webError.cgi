#!/usr/bin/python
# 
# weberror.py - a CGI script that doesn't run, throws an error
# 
#	Kurt Schmidt
# 5/06
#

import sys
sys.stderr = sys.stdout

	#	The server NEEDS to see this line first (if you're sending an HTML file)
	#   We need both of those newlines
print "Content-type: text/plain\n\n";

def writeDoc() :

	a = b	# Here is the ERROR
	print """
<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN'>
<html>
<head>
	<meta http-equiv='content-language' content='en-us'>
	<meta http-equiv='content-type' content='text/html; charset=iso-8859-1'>
	<meta name='Author' content='Your own name, please'>
	<title>Quick CGI Example</title>
</head>
<body>"""

	print "<h1>My first CGI script in Python</h1>"

	print """</body>
	</html>
	"""
 
writeDoc()

