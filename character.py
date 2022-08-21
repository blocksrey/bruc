from v2 import V2,null2,cang
from r2 import R2
from geometry import Block
from m2 import push_point,project_point
from math import sin,pi
import pyglet
from v3 import null3
from caller import Caller
from shared import *

characters=[]

class Character:
	def __init__(self,p,v,c):
		#character stuff
		self.p,self.v=p,v
		self.c=c
		self.t=null2
		self.cj=0#this is wrong
		self.tick=0
		#self.label=pyglet.text.Label('ASDASDAS',x=400,y=400,anchor_x='center',anchor_y='center')

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
		self.block.transform(p+V2(abs(1-2*x)-0.5,1+abs(s)),cang(0.3*s),V2(1,2),self.c,1)#negate the cang input for shougaisha mode

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

	def use(self):
		global the_character
		the_character=self
		print('use character',self)

	def unuse(self):
		pass

def step(dt):
	for character in characters:
		character.step(dt)