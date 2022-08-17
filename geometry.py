from pyglet.gl import *
from pyglet.graphics import draw
from glutil import *
from events import *
from camera import active_camera
from v2 import v2
from m2 import m2

block_l=0
block_p=[]
block_c=[]

class Collidable:
	def __init__(self,p,o,s,c,a):
		self.block=Block()
		self.m2=m2(4)
		self.transform(p,o,s,c,a)

	def __del__(self):
		return
		print('del',self)

	def transform(self,p,o,s,c,a):
		self.block.transform(p,o,s,c,a)
		i8=8*self.block.i
		self.m2.update_vertices([
			v2(block_p[i8+0],block_p[i8+1]),
			v2(block_p[i8+2],block_p[i8+3]),
			v2(block_p[i8+4],block_p[i8+5]),
			v2(block_p[i8+6],block_p[i8+7])
		])

class Block:
	def __init__(self):
		global block_l
		self.i=block_l
		block_l+=1
		block_p.extend( 8*[None])
		block_c.extend(16*[None])

	def remove():
		pass

	def __del__(self):
		return
		print('del',self)

	def transform(self,p,o,s,c,a):
		rx,ry=0.5*s.x,0.5*s.y
		r,g,b=c.x,c.y,c.z
		i8 = 8*self.i
		i16=16*self.i
		block_p[i8+0],block_p[i8+1]=(p+o.cmul(v2(+rx,+ry))).dump()
		block_p[i8+2],block_p[i8+3]=(p+o.cmul(v2(+rx,-ry))).dump()
		block_p[i8+4],block_p[i8+5]=(p+o.cmul(v2(-rx,-ry))).dump()
		block_p[i8+6],block_p[i8+7]=(p+o.cmul(v2(-rx,+ry))).dump()
		block_c[i16+ 0],block_c[i16+ 1],block_c[i16+ 2],block_c[i16+ 3]=r,g,b,a
		block_c[i16+ 4],block_c[i16+ 5],block_c[i16+ 6],block_c[i16+ 7]=r,g,b,a
		block_c[i16+ 8],block_c[i16+ 9],block_c[i16+10],block_c[i16+11]=r,g,b,a
		block_c[i16+12],block_c[i16+13],block_c[i16+14],block_c[i16+15]=r,g,b,a

VAO_MODE=gl_info.have_version(2) and 0

if VAO_MODE:
	block_program=Program(
		Shader('shaders/blockv.glsl',GL_VERTEX_SHADER),
		Shader('shaders/blockf.glsl',GL_FRAGMENT_SHADER)
	)

	block_camd_uniform=glGetUniformLocation(block_program.id,b'camd')
	block_camp_uniform=glGetUniformLocation(block_program.id,b'camp')
	block_camo_uniform=glGetUniformLocation(block_program.id,b'camo')
	block_wins_uniform=glGetUniformLocation(block_program.id,b'wins')

	def draw_block():
		draw(
			4*block_l,
			GL_QUADS,
			('v2f',block_p),
			('c4f',block_c)
		)

	def _(wins):
		glUseProgram(block_program.id)
		glUniform2f(block_wins_uniform,wins.x,wins.y)
	on_resize_caller.connect(_)

	def draw_scene():
		glClear(GL_COLOR_BUFFER_BIT)#can't make this assumption (i want better state management)

		#render block
		glUseProgram(block_program.id)
		glUniform1f(block_camd_uniform,active_camera.d)
		glUniform2f(block_camp_uniform,active_camera.p.x,active_camera.p.y)
		glUniform2f(block_camo_uniform,active_camera.o.x,active_camera.o.y)
		draw_block()
else:
	from math import tan,pi,atan2

	def glPerspective(t,r,n,f):
		h=tan(pi/180*t)*n
		w=r*h
		glFrustum(-w,w,-h,h,n,f)

	def draw_block():
		for i in range(block_l):
			i16=16*i
			glColor4f(block_c[i16+0],block_c[i16+1],block_c[i16+2],block_c[i16+3])

			i8=8*i
			glVertex2f(block_p[i8+0],block_p[i8+1])
			glVertex2f(block_p[i8+2],block_p[i8+3])
			glVertex2f(block_p[i8+4],block_p[i8+5])
			glVertex2f(block_p[i8+6],block_p[i8+7])

	def draw_scene():
		glClear(GL_COLOR_BUFFER_BIT)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glPerspective(45,the_window.width/the_window.height,0.1,1000)

		glRotatef(180/pi*atan2(-active_camera.o.y,active_camera.o.x),0,0,1)
		glTranslatef(-active_camera.p.x,-active_camera.p.y,-active_camera.d)

		glBegin(GL_QUADS)
		draw_block()
		glEnd()