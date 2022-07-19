from serial import serialize, deserialize
from threading import Thread

BUFFER_SIZE = 1024 # this is probably enough

def Network():
	queue = []

	def connect(sock_t):
		addr_t = sock_t.getpeername()
		iscon = 1

		def begin():
			print("connect", addr_t)

			while stream_i := sock_t.recv(BUFFER_SIZE):
				print(addr_t, deserialize(stream_i))

			print("close", addr_t)

			# disable connection state
			nonlocal iscon
			iscon = 0

			sock_t.close()

		Thread(target = begin).start()

		def comm():
			# run communications while connected
			while iscon:
				nonlocal queue
				if len(queue):
					sock_t.send(serialize(queue)) # this prevents an entire paradox
					queue = []

			print("comms ended")

		Thread(target = comm).start()

	def enqueue(stuff):
		nonlocal queue
		queue.append(stuff)

	return connect, enqueue