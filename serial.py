from json import loads, dumps # this works for now :/

# this is explicit to avoid problems with undefined behavior
CODEC = 'UTF-8'


def serialize(stuff):
	return dumps(stuff).encode(CODEC)


def deserialize(cantread):
	return loads(cantread.decode(CODEC))