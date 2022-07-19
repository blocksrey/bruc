from serial import serialize, deserialize
from threading import Thread
from signal import signal

BUFFER_SIZE = 512

class network:
	# should these be created with __init__? idk
	socks = {}

	onconnect = signal()
	onclose = signal()
	onreceive = signal()

	def connect(self, sock):
		def doodoo():
			self.socks[sock] = None

			self.onconnect.fire(sock)
			while stream := sock.recv(BUFFER_SIZE):
				self.onreceive.fire(sock, deserialize(stream))
			self.onclose.fire(sock)

			del self.socks[sock]

			sock.close()

		Thread(target = doodoo).start()

	def send(self, stuff):
		for sock in self.socks:
			sock.send(serialize(stuff))