from json import loads, dumps # this works for now :/

def serialize(stuff):
	return dumps(stuff).encode()

def deserialize(cantread):
	return loads(cantread.decode())