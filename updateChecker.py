'''
A quick script I wrote to tell if a website code has been changed,
of was meant for websites that change often, because its very wasteful, 
but gives you instant results.
'''

import urllib.request

website = "http://www.google.com"

f = urllib.request.urlopen(website)
current = f.read()

while True:
	f = urllib.request.urlopen(website)
	temp = f.read()
	if(current != temp):
		break
