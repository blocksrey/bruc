from socket import socket
from network import Network
from threading import Thread

network0 = Network()

def talk():
	while 1:
		network0.send(input())
Thread(target = talk).start()

socket0 = socket() # AF_INET, SOCK_STREAM
socket0.bind(("localhost", 57005)) # hehe
socket0.listen(4) # this might be enough idk

from atexit import register
register(socket0.close)



def on_connect(socket):
	print("CONNECT", socket)
on_connectcon = network0.on_connect.connect(on_connect)

def on_close(socket):
	print("CLOSE", socket)
on_closecon = network0.on_close.connect(on_close)

def on_receive(socket, key, *args):
	print(key, *args)
on_receivecon = network0.on_receive.connect(on_receive)










while 1:
	network0.connect(socket0.accept()[0])