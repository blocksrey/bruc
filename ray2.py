def do_proj(a, b, i, j):
	ij = i.dot(j)
	if ij > 0:
		return a + i*(b - a).dot(j)/ij
	return a + i

class Ray2:
	def __init__(ray2, o, h):
		ray2.o, ray2.h = o, h

	def __repr__(a):
		return 'Ray2({}, {})'.format(a.o, a.h)

	def push_point(a, b):
		w = do_proj(a.o, b.o, a.h, b.h.perp())

		la = a.h.norm()
		lb = b.h.norm()

		za = a.h.unit().dot(w - a.o)
		zb = b.h.unit().dot(w - b.o)

		if za > 0 and za < la and zb > 0 and zb < lb: # idc rn
			return za, b.h.prep().unit() # perp in the other direction
		return la, b.h*0