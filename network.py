from serial import serialize, deserialize
from threading import Thread
from sig import Signal

BUFFER_SIZE = 512

class Network:
	# should these be created with __init__? idk
	sockets = {}

	on_connect = Signal()
	on_close = Signal()
	on_receive = Signal()

	def connect(network, socket):
		def doodoo():
			network.sockets[socket] = None

			network.on_connect.fire(socket)

			while 1:
				stream = socket.recv(BUFFER_SIZE)
				if not stream:
					break

				network.on_receive.fire(socket, deserialize(stream))

			network.on_close.fire(socket)

			del network.sockets[socket]

			socket.close()

		Thread(target = doodoo).start()

	def send(network, stuff):
		for socket in network.sockets:
			socket.send(serialize(stuff))