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
import subprocess

DATA_DIR = '/home/kschmidt/share/games/fortune'

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
  <meta name='Audience' content='Idle fools'>
  <link rel='shortcut icon' type='image/gif'
    href='http://www.cs.drexel.edu/~kschmidt/images/drexel.gif'></link>
</head>

<body style='background-image:
url(http://www.cs.drexel.edu/~kschmidt/images/gray_witch_on_broom.gif);
background-repeat: repeat; background-attachment: fixed' text='#330099'>


'''


def printTail() :
  '''finishes up HTML doc'''

  print '</body>\n</html>'

 
form = cgi.FieldStorage()


def printForm( s='' ) :
	'''prints the blank form'''

	print '''
	<form action='/~kschmidt/cgi-bin/Python/fortune.cgi'
		method='post' enctype='multipart/form-data'> 

	<h1> Get Your Fortune </h1>
	<p> Please choose your preference type: </p>
	<ul>
		<p>
		<input type='radio' name='type' value='inoff'> Inoffensive only, please
		</input> <br/>
		<input type='radio' name='type' value='all'> Whichever<sup>&dagger;</sup>
		</input> <br/>
		<input type='radio' name='type' value='off'> Offensive
		only<sup>&dagger;</sup> </input> 
		</p>
	</ul>

	<p> <input type='submit' value='Get your Fortune'> </p>


	<textarea name='email_list' rows=20 cols=60 readonly>
	%s
	</textarea>

	<p> <sup>&dagger;</sup>Offensive topics include (but are not limited to):
	race, ethnicity, art, drugs, misandry, religion, sex, misogyny, politics,
	and homophobia.  If you think you might possibly be offended by one of
	these, then <b><font color='red' size='+1'>don't request one</font></b>.
	If ya do, and you <em>are</em> offended, go tell your shrink what an idiot
	you are; <em>I</em> don't want to hear about it. </p>

</form> ''' % s


def parseForm() :
	'''parses out fields, returns results'''

	flag = ''
	if form[ 'type' ].value == 'all' :  #
		flag = '-a'
	elif form[ 'type' ].value == 'off' :  #
		flag = '-o'

	cmd = '/usr/games/fortune ' + flag #+ DATA_DIR
	#cmd = '/bin/echo shit'
	proc = subprocess.Popen( [cmd] )
	#proc = subprocess.Popen( [cmd], stdout=subprocess.PIPE, \
	#			stderr=subprocess.STDOUT )
	out = proc.communicate()[0]  # stdout
	#out = "shit your bed"

	printForm( out )


def main( args = sys.argv ) :
	
	printHead()

	if form :	# form called itself
		parseForm() 
	else :
		printForm() 
	
	printTail()


if __name__ == '__main__' :
	main()

