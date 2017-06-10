#!/usr/bin/python
# info.cgi - an example of a script displaying a form that calls this (same)
#	 script, doing simple error checking
#
# Kurt Schmidt
# Aug '06
#
# TODO: Put better errors (output) to user
#

import sys
import cgi

	# this is a handy little move.  You must also make sure that that line
	# 	that prints "Content-type: text/html\n\n" is called before anything
	# 	else happens
	#	Now, stack trace info will show up on your page (ya might need to view
	#		source)
	# There's also a handy module out there, cgitb, just:
	#		import cgitb
	#		cgitb.enable()
	#	but, I haven't played w/it yet.
sys.stderr = sys.stdout

def printHead() :
	"""print out an HTML header"""

	print "Content-type: text/html\n\n"
	print """<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN'>
<html>
<head>
	<meta http-equiv='content-language' content='en-us'>
	<meta http-equiv='content-type' content='text/html; charset=iso-8859-1'>
	<meta name='Author' content='Kurt Schmidt'>
	<title>CGI Lab - info</title>
</head>
<body>
	<style type="text/css">
		input.reqd { background:PaleGoldenRod }
		input.opt { background:white }
	</style>
"""

def printTail() :
	"""print the closing HTML tags"""

	print """</body>
</html>"""

def parseForm( f ) :
	'''Given form f
		performs most of the logic
		Writes form, error msgs, or output to HTML document
	'''

	bFirstCall = True	# is this a fresh form?
	bErrors = False

	fields = {
		'name':'', 
		'street1':'',
		'street2':'',
		'city':'',
		'state':'',
		'zip':'',
		'zip_4':'',
		'area':'',
		'trunk':'',
		'ext':''
		}
	
	if f.has_key( 'name' ) and f['name'].value != '' :
		bFirstCall = False
		fields['name'] = f['name'].value
	else :
		bErrors = True

	if f.has_key( 'street1' ) and f['street1'].value != '' :
		bFirstCall = False
		fields['street1'] = f['street1'].value
	else :
		bErrors = True

	if f.has_key( 'street2' ) and f['street2'].value != '' :
		bFirstCall = False
		fields['street2'] = f['street2'].value

	if f.has_key( 'city' ) and f['city'].value != '' :
		bFirstCall = False
		fields['city'] = f['city'].value
	else :
		bErrors = True

	if f.has_key( 'state' ) and f['state'].value != '' :
		bFirstCall = False
		fields['state'] = f['state'].value
	else :
		bErrors = True

	if f.has_key( 'zip' ) and f['zip'].value != '' :
		bFirstCall = False
		zip = f['zip'].value
		if len( zip ) != 5 :
			bErrors = True
			fields['zip'] = ''
		else :
			try :
				int( zip )
				fields['zip'] = zip
			except :
				bErrors = True
				fields['zip'] = ''
	else :
		bErrors = True

	if f.has_key( 'zip_4' ) and f['zip_4'].value != '' :
		bFirstCall = False
		if len( f['zip_4'].value ) != 4 :
			bErrors = True
			fields['zip_4'] = 'ERR'
		else :
			try :
				int( f['zip_4'].value )
				fields['zip_4'] = f['zip_4'].value
			except :
				bErrors = True
				fields['zip_4'] = 'ERR'

	if f.has_key( 'area' ) and f['area'].value != '' :
		bFirstCall = False
		area = f['area'].value
		if len( area ) != 3 :
			bErrors = True
			fields['area'] = ''
		else :
			try :
				int( area )
				fields['area'] = area
			except :
				bErrors = True
				fields['area'] = ''
	else :
		bErrors = True

	if f.has_key( 'trunk' ) and f['trunk'].value != '' :
		bFirstCall = False
		if len( f['trunk'].value ) != 3 :
			bErrors = True
			fields['trunk'] = ''
		else :
			try :
				int( f['trunk'].value )
				fields['trunk'] = f['trunk'].value
			except :
				bErrors = True
				fields['trunk'] = ''
	else :
		bErrors = True

	if f.has_key( 'ext' ) and f['ext'].value != '' :
		bFirstCall = False
		if len( f['ext'].value ) != 4 :
			bErrors = True
			fields['ext'] = ''
		else :
			try :
				int( f['ext'].value )
				fields['ext'] = f['ext'].value
			except :
				bErrors = True
				fields['ext'] = ''
	else :
		bErrors = True
	
	if bFirstCall :
		printForm( fields )
	else :
		if bErrors :
			print "<b><font color='red' size='+2'>Error!</font></b>"
		else :
			printTable( fields )
	
		print "<hr>"
		printForm( fields , bErrors )
	

