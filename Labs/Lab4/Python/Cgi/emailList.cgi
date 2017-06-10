#!/usr/bin/python
# emailList.cgi - Takes a list of email addresses, 1 per line, and joins
#	 them into a single line, comma-separated
#
#		Written at the request of Andrea
#
# Kurt Schmidt
# 4/08
#

import sys
	# for debugging
sys.stderr = sys.stdout

import cgi

def printHead( ) :
  """print out an HTML header, up to (and including) the <body> tag
    INPUT: None"""

  print '''Content-type: text/html

<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN'>
<html>
<head>
  <meta http-equiv='content-language' content='en-us'>
  <meta http-equiv='content-type' content='text/html; charset=iso-8859-1'>
  <title>Address Squisher</title>
  <meta name='Author' content='Kurt Schmidt'>
  <meta name='Publisher' content='Drexel University'>
  <meta HTTP-EQUIV='Expires' content='no-expire'>
  <meta name='Description' content='utility'>
  <meta name='Audience' content='Andrea'>
  <link rel='shortcut icon' type='image/gif'
    href='http://www.cs.drexel.edu/~kschmidt/images/drexel.gif'></link>
</head>

<body style='background-image:
url(http://www.cs.drexel.edu/~kschmidt/images/gray_witch_on_broom.gif);
background-repeat: repeat; background-attachment: fixed' text='#330099'>

<font size='+2'>

<h1> Email List to Single Line w/Comma Converter </h1>
<p> Just for Andrea </p>
</font>

'''


def printTail() :
  '''finishes up HTML doc'''

  print '</body>\n</html>'

 
form = cgi.FieldStorage()


def printForm() :
	'''prints the blank form'''

	print '''
<form action='/~kschmidt/cgi-bin/Python/emailList.cgi'
	method='post' enctype='multipart/form-data'> 

	<p>  Paste the email addresses here (one per line, please), then hit the
	button, below: </p>

	<textarea name='email_list' rows=40 cols=60></textarea>

	<p> <input type='submit' value='Not This Button!'> </p>

</form> '''


def parseForm() :
	'''parses out fields, returns results'''

	s = form[ 'email_list' ].value
	s = s.strip()
	s = s.replace( '\r', '' )
	s = s.replace( '\n', ', ' )

	print '''
	<p> Here they are, in a single line.  Just click in there, hit
	<nobr><i>ctrl</i>-a</nobr> to select all, then copy. </p>
	'''

	print "<textarea name='output' rows='20' cols='80'>"
	print s
	print "</textarea>"

	print '''\n<p> I know, it looks like multiple lines.  But, it copies out of
Firefox just fine, and <i>should</i> paste okay.  Give it a try, w/just a few
addresses </p>'''

	print "<hr width='100%'>"

	#print "<input type='text' name='out' value='" + s + "'/>"



def main( args = sys.argv ) :
	
	printHead()

	if form :	# form called itself
		parseForm() 
	
	printForm() 
	
	printTail()


if __name__ == '__main__' :
	main()

