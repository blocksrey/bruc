from v2 import V2,null2
from r2 import R2
from sorter import Sorter
from math import atan2,inf,sqrt
from spacer import Spacer

index=0
rays=[]
racer=Spacer()

class M2:
	def __init__(m,l):
		global index
		m.i=l*index
		index+=1
		rays.extend(l*[None])

	def build_rays(m,v):
		i=m.i
		n=len(v)-1
		for o in range(n):#maybe this is n
			rays[i+o]=R2(v[o],v[o+1]-v[o])
		rays[i+n]=R2(v[n],v[0]-v[n])

	def update_vertices(m,vt):
		hx,hy=0,0
		lx,ly=0,0

		sorter=Sorter()

		c=vt[0]

		for v in vt:
			hx,hy=max(hx,v.x),max(hy,v.y)
			lx,ly=min(lx,v.x),min(ly,v.y)

			sorter.set(atan2(v.y-c.y,v.x-c.x),v)

		m.s=V2(lx,ly)
		m.e=V2(hx,hy)-m.s

		m.build_rays(sorter.sorted)

	def get_aabb(m):
		return m.s,m.e

def push_point(r0):
	fl=r0.l
	fn=null2

	for r1 in rays:
		h,n=r0.push_point(r1)

		if fl>h:
			fl=h
			fn=n

	return fl,fn

def project_point(v):
	fl=inf
	fp=null2

	for r in rays:
		p=r.project_point(v)
		d=(v-p).square()

		if fl*fl>d:
			fl=d
			fp=p

	return sqrt(fl),fp

#def push_point(r):
#	fl=r.l
#	fn=null2
#
#	for y in racer.from_aabb(r.get_aabb()):
#		h,n=r.push_point(y)
#
#		if fl>h:
#			fl=h
#			fn=n
#
#	return fl,fn
#
#def project_point(v):
#	fl=inf
#	fp=null2
#
#	for r in racer.from_point(v):
#		p=r.project_point(v)
#		d=(v-p).square()
#
#		if fl*fl>d:
#			fl=d
#			fp=p
#
#	return sqrt(fl),fp