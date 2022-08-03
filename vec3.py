from math import sqrt

class Vec3:
	def __init__(a, x, y, z):
		a.x, a.y, a.z = x, y, z

	def __str__(a):
		return 'Vec3({}, {}, {})'.format(a.x, a.y, a.z)

	def __add__(a, b):
		return Vec3(a.x + b.x, a.y + b.y, a.z + b.z)

	def __sub__(a, b):
		return Vec3(a.x - b.x, a.y - b.y, a.z - b.z)

	def __mul__(a, b):
		return Vec3(a.x*b.x, a.y*b.y, a.z*b.z)

	def __div__(a, b):
		return Vec3(a.x/b.x, a.y/b.y, a.z/b.z)

	def __neg__(a):
		return Vec3(-a.x, -a.y, -a.z)

	def __mod__(a, b):
		return Vec3(a.x%b, a.y%b, a.z%b)

	def norm(a):
		return sqrt(a.x*a.x + a.y*a.y + a.z*a.z)

	def dot(a, b):
		return a.x*b.x + a.y*b.y + a.z*b.z

	def unit(a):
		l = sqrt(a.x*a.x + a.y*a.y + a.z*a.z)
		return Vec2(a.x/l, a.y/l, a.z/l)