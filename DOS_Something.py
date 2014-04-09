import urllib.request
import socket
import urllib
import threading
from threading import Thread

import threading

class SpammingThread(threading.Thread):
	def __init__(self, website, i):
		threading.Thread.__init__(self)
		self.website = website
		self.i = i

	def run(self):
		for i in range(100):
			string = str(urllib.request.urlopen(self.website).read())
			# print(str(string))
		print("Thread ended", self.i)



for i in range(100):
	SpammingThread("https://sites.google.com/site/davidchristy520/", i).start()
	print("Starting Thread")
