import socket
from network import network
from threading import Thread

network0 = network()

def talk():
	while 1:
		network0.send(input())
Thread(target = talk).start()

sock_t = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET, SOCK_STREAM
sock_t.connect(("localhost", 0xDEAD))







def onconnect(sock):
	print("CONNECT", sock)
onconnectcon = network0.onconnect.connect(onconnect)

def onclose(sock):
	print("CLOSE", sock)
onclosecon = network0.onclose.connect(onclose)

def onreceive(sock, key, *args):
	print(key, *args)
onreceivecon = network0.onreceive.connect(onreceive)








network0.connect(sock_t)
