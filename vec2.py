from math import sqrt, atan2, cos, sin


class Vec2:
	def __init__(a, x, y):
		a.x, a.y = x, y

	def __add__(a, b):
		return isinstance(b, Vec2) and Vec2(a.x+b.x, a.y+b.y) or Vec2(a.x+b, a.y+b)

	def __sub__(a, b):
		return isinstance(b, Vec2) and Vec2(a.x-b.x, a.y-b.y) or Vec2(a.x-b, a.y-b)

	def __mul__(a, b):
		return isinstance(b, Vec2) and Vec2(a.x*b.x, a.y*b.y) or Vec2(a.x*b, a.y*b)

	def __truediv__(a, b): # wtf
		return isinstance(b, Vec2) and Vec2(a.x/b.x, a.y/b.y) or Vec2(a.x/b, a.y/b)

	def __mod__(a, b):
		return isinstance(b, Vec2) and Vec2(a.x%b.x, a.y%b.y) or Vec2(a.x%b, a.y%b)

	def __neg__(a):
		return Vec2(-a.x, -a.y)

	def dot(a, b):
		return a.x*b.x+a.y*b.y

	def norm(a):
		return sqrt(a.x*a.x+a.y*a.y)

	def unit(a):
		l = sqrt(a.x*a.x+a.y*a.y)
		return Vec2(a.x/l, a.y/l)

	def polar(a):
		return sqrt(a.x*a.x+a.y*a.y), atan2(a.y, a.x)

	def cmul(a, b):
		return Vec2(a.x*b.x - a.y*b.y, a.x*b.y + a.y*b.x)

	def cang(t):
		return Vec2(cos(t), sin(t))

	def perp(a):
		return Vec2(-a.y, a.x)