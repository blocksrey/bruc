import socket
import network

network0 = network.Network()

socket0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP
socket0.connect(('localhost', 57005)) # Hehe



def on_connect(socket):
	print('CONNECT', socket)
on_connectcon = network0.on_connect.connect(on_connect)

def on_close(socket):
	print('CLOSE', socket)
on_closecon = network0.on_close.connect(on_close)

def on_receive(socket, key, *args):
	print(key, *args)
on_receivecon = network0.on_receive.connect(on_receive)






network0.connect(socket0)