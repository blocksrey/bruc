from v2 import cang
from spring import Spring
import character

class Camera:
	def __init__(self,p,v):
		self.sp=Spring(p,v)
		self.sa=Spring(0,0)
		self.d=100

	def step(self,dt):
		self.sp.step(character.the_character.p,16,0.5,dt)
		self.sa.step(0,24,0.4,dt)
		self.p=self.sp.p
		self.o=cang(self.sa.p)

	def impulse(self,p,v):
		self.sp.v+=0.1*v
		self.sa.v+=0.0002*(p-self.p).prep().dot(v)#moment of inertia is arbitrarily picked

	def use(self):
		global the_camera
		the_camera=self

def impulse(*a):
	the_camera.impulse(*a)

def step(dt):
	the_camera.step(dt)