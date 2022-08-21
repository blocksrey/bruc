from serial import serialize,deserialize
from threading import Thread
from caller import Caller

BUFFER_SIZE=512#this is probably enough

class Commer:
	#should these be created with __init__? idk
	socks={}
	on_connect=Caller()
	on_close=Caller()
	on_receive=Caller()

	def connect(self,ソケット):
		def 入():
			self.socks[ソケット]=None
			self.on_connect.fire(ソケット)

			while バイト:=ソケット.recv(BUFFER_SIZE):
				self.on_receive.fire(ソケット,*deserialize(バイト))#tuple unpacking is wrong here because its wrong in serializer (this is living proof that wrong creates more wrong)

			self.on_close.fire(ソケット)
			del self.socks[ソケット]
			ソケット.close()

		Thread(target=入).start()

	def send(self,*whatever):#this is definitely faster than send if youre connected to multiple sockets
		bytes=serialize(*whatever)#tuple unpacking is wrong here because its wrong in serializer (this is living proof that wrong creates more wrong)
		for ソケット in self.socks:
			ソケット.send(bytes)

	def send_but(self,sockin,*whatever):
		bytes=serialize(*whatever)#tuple unpacking is wrong here because its wrong in serializer (this is living proof that wrong creates more wrong)
		for ソケット in self.socks:
			if sockin != ソケット:
				ソケット.send(bytes)

	#             YESSSS
	def send_to(self,ソケット,*whatever):#AHHHH YESSSSSSSSSSS
		ソケット.send(serialize(*whatever))#tuple unpacking is wrong here because its wrong in serializer (this is living proof that wrong creates more wrong)