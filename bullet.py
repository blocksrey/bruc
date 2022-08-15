from geometry import Block
from m2 import push_point
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
		h,n=push_point(r2(b,d))

		l=d.norm()
		if h+1e-6<l:
			p=b+(h-1e-6)/l*d
			v=0.5*v.reflect(n)#energy reduction
			camera.impulse(p,0.1*v)#cam gets some of the energy

		#bullet geometry (super elegant ngl)
		d=p-b
		h=0.5
		w=d.norm() or h#lol
		self.block.transform(p+0.5*d,d/w,v2(h+w,h),v3(1,0,0),(1)*0.5*pi*h/(0.5*pi*h+2*w))

		self.p,self.v=p,v

def step(dt):
	for bullet in bullets:
		bullet.step(dt)