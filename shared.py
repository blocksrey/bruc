from v2 import V2

GLOBAL_ACCELERATION=V2(0,-128)

#projectile with drag (only accurate for small t)
def aero_projectile(p,v,g,k,t):
	a=g#-k*v.norm()*v#global acceleration+drag
	return p+t*v+0.5*t*t*a,v+t*a#p(t),p'(t)
