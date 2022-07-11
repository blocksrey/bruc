import socket
from network import Network
from threading import Thread

nConnect, nQueue = Network()

def talk():
	while 1:
		nQueue(input())
Thread(target = talk).start()

sock_t = socket.socket() # AF_INET, SOCK_STREAM
sock_t.connect(("localhost", 0xDEAD))






nConnect(sock_t)