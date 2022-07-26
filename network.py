from serial import serialize, deserialize
from threading import Thread
from signal import Signal

BUFFER_SIZE = 512

class Network:
	# should these be created with __init__? idk
	socks = {}

	on_connect = Signal()
	on_close = Signal()
	on_receive = Signal()

	def connect(self, sock):
		def doodoo():
			self.socks[sock] = None

			self.on_connect.fire(sock)
			while stream := sock.recv(BUFFER_SIZE):
				self.on_receive.fire(sock, deserialize(stream))
			self.on_close.fire(sock)

			del self.socks[sock]

			sock.close()

		Thread(target = doodoo).start()

	def send(self, stuff):
		for sock in self.socks:
			sock.send(serialize(stuff))