from serial import serialize, deserialize
from threading import Thread
from caller import Caller

BUFFER_SIZE = 512 # This is probably enough

class Network:
	# should these be created with __init__? idk
	sockets = {}

	on_connect = Caller()
	on_close = Caller()
	on_receive = Caller()

	def connect(network, socket):
		def doodoo():
			network.sockets[socket] = None
			network.on_connect.fire(socket)

			while stream := socket.recv(BUFFER_SIZE):
				network.on_receive.fire(socket, deserialize(stream))

			network.on_close.fire(socket)
			del network.sockets[socket]
			socket.close()

		Thread(target = doodoo).start()

	def send(network, stuff):
		for socket in network.sockets:
			socket.send(serialize(stuff))