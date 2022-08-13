from v2 import v2,null2,cang
from r2 import r2
from block import Block
from collidable import raycast
from math import sin,pi
import camera

GLOBAL_ACCELERATION=v2(0,-128)

#projectile with drag (only accurate for small t)
def aero_projectile(p,v,g,k,t):
	a=g-k*v.norm()*v#global acceleration+drag
	return p+t*v+0.5*t*t*a,v+t*a#p(t),p'(t)

characters=[]

class Character:
	def __init__(self,p,v,c):
		#character stuff
		self.p,self.v=p,v
		self.c=c
		self.m=null2
		self.t=null2
		self.cj=0#this is wrong
		self.tick=0
		self.gv=null2
		self.n=null2

		#geometry
		self.block=Block()

		#append so it does something i guess
		characters.append(self)

	def __del__(self):
		return
		print('del',self)

	def step(self,dt):
		p,v=self.p,self.v
		self.tick+=dt

		p+=32*dt*self.t
		b=p
		p,v=aero_projectile(p,v,(GLOBAL_ACCELERATION+32*self.t).project(self.n),0.005,dt)
		d=p-b
		l=d.norm()
		h,n=raycast(r2(b,d))

		if h+1e-6<l:
			#print('a')
			#these are quantitatively the same but numerical stability is vastly different... (unstable one is faster but horrible for shallow angles)
			p=b+h/l*d+1e-6*n
			#p=b+(h-1e-6)/l*d
			#p=b+(h-1e-6)/l*d
			v=v.project(n)

		#animate
		x=2*self.tick%1
		s=sin(2*pi*x)
		self.block.transform(p+v2(abs(1-2*x)-0.5,1+abs(s)),cang(0.3*s),v2(1,2),self.c,1)#negate the cang input for shougaisha mode

		self.p,self.v=p,v

	def jump(self):
		if self.cj:
			self.cj=0#debounce
			self.v.y+=36

	def fat(self,t):
		self.t=v2(t,0)

	def use(self):
		global active_character
		active_character=self
		print('use character',self)

def step(dt):
	for character in characters:
		character.step(dt)