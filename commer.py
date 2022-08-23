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

	def connect(self,socket):
		def start():
			self.socks[socket]=None
			self.on_connect.fire(socket)
			
			while 1:
				byte=socket.recv(BUFFER_SIZE)
				self.on_receive.fire(socket,*deserialize(byte))#tuple unpacking is wrong here because its wrong in serializer (this is living proof that wrong creates more wrong)
				if not byte:
					break

			self.on_close.fire(socket)
			del self.socks[socket]
			socket.close()

		a=Thread(target=start)
		a.start()
		#print(a.is_alive())

	def send(self,*whatever):#this is definitely faster than send if youre connected to multiple sockets
		bytes=serialize(*whatever)#tuple unpacking is wrong here because its wrong in serializer (this is living proof that wrong creates more wrong)
		for socket in self.socks:
			socket.send(bytes)

	def send_but(self,sockin,*whatever):
		bytes=serialize(*whatever)#tuple unpacking is wrong here because its wrong in serializer (this is living proof that wrong creates more wrong)
		for socket in self.socks:
			if sockin != socket:
				socket.send(bytes)

	#             YESSSS
	def send_to(self,socket,*whatever):#AHHHH YESSSSSSSSSSS
		socket.send(serialize(*whatever))#tuple unpacking is wrong here because its wrong in serializer (this is living proof that wrong creates more wrong)
