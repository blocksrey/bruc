from math import sqrt, atan2

class Vec2:
	def __init__(a, x, y):
		a.x, a.y = x, y

	def __str__(a):
		return "Vec2({}, {})".format(a.x, a.y)

	def __add__(a, b):
		return Vec2(a.x + b.x, a.y + b.y)

	def __sub__(a, b):
		return Vec2(a.x - b.x, a.y - b.y)

	def __mul__(a, b):
		return Vec2(a.x*b.x, a.y*b.y)

	def __div__(a, b):
		return Vec2(a.x/b.x, a.y/b.y)

	def unpack(a):
		return a.x, a.y

	def __neg__(a):
		return Vec2(-a.x, -a.y)

	def __mod__(a, b):
		return Vec2(a.x%b, a.y%b)

	def norm(a):
		return sqrt(a.x*a.x + a.y*a.y)

	def dot(a, b):
		return a.x*b.x + a.y*b.y

	def unit(a):
		l = sqrt(a.x*a.x + a.y*a.y)
		return Vec2(a.x/l, a.y/l)

	def to_polar(a):
		return a.norm(), atan2(a.y, a.x)
