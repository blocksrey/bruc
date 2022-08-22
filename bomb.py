from geometry import Block
from m2 import push_point
from v2 import V2
from v3 import V3
from r2 import R2
from math import pi
import camera
import pyglet
from explosion import Explosion

GLOBAL_ACCELERATION=V2(0,-96)

#projectile with drag (only accurate for small t)
def aero_projectile(p,v,g,k,t):
	a=g#-k*v.norm()*v#global acceleration+drag
	return p+t*v+0.5*t*t*a,v+t*a#p(t),p'(t)

bombs=[]

class Bomb:
	def __init__(self,p,v):
		self.p,self.v=p,v
		self.t=3
		self.block=Block()
		self.block.transform(p,V2(1,0),V2(0,0),V3(0,0,0),0)
		bombs.append(self)

	def remove(self):
		bombs.remove(self)

	def __del__(self):
		return
		print('del',self)

	def step(self,dt):
		p,v=self.p,self.v

		b=p
		p,v=aero_projectile(p,v,GLOBAL_ACCELERATION,0.005,dt)

		d=p-b
		r=R2(b,d)
		h,n=push_point(r)

		if h+1e-6<r.l:
			if v.square()>1:
				the_sound=pyglet.media.load('sounds/bump.wav').play()
				the_sound.volume=v.norm()/100
				the_sound.pitch=0.9+0.002*v.norm()

			p=b+(h-1e-6)/r.l*d
			camera.impulse(p,v)#cam gets some of the energy
			#v=v.reflect(0.3*n)#LMAO
			v=0.5*v.reflect(n)#energy reduction

		#bomb geometry (super elegant ngl)
		d=p-b
		h=1
		w=d.norm() or h#lol
		self.block.transform(p+0.5*d,d/w,V2(h+w,h),V3(0,0.2,0),(2)*0.5*pi*h/(0.5*pi*h+2*w))

		self.p,self.v=p,v

		self.t-=dt
		if self.t<=0:
			Explosion(self.p)
			self.remove()
			#self.block.remove()

import network

def _(socket,p,v):
	Bomb(p,v)
network.on_receive('newbomb').connect(_)

def step(dt):
	for bomb in bombs:
		bomb.step(dt)