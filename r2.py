def proj(a,b,i,j):
	ij=i.dot(j)
	if ij>0:
		return a+(b-a).dot(j)/ij*i
	return a+i

class r2:
	def __init__(r2,o,h):
		l=h.norm() or 1e-6#only 1 square root damn
		r2.o,r2.h,r2.l=o,h/l,l

	def __repr__(a):
		return 'r2({},{})'.format(a.o,a.h)

	def push_point(a,b):
		p=proj(a.o,b.o,a.l*a.h,b.h.perp())

		da=a.h.dot(p-a.o)
		db=b.h.dot(p-b.o)

		if da>0 and da<a.l and db>0 and db<b.l:#idc rn
			return da,b.h.prep()#perp in the other direction
		return a.l,0*b.h