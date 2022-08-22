# make the server and the client the same thing (in implementation) and have them work seamlessly



characters={}


import network

def _(socket,*whatever):
	network.send_but(socket,'newbullet',*whatever)
network.on_receive('newbullet').connect(_)



def _(socket,*whatever):
	characters[socket]=None
	network.send_but(socket,'newcharacter',*whatever)
network.on_receive('newcharacter').connect(_)




def _(socket):
	network.send_to(socket,'okay',112)
network.on_receive('ready').connect(_)





network.server()