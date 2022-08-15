from v2 import v2,null2
from r2 import r2
from sorter import Sorter
from math import atan2

index=0
rays=[]

class m2:
	def __init__(self,l):
		global index
		self.i=l*index
		index+=1
		rays.extend(l*[None])

	def build_rays(self,v):
		i=self.i
		n=len(v)-1
		for o in range(n):#maybe this is n
			rays[i+o]=r2(v[o],v[o+1]-v[o])
		rays[i+n]=r2(v[n],v[0]-v[n])

	def update_vertices(self,verts):
		hx,hy=0,0
		lx,ly=0,0

		sorter=Sorter()

		c=verts[0]

		for v in verts:
			hx,hy=max(hx,v.x),max(hy,v.y)
			lx,ly=min(lx,v.x),min(ly,v.y)

			sorter.set(atan2(v.y-c.y,v.x-c.x),v)

		self.h=v2(hx,hy)
		self.l=v2(lx,ly)

		self.build_rays(sorter.sorted)

	def get_aabb(self):
		return self.h,self.l

def push_point(r0):
	fh=r0.l
	fn=null2

	for r1 in rays:
		h,n=r0.push_point(r1)

		if h<fh:
			fh=h
			fn=n

	return fh,fn