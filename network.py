from socket import socket,AF_INET,SOCK_STREAM
from commer import Commer

the_commer=Commer()

the_socket=socket(AF_INET,SOCK_STREAM)#IPv4,TCP

from caller import Caller
callers={}

def on_receive(name):
	try:#this is just awful
		if not callers[name]:
			pass#this is just awful
	except:#this is just awful
		callers[name]=Caller()
	return callers[name]

def _(socket,name,*whatever):#wrong
	callers[name].fire(socket,*whatever)#wrong
the_commer.on_receive.connect(_)

send=the_commer.send
send_to=the_commer.send_to
send_but=the_commer.send_but

def client():
	the_socket.connect(('localhost',57005))

	the_commer.connect(the_socket)

def server():
	the_socket.bind(('localhost',57005))
	the_socket.listen(4)#this is probs enough

	from atexit import register
	register(the_socket.close)

	while 1:
		the_commer.connect(the_socket.accept()[0])