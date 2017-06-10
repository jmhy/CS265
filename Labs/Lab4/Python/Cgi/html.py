#!/usr/bin/python
#


def printHead( title="Untitle" ) :
	"""print out an HTML header, up to (and including) the <body> tag
		INPUT: title to use, as string"""

	print '''Content-type: text/html

<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN'>
<html>
<head>
  <meta http-equiv='content-language' content='en-us'>
  <meta http-equiv='content-type' content='text/html; charset=iso-8859-1'>
  <title>CGI Examples</title>
  <Meta name="Author" content="Kurt Schmidt">
  <Meta name="Publisher" content="Drexel University">
  <Meta HTTP-EQUIV="Expires" content="no-expire">
  <Meta name="Description" content="CGI example">
  <Meta name="Pagetype" content="Example">
  <Meta name="Audience" content="All">
  <link rel='shortcut icon' type='image/gif'
    href='/~kschmidt/images/drexel.gif'></link>
</head>

<body>'''

def printTail() :
	'''finishes up HTML doc'''

	print '</body>\n</html>'

def main() :
	'''Just testing'''

	printHead( 'Test' )
	printTail()

if __name__ == '__main__' :
	main()
