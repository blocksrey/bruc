from serial import serialize, deserialize
from threading import Thread

def Network():
	queue = []

	def connect(sock_t):
		addr_t = sock_t.getpeername()
		def dewit():
			print('connect', addr_t)
			sock_t.send("A".encode())
			while stream_i := sock_t.recv(1024): # this is probably enough
				print(addr_t, deserialize(stream_i))
				print(len(queue))
				sock_t.send("A".encode())
				if len(queue) > 0:
					sock_t.send(serialize(queue))
					queue = []
			print('close', addr_t)
			sock_t.close()
		Thread(target = dewit).start()

	def enqueue(stuff):
		queue.append(stuff)

	return connect, enqueue