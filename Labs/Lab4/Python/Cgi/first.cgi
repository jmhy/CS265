#!/usr/bin/python
# 
# first.cgi - a quick example of writing a simple HTML page from a CGI call
# 
#	Kurt Schmidt
# 5/06
#
 
import sys
sys.stderr = sys.stdout

	#	The server NEEDS to see this line first (if you're sending an HTML file)
	# 	We need both of those newlines
print "Content-type: text/html\n\n"

	# The actual document, that the server sends to the client
print """
<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN'>
<html>
<head>
   <meta http-equiv='content-language' content='en-us'>
   <meta http-equiv='content-type' content='text/html; charset=iso-8859-1'>
   <meta name='Author' content='Your own name, please'>
   <title>Quick CGI Example</title>
</head>
<body>

<h1>My first CGI script in Python</h1>

</body>
</html>
""
