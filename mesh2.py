from v2 import v2,null2
from r2 import r2
from math import inf,atan2
from sorty import sorty

class Mesh2:
	def __init__(self,v):
		self.update_vertices(v)

	def _build_rays(self):
		self._rs=[]
		n=len(self._vs)
		for i in range(n):
			va=self._vs[i]
			vb=self._vs[(i+1)%n]
			self._rs.append(r2(va,vb-va))

	def update_vertices(self,v):
		self._vs=v
		self._s=sorty()#THIS NEEDS TO CHANGE (SLOW!)
		c=self._vs[0]
		for v in self._vs:
			self._s.set(atan2(v.y-c.y,v.x-c.x),v)
		self._vs=self._s.sorted
		self._build_rays()

	def get_aabb(self):
		ux,uy=-inf,-inf
		lx,ly=+inf,+inf
		for v in self._rs:
			vx,vy=v.o.x,v.o.y
			ux,uy=max(ux,vy),max(uy,vy)
			lx,ly=min(lx,vy),min(ly,vy)
		return v2(ux,uy),v2(lx,ly)

	def push_point(self,r2):
		fz=r2.h.norm()
		fn=null2
		for r in self._rs:
			cz,cn=r2.push_point(r)
			if cz<fz:
				fz=cz
				fn=cn
		return fz,fn