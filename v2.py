from math import sqrt,atan2,cos,sin
from v import V

class V2(V):
	def __init__(a,x,y):
		a.x,a.y=x,y

	def __repr__(a):
		return 'V2({},{})'.format(a.x,a.y)

	def __add__(a,b):
		return V2(a.x+b.x,a.y+b.y)

	def __sub__(a,b):
		return V2(a.x-b.x,a.y-b.y)

	def __rmul__(a,b):
		return isinstance(b,V2) and V2(a.x*b.x,a.y*b.x) or V2(a.x*b,a.y*b)

	def __truediv__(a,b):#wtf
		return isinstance(b,V2) and V2(a.x/b.x,a.y/b.y) or V2(a.x/b,a.y/b)

	def __neg__(a):
		return V2(-a.x,-a.y)

	#def __eq__(a,b):
	#	return a.x==b.x and a.y==b.y

	def dump(a):
		return a.x,a.y

	def dot(a,b):
		return a.x*b.x+a.y*b.y

	def square(a):
		return a.x*a.x+a.y*a.y

	def norm(a):
		return sqrt(a.x*a.x+a.y*a.y)

	def unit(a):
		l=sqrt(a.x*a.x+a.y*a.y)
		return V2(a.x/l,a.y/l)

	def cmul(a,b):
		return V2(a.x*b.x-a.y*b.y,a.x*b.y+a.y*b.x)

	def perp(a):
		return V2(-a.y,a.x)

	def prep(a):
		return V2(a.y,-a.x)

null2=V2(0,0)

def cang(t):
	return V2(cos(t),sin(t))