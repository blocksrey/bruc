from serial import serialize,deserialize
from threading import Thread
from caller import caller

BUFFER_SIZE=512#this is probably enough

class network:
	#should these be created with __init__? idk
	socks={}
	on_connect=caller()
	on_close=caller()
	on_receive=caller()

	def connect(self,ソケット):
		def 入():
			self.socks[ソケット]=None
			self.on_connect.fire(ソケット)

			while バイト:=ソケット.recv(BUFFER_SIZE):
				self.on_receive.fire(ソケット,deserialize(バイト))

			self.on_close.fire(ソケット)
			del self.socks[ソケット]
			ソケット.close()

		Thread(target=入).start()

	def send(self,d):
		for ソケット in self.socks:
			ソケット.send(serialize(d))