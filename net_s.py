import socket
from network import Network
from threading import Thread

nConnect, nQueue = Network()

def talk():
	while 1:
		nQueue(input())
Thread(target = talk).start()

sock_u = socket.socket() # AF_INET, SOCK_STREAM
sock_u.bind(('localhost', 0xDEAD))
sock_u.listen(4) # this might be enough idk

from atexit import register
register(sock_u.close)

while 1:
	nConnect(sock_u.accept()[0])