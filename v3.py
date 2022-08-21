from math import sqrt
from v import V

class V3(V):
	def __init__(a,x,y,z):
		a.x,a.y,a.z=x,y,z

	def __repr__(a):
		return 'V3({},{},{})'.format(a.x,a.y,a.z)

	def __add__(a,b):
		return V3(a.x+b.x,a.y+b.y,a.z+b.z)

	def __sub__(a,b):
		return V3(a.x-b.x,a.y-b.y,a.z-b.z)

	def __rmul__(a,b):
		return isinstance(b,V3) and V3(a.x*b.x,a.y*b.y,a.z*b.z) or V3(a.x*b,a.y*b,a.z*b)

	def __truediv__(a,b):#wtf
		return isinstance(b,V3) and V3(a.x/b.x,a.y/b.y,a.z/b.z) or V3(a.x/b,a.y/b,a.z/b)

	def __neg__(a):
		return V3(-a.x,-a.y,-a.z)

	def dot(a,b):
		return a.x*b.x+a.y*b.y+a.z*b.z

	def norm(a):
		return sqrt(a.x*a.x+a.y*a.y+a.z*a.z)

	def unit(a):
		l=sqrt(a.x*a.x+a.y*a.y+a.z*a.z)
		return V2(a.x/l,a.y/l,a.z/l)

null3=V3(0,0,0)