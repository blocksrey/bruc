def do_proj(a, b, i, j):
	ij = i.dot(j)
	if ij > 0:
		return a + i*(b - a).dot(j)/ij
	return a + i

class Ray2:
	def __init__(ray2, o, h):
		ray2.o, ray2.h = o, h

	def project_ray(a, b):
		w = do_proj(a.o, b.o, a.h, b.h.perp())

		la = a.h.norm()
		lb = b.h.norm()

		za = a.h.unit().dot(w - a.o)
		zb = b.h.unit().dot(w - b.o)

		if za > 0 and za < la and zb > 0 and zb < lb: # idc rn
			print("norm: ", b.h.y, -b.h.x)
			return za
		return la