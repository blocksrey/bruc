# Blocksrey

from math import cos, sin, pow, sqrt, e

def analytical_spring(p, v, b, k, d, t): # position, velocity, target, constant, dampness, time
	h = sqrt(1 - d*d)
	s = sin(h*k*t)
	c = h*cos(h*k*t) # not really c, more like hc
	y = h*pow(e, d*k*t) # more like hy i guess

	return b + (k*(p - b)*(c + d*s) + v*s)/(k*y), (k*(b - p)*s + v*(c - d*s))/y # assuming k > 0 && d < 1

class Spring:
	def __init__(self, p, v):
		self.p, self.v = p, v

	def step(self, b, k, d, dt):
		self.p, self.v = analytical_spring(
			self.p,
			self.v,
			b,
			k,
			d,
			dt
		) # pretty simple, eh?