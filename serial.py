from pickle import loads,dumps#this shit is slow and needs to change

def serialize(*whatever):
	return dumps(whatever)

deserialize=loads