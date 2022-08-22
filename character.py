from v2 import V2,null2,cang
from r2 import R2
from geometry import Block
from m2 import push_point,project_point
from math import sin,pi
import pyglet
from v3 import V3,null3
from caller import Caller
from random import random

GLOBAL_ACCELERATION=V2(0,-150)

#projectile with drag (only accurate for small t)
def aero_projectile(p,v,g,k,t):
	a=g#-k*v.norm()*v#global acceleration+drag
	return p+t*v+0.5*t*t*a,v+t*a#p(t),p'(t)

characters=[]

class Character:
	def __init__(self,p,v,c):
		#character stuff
		self.p,self.v=p,v
		self.c=c
		self.t=null2
		self.cj=0#this is wrong
		self.tick=0

		self.name='bonnnaa'
		#self.label=pyglet.text.Label(self.name,font_size=16,x=0,y=0,anchor_x='center',anchor_y='center')

		self.health=1
		self.impulse_time=100000000

		#geometry
		self.block=Block()

		#append so it does something i guess
		characters.append(self)

	def __del__(self):
		return
		print('del',self)

	def step(self,dt):
		#in
		p,v=self.p,self.v

		r=0.5
		l,c=project_point(p)
		#print(p.x==c.x)
		n=null2
		if l+1e-6<r:
			n=(p-c).unit()
			p=c+r*n
			#print('a')
		else:
			pass#print('ASDAS')

		b=p
		p,v=aero_projectile(p,v.project(n),GLOBAL_ACCELERATION.project(n),0.005,dt)
		d=p-b
		r=R2(b,d)
		h,n=push_point(r)

		#if n.dot(V2(0,1))>0.7:

		if h+1e-6<r.l:
			#these are quantitatively similar but numerical stability is vastly different... (unstable one is faster but horrible for shallow angles)
			p=b+h/r.l*d+1e-6*n
			#p=b+(h-1e-6)/r.l*d
			v=v.project(n)

		#animate
		self.tick+=dt
		x=2*self.tick%1
		s=sin(2*pi*x)

		c0=self.c

		self.impulse_time+=dt
		self.block.transform(p+V2(abs(1-2*x)-0.5,1+abs(s)),cang(0.3*s),V2(1,2),c0+(V3(1,0,0)-c0)/(self.impulse_time*30),1)#negate the cang input for shougaisha mode

		#self.label.draw()

		#out
		self.p,self.v=p,v

	def jump(self):
		if self.cj:
			pyglet.media.load('sounds/jump.ogg').play()
			self.cj=0#debounce
			self.v.y+=36

	def fat(self,t):
		self.t=V2(t,0)

	def impulse(self,impact):
		self.v+=impact
		dd=impact.square()
		if dd>14:
			self.health-=1e-4*dd#lmao
			self.impulse_time=0

			oto=pyglet.media.load('sounds/hurt'+str(int(3*random()))+'.mp3').play()
			oto.pitch=0.9+0.1*random()

			if self.health<=0:
				print(self,'dead')
				return 1

	def use(self):
		global the_character
		the_character=self
		print('use character',self)

	def unuse(self):
		pass

def step(dt):
	for character in characters:
		character.step(dt)