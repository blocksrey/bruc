def proj(a,b,i,j):
	ij=i.dot(j)
	if ij>0:
		return a+(b-a).dot(j)/ij*i
	return a+i

class r2:
	def __init__(r2,o,h):
		r2.o,r2.h=o,h

	def __repr__(a):
		return 'r2({},{})'.format(a.o,a.h)

	def push_point(a,b):
		w=proj(a.o,b.o,a.h,b.h.perp())

		la=a.h.norm()
		lb=b.h.norm()

		za=a.h.dot(w-a.o)/la
		zb=b.h.dot(w-b.o)/lb

		if za>0 and za<la and zb>0 and zb<lb:#idc rn
			return za,b.h.prep().unit()#perp in the other direction
		return la,0*b.h