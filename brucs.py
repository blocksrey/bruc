# make the server and the client the same thing (in implementation) and have them work seamlessly


import network

def _(socket,*whatever):
	network.send_but(socket,'newbullet',*whatever)
network.on_receive('newbullet').connect(_)



def _(socket,*whatever):
	network.send_but(socket,'newcharacter',*whatever)
network.on_receive('newcharacter').connect(_)



network.server()