import socket
from network import network
from threading import Thread

network0 = network()

def talk():
	while 1:
		network0.send(input())
Thread(target = talk).start()

sock_u = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET, SOCK_STREAM
sock_u.bind(("localhost", 0xDEAD))
sock_u.listen(4) # this might be enough idk

from atexit import register
register(sock_u.close)







def onconnect(sock):
	print("CONNECT", sock)
onconnectcon = network0.onconnect.connect(onconnect)

def onclose(sock):
	print("CLOSE", sock)
onclosecon = network0.onclose.connect(onclose)

def onreceive(sock, key, *args):
	print(key, *args)
onreceivecon = network0.onreceive.connect(onreceive)










while 1:
	network0.connect(sock_u.accept()[0])