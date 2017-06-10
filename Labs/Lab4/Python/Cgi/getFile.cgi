#!/usr/bin/python
# 
# getPage.py - a quick example of writing a simple HTML page from a CGI call
# 
#	Kurt Schmidt
# 5/06
#
 
#import os, subprocess

filename = "/home/kschmidt/public_html/cgi-bin/test.input"

	#	The server NEEDS to see this line first (if you're sending an HTML file)
	# 	We need both of those newlines

print "Content-type: text/html\n\n";

print """
<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN'>
<html>
<head>
   <meta http-equiv='content-language' content='en-us'>
   <meta http-equiv='content-type' content='text/html; charset=iso-8859-1'>
   <meta name='Author' content='Your own name, please'>
   <title>Quick CGI Example</title>
</head>
<body> """

print "<h1>Here's the file</h1>"
print "<tt><pre>"

cmd = [ "ls", "-l", "/" ]

## Create output log file
#outFile = "Public/output.log"
#outptr = file(outFile, "w")
#
## Create error log file
#errFile = "Public/error.log"
#errptr = file(errFile, "w")
#
## Call the subprocess using convenience method
#retval = subprocess.call(cmd, 0, None, None, outptr, errptr)

f = open( filename, "r" )

for l in f :
	l = l.strip()
	print l

print "</pre></tt>"

print """</body>
</html>
"""
