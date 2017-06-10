#!/usr/bin/python
#

import cgi

form = cgi.FieldStorage()	# get access to the form fields

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

printHead()

print "<h1>Hello</h1>\n";

print """<p>Here are the form fields, and their values.  Please note that
this script is indifferent of the method (<tt><b>post</b></tt> or
<tt><b>get</b></tt>); the cgi module handles this for us </p>

<dl>"""


	# let's look at all of the fields:
for field in form.keys() :
	print "\t<dt><b>" + field + "</b></dt>"
	if type( form[field] ) is list :
	  for v in form[field] :
			print "\n\t\t<dd>" + str( v.value ) + "</dd>"
	else :
		print "\n\t\t<dd>" + str( form[field].value ) + "</td>"

print "</dl>\n"

print """<p><b>Note:</b>  The satellite data associated w/a field name
<i>might</i> be a list (if, for example, the fieldname was used multiple
times), so, you might need to check, and iterate over this list, pulling out
each element's <tt>value</tt> attribute.</p>"""

#	# Note the call to an external utility here.
#my $dts = `date + "%D %R"`;
#my ( $date, $time ) = split( /\s+/, $dts );
#my ( $month, $day ) = split( /\//, $date, 2 );
#my ( $hour, $min ) = split( /:/, $time );
#
#if( $day==$bDay && $month==$bMonth )
#{
#	print "\n<p><font size='+2'><b>Happy Birthday!</b></font></p>\n";
#}
#
#print "\n<p>The time is now $hour:$min, and all's well on the",
#	" east wall.</p>\n";

printTail()