def printForm( f, errors=False ) :
	'''Given dict f of fields
		Prints the form (in a table) to the HTML document (stdout)
	'''

	print r"""<form action='/~kschmidt/cgi-bin/Python/info.cgi'
	method='post' enctype='multipart/form-data'> 

	<table><tbody>
		<tr><th>Name:</th>
			<td><input type='text' name='name' class='reqd' value='""" + \
				f['name'] + """'></td></tr>
		<tr><th>Street Address 1:</th>
			<td><input type='text' name='street1' class='reqd' value='""" + \
				f['street1'] + """'></td></tr>
		<tr><th>Street Address 2:</th>
			<td><input type='text' name='street2' class='opt' value='""" + \
				f['street2'] + """'></td></tr>
		<tr><th>City:</th>
			<td><input type='text' name='city' class='reqd' value='""" + \
				f['city'] + """'></td></tr>
		<tr><th>State:</th>
			<td><input type='text' name='state' class='reqd' value='""" + \
			f['state'] + """' size='2' maxlength='2'></td></tr>
		<tr><th>Zip:</th>
			<td nowrap><input type='text' name='zip' class='reqd' value='""" + \
				f['zip'] + """' size='5' maxlength='5'> - 
				<input type='text' name='zip_4' class='opt' value='""" + \
					f['zip_4'] + """' size='4' maxlength='4'></td></tr>
		<tr><th>Phone #:</th>
			<td nowrap>( <input type='text' name='area' class='reqd' value='""" + \
				f['area'] + """'size='3' maxlength='3'> )
				<input type='text' name='trunk' class='reqd' value='""" + \
					f['trunk'] + """' size='3' maxlength='3'> - 
				<input type='text' name='ext' class='reqd' value='""" + \
					f['ext'] + """' size='4' maxlength='4'></td></tr>
		<tr><td><input type='submit' value='Submit'></td>
			<td><input type='reset' value='Clear'></td></tr>
	</tbody></table>
"""

def printTable( f ) :
	'''Given dict f of fields
		Prints the table to HTML document
	'''

	print r"""	<table><tbody>
		<tr><th>Name:</th>
			<td>""" + f['name'] + """</td></tr>
		<tr><th>Street Address 1:</th>
			<td>""" + f['street1'] + """</td></tr>
		<tr><th>Street Address 2:</th>
			<td>""" + f['street2'] + """</td></tr>
		<tr><th>City:</th>
			<td>""" + f['city'] + """</td></tr>
		<tr><th>State:</th>
			<td>""" + f['state'] + """</td></tr>
		<tr><th>Zip:</th>
			<td nowrap>""" + f['zip'] + "-" + f['zip_4'] + """</td></tr>
		<tr><th>Phone #:</th>
			<td nowrap>(""" +  f['area'] + ") " + f['trunk'] + \
					"-" + f['ext'] + """</td></tr>
		<tr><td>
			<td>
	</tbody></table>
"""


def main() :

	form = cgi.FieldStorage()	# get access to the form fields

	printHead()

	parseForm( form )

	printTail()


def hold() :
		# let's look at all of the fields:
	for field in form.keys() :
		print "\t<tr>\n\t\t<th>" + field + "</th>"
		print "\t\t<td>" + str( form[field].value ) + "</td></tr>"

	print "</tbody></table>"

	print """<p><b>Note:</b>  The satellite data associated w/a field name
	<i>might</i> be a list (if, for example, the fieldname was used multiple
	times), so, you might need to check, and iterate over this list, pulling out
	each element's <tt>value</tt> attribute.</p>"""

main()
