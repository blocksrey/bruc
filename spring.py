#blocksrey
from math import cos,sin,exp,sqrt

def analytical_spring(p,v,b,k,d,t):#position,velocity,target,constant,dampness,time
	h=sqrt(1-d*d)
	s=sin(h*k*t)
	c=h*cos(h*k*t)#not really c, more like hc
	y=h*exp(d*k*t)#more like hy i guess
	return b+(k*(c+s*d)*(p-b)+s*v)/(k*y),(k*s*(b-p)+(c-s*d)*v)/y#assuming k>0&&d<1

class spring:
	def __init__(self,p,v):
		self.p,self.v=p,v

	def step(self,b,k,d,dt):
		self.p,self.v=analytical_spring(self.p,self.v,b,k,d,dt)#pretty simple eh?