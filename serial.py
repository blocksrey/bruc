from json import loads, dumps

def serialize(yup):
	return dumps(yup).encode()

def deserialize(wow):
	return loads(wow.decode())
