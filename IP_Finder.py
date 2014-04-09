'''
A small program to put the Local and Global IP on the same screen.
I needed to know both for a project and wrote this up to save time.
'''

import urllib.request
import socket
import urllib

print("Local IP : " + socket.gethostbyname(socket.gethostname()))
inFile = str(urllib.request.urlopen("http://www.biranchi.com/ip.php").read())
# print("File without itereating over: "+ str(inFile))
ip = "Global IP: "
for i in inFile:
	if i.isdigit() or i == ".":
		ip +=i
print(str(ip))
