from math import sqrt,atan2,cos,sin
from v import v

class v2(v):
	def __init__(a,x,y):
		a.x,a.y=x,y

	def __repr__(a):
		return 'v2({},{})'.format(a.x,a.y)

	def __add__(a,b):
		return v2(a.x+b.x,a.y+b.y)

	def __sub__(a,b):
		return v2(a.x-b.x,a.y-b.y)

	def __rmul__(a,b):
		return isinstance(b,v2) and v2(a.x*b.x,a.y*b.x) or v2(a.x*b,a.y*b)

	def __truediv__(a,b):#wtf
		return isinstance(b,v2) and v2(a.x/b.x,a.y/b.y) or v2(a.x/b,a.y/b)

	def __neg__(a):
		return v2(-a.x,-a.y)

	def __eq__(a,b):
		return a.x==b.x and a.y==b.y

	def dump(a):
		return a.x,a.y

	def dot(a,b):
		return a.x*b.x+a.y*b.y

	def norm(a):
		return sqrt(a.x*a.x+a.y*a.y)

	def unit(a):
		l=sqrt(a.x*a.x+a.y*a.y)
		return v2(a.x/l,a.y/l)

	def cmul(a,b):
		return v2(a.x*b.x-a.y*b.y,a.x*b.y+a.y*b.x)

	def perp(a):
		return v2(-a.y,a.x)

	def prep(a):
		return v2(a.y,-a.x)

null2=v2(0,0)

def cang(t):
	return v2(cos(t),sin(t))