from v2 import v2,null2
from r2 import r2
from math import inf,atan2
from sorter import Sorter

class cm2:
	def build_rays(self):
		self.rays=[]
		n=len(self.vertices)
		for i in range(n):
			a=self.vertices[i]
			b=self.vertices[(i+1)%n]
			self.rays.append(r2(a,b-a))

	def update_vertices(self,v):
		self.vertices=v
		self.sorter=Sorter()#THIS NEEDS TO CHANGE (SLOW!)
		c=self.vertices[0]
		for v in self.vertices:
			self.sorter.set(atan2(v.y-c.y,v.x-c.x),v)
		self.vertices=self.sorter.sorted
		self.build_rays()

	__init__=update_vertices

	def get_aabb(self):
		ux,uy=-inf,-inf
		lx,ly=+inf,+inf
		for v in self.rays:
			vx,vy=v.o.x,v.o.y
			ux,uy=max(ux,vy),max(uy,vy)
			lx,ly=min(lx,vy),min(ly,vy)
		return v2(ux,uy),v2(lx,ly)

	def get_aabb2(self):
		print("ASD")

	def push_point(self,r2):
		fz=r2.l
		fn=null2
		for r in self.rays:
			cz,cn=r2.push_point(r)
			if cz<fz:
				fz=cz
				fn=cn
		return fz,fn