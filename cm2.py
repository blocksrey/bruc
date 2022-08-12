from v2 import v2,null2
from r2 import r2
from math import inf,atan2
from sorty import sorty

class cm2:
	def __init__(self,v):
		self.update_vertices(v)

	def _build_rays(self):
		self._rays=[]
		n=len(self._verts)
		for i in range(n):
			a=self._verts[i]
			b=self._verts[(i+1)%n]
			self._rays.append(r2(a,b-a))

	def update_vertices(self,v):
		self._verts=v
		self._sorty=sorty()#THIS NEEDS TO CHANGE (SLOW!)
		c=self._verts[0]
		for v in self._verts:
			self._sorty.set(atan2(v.y-c.y,v.x-c.x),v)
		self._verts=self._sorty.sorted
		self._build_rays()

	def get_aabb(self):
		ux,uy=-inf,-inf
		lx,ly=+inf,+inf
		for v in self._rays:
			vx,vy=v.o.x,v.o.y
			ux,uy=max(ux,vy),max(uy,vy)
			lx,ly=min(lx,vy),min(ly,vy)
		return v2(ux,uy),v2(lx,ly)

	def push_point(self,r2):
		fz=r2.l
		fn=null2
		for r in self._rays:
			cz,cn=r2.push_point(r)
			if cz<fz:
				fz=cz
				fn=cn
		return fz,fn