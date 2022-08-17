import v2
from spring import Spring
import character

class Camera:
	def __init__(self,p,v):
		self.sp=Spring(p,v)
		self.sa=Spring(0,0)
		self.d=100

	def step(self,dt):
		self.sp.step(character.active_character.p,16,0.5,dt)
		self.sa.step(0,24,0.4,dt)
		self.p=self.sp.p
		self.o=v2.cang(self.sa.p)

	def impulse(self,p,v):
		self.sp.v+=0.1*v
		self.sa.v+=0.0002*(p-self.p).prep().dot(v)#moment of inertia is arbitrarily picked

import v2
active_camera=Camera(v2.v2(0,0),v2.v2(0,0))

def impulse(*a):
	active_camera.impulse(*a)

def step(dt):
	active_camera.step(dt)