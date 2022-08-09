from math import sqrt

class Vec3:
	def __init__(a, x, y, z):
		a.x, a.y, a.z = x, y, z

	def __add__(a, b):
		return isinstance(b, Vec3) and Vec3(a.x+b.x, a.y+b.y, a.z+b.z) or Vec3(a.x+b, a.y+b, a.z+b)

	def __sub__(a, b):
		return isinstance(b, Vec3) and Vec3(a.x-b.x, a.y-b.y, a.z-b.z) or Vec3(a.x-b, a.y-b, a.z-b)

	def __mul__(a, b):
		return isinstance(b, Vec3) and Vec3(a.x*b.x, a.y*b.y, a.z*b.z) or Vec3(a.x*b, a.y*b, a.z*b)

	def __truediv__(a, b): # wtf
		return isinstance(b, Vec3) and Vec3(a.x/b.x, a.y/b.y, a.z/b.z) or Vec3(a.x/b, a.y/b, a.z/b)

	def __mod__(a, b):
		return isinstance(b, Vec3) and Vec3(a.x%b.x, a.y%b.y, a.z%b.z) or Vec3(a.x%b, a.y%b, a.z%b)

	def __neg__(a):
		return Vec3(-a.x, -a.y, -a.z)

	def dot(a, b):
		return a.x*b.x+a.y*b.y+a.z*b.z

	def norm(a):
		return sqrt(a.x*a.x+a.y*a.y+a.z*a.z)

	def unit(a):
		l = sqrt(a.x*a.x+a.y*a.y+a.z*a.z)
		return Vec2(a.x/l, a.y/l, a.z/l)