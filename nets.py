import socket
import network

network0=network.network()

socket0=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#IPv4,TCP
socket0.bind(('localhost',57005))#Hehe
socket0.listen(4)#This might be enough?

from atexit import register
register(socket0.close)




def on_connect(socket):
	print('CONNECT',socket)
on_connectcon=network0.on_connect.connect(on_connect)

def on_close(socket):
	print('CLOSE',socket)
on_closecon=network0.on_close.connect(on_close)

def on_receive(socket,key,*args):
	print(key,*args)
on_receivecon=network0.on_receive.connect(on_receive)







while 1:
	network0.connect(socket0.accept()[0])