#!/usr/bin/python
#

import os

def printHead() :
	"""print out an HTML header"""

	print "Content-type: text/html\n\n"
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

# Some security stuff here

os.environ["SERVER_NAME"] = "(Hidden for security purposes)"
os.environ["SERVER_ADMIN"] = "(Hidden for security purposes)"
os.environ["SCRIPT_FILENAME"] = "(Hidden for security purposes)"
os.environ["SERVER_SOFTWARE"] = "(Hidden for security purposes)"
os.environ["SERVER_PORT"] = "(Hidden for security purposes)"
os.environ["SERVER_SIGNATURE"] = \
	"Apache-AdvancedExtranetServer (Complete info hidden)"
os.environ["PATH"] = "(Hidden for security purposes)"
os.environ["SERVER_ADDR"] = "(Hidden for security purposes)"
os.environ["DOCUMENT_ROOT"] = "(Hidden for security purposes)"

# On to the actual file

printHead()

print "<h1>QUERY_STRING, result of a GET</h1>\n";

print """<p>This is how a CGI process gets the data as a result of a GET
operation.  All of the form data is in the QUERY_STRING environment
variable, and can be parsed out from there.</p>"""

print "<table><tbody>"

	# let's look at all of the fields:
for field in os.environ.keys() :
	if field == "QUERY_STRING" :
		print "\t<tr>\n\t\t<th><font color='red'>" + field + "</font></th>"
	else :
		print "\t<tr>\n\t\t<th>" + field + "</th>"
	print "\t\t<td>" + str( os.environ[field] ) + "</td></tr>"

print "\n<hr>\n"

print "<h2>We'll parse QUERY_STRING:</h2>\n"

pairs = os.environ["QUERY_STRING"].split( "&" )

print "<table>"

for p in pairs :
	print "<tr>"
	name, val = p.split( '=' )
	print "<th>%s</th><td>%s</td>" % (name, val)
	print "</tr>"
	
print "</table>"

print "</tbody></table>"

printTail()

