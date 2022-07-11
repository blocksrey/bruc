class vec3:
	def __init__(a, x, y, z):
		a.x, a.y, a.z = x, y, z

	def __str__(a):
		return "vec3({}, {}, {})".format(a.x, a.y, a.z)

	def __add__(a, b):
		return vec3(a.x + b.x, a.y + b.y, a.z + b.z)

	def __sub__(a, b):
		return vec3(a.x - b.x, a.y - b.y, a.z - b.z)

	def __mul__(a, b):
		return vec3(a.x * b.x, a.y * b.y, a.z * b.z)

	def __div__(a, b):
		return vec3(a.x / b.x, a.y / b.y, a.z / b.z)

	def __neg__(a):
		return vec3(-a.x, -a.y, -a.z)

	def dot(a, b):
		return a.x*b.x + a.y*b.y + a.z*b.z