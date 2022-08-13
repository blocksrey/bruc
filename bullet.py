from block import Block
from collidable import raycast
from v2 import v2
from v3 import v3
from r2 import r2
from math import pi
import camera

GLOBAL_ACCELERATION=v2(0,-128)

#projectile with drag (only accurate for small t)
def aero_projectile(p,v,g,k,t):
	a=g-k*v.norm()*v#global acceleration+drag
	return p+t*v+0.5*t*t*a,v+t*a#p(t),p'(t)

bullets=[]

class Bullet:
	def __init__(self,p,v):
		self.p,self.v=p,v
		self.block=Block()
		bullets.append(self)

	def __del__(self):
		return
		print('del',self)

	def step(self,dt):
		p,v=self.p,self.v

		b=p
		p,v=aero_projectile(p,v,GLOBAL_ACCELERATION,0.005,dt)

		d=p-b
		h,n=raycast(r2(b,d))

		l=d.norm()
		if h+1e-6<l:
			p=b+h/l*d
			v=0.5*v.reflect(n)#energy reduction
			camera.impulse(p,0.1*v)#cam gets some of the energy

		#bullet geometry (super elegant ngl)
		d=p-b
		h=d.norm()
		r=0.1
		self.block.transform(p,d/h,v2(h,2*r),v3(1,0,0),(6)*pi*r/(pi*r+2*h))

		self.p,self.v=p,v

def step(dt):
	for bullet in bullets:
		bullet.step(dt)