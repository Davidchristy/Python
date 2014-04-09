import urllib.request

f = urllib.request.urlopen("http://www.google.com")
current = f.read()

while True:
	f = urllib.request.urlopen("http://www.google.com")
	temp = f.read()
	if(current != temp):
		break
