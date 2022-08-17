from geometry import Block
from m2 import push_point
from v2 import v2
from v3 import v3
from r2 import r2
from math import pi
import camera

import pyglet

GLOBAL_ACCELERATION=v2(0,-128)

#projectile with drag (only accurate for small t)
def aero_projectile(p,v,g,k,t):
	a=g-k*v.norm()*v#global acceleration+drag
	return p+t*v+0.5*t*t*a,v+t*a#p(t),p'(t)

bullets=[]

class Bullet:
	def __init__(self,p,v):
		self.p,self.v=p,v
		self.t=2
		self.block=Block()
		bullets.append(self)

	def remove(self):
		bullets.remove(self)

	def __del__(self):
		return
		print('del',self)

	def step(self,dt):
		p,v=self.p,self.v

		b=p
		p,v=aero_projectile(p,v,GLOBAL_ACCELERATION,0.005,dt)

		d=p-b
		r=r2(b,d)
		h,n=push_point(r)

		if h+1e-6<r.l:
			the_sound=pyglet.media.load('sounds/bump.wav').play()
			the_sound.volume=v.norm()/100
			the_sound.pitch=1+0.001*v.norm()

			p=b+(h-1e-6)/r.l*d
			camera.impulse(p,v)#cam gets some of the energy
			v=0.5*v.reflect(n)#energy reduction

		#bullet geometry (super elegant ngl)
		d=p-b
		h=0.5
		w=d.norm() or h#lol
		self.block.transform(p+0.5*d,d/w,v2(h+w,h),v3(1,0,0),(1)*0.5*pi*h/(0.5*pi*h+2*w))

		self.p,self.v=p,v

		self.t-=dt
		if self.t<=0:
			self.remove()
			#self.block.remove()

def step(dt):
	for bullet in bullets:
		bullet.step(dt)