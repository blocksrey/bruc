from math import sqrt, atan2

class vec2:
	def __init__(a, x, y):
		a.x, a.y = x, y

	def __str__(a):
		return "vec2({}, {})".format(a.x, a.y)

	def __add__(a, b):
		return vec2(a.x + b.x, a.y + b.y)

	def __sub__(a, b):
		return vec2(a.x - b.x, a.y - b.y)

	def __mul__(a, b):
		return vec2(a.x*b.x, a.y*b.y)

	def __div__(a, b):
		return vec2(a.x/b.x, a.y/b.y)

	def __repr__(a):
		return repr((a.x, a.y))

	def dot(a, b):
		return a.x*b.x + a.y*b.y

	def __neg__(a):
		return vec2(-a.x, -a.y)

	def __mod__(a, b):
		return vec2(a.x%b, a.y%b)

	def __abs__(a):
		return sqrt(a.x*a.x + a.y*a.y)

	def to_polar(a):
		return a.__abs__(), atan2(a.y, a.x)
