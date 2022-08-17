def proj(a,b,i,j):
	ij=i.dot(j)
	if ij>0:
		return a+(b-a).dot(j)/ij*i
	return a+i

class r2:
	def __init__(a,o,d):
		l=d.norm()
		a.o,a.u,a.l=o,l and d/l or d,l

	def __repr__(a):
		return 'r2({},{})'.format(a.o,a.u)

	def push_point(a,b):
		p=proj(a.o,b.o,a.l*a.u,b.u.perp())

		da=a.u.dot(p-a.o)
		db=b.u.dot(p-b.o)

		if da>0 and da<a.l and db>0 and db<b.l:#idc rn
			return da,b.u.prep()#perp in the other direction
		return a.l,0*b.u

	def project_point(a,v):
		return a.o+max(0,min((v-a.o).dot(a.u),a.l))*a.u