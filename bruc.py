print('start bruc client')

from v2 import v2,null2,cang
from v3 import v3,null3
from math import cos,sin,atan2,sqrt
import pyglet
from pyglet.gl import *
from glutil import *
from caller import caller

the_window=pyglet.window.Window(222,173,'bruc')#easter egg much?

on_key_press_caller=caller()
@the_window.event
def on_key_press(code,mod):
	on_key_press_caller.fire(code,mod)

on_key_release_caller=caller()
@the_window.event
def on_key_release(code,mod):
	on_key_release_caller.fire(code,mod)

on_mouse_scroll_caller=caller()
@the_window.event
def on_mouse_scroll(px,py,dx,dy):
	on_mouse_scroll_caller.fire(px,py,dx,dy)

on_mouse_press_caller=caller()
@the_window.event
def on_mouse_press(px,py,code,mod):
	on_mouse_press_caller.fire(px,py,code,mod)

on_mouse_motion_caller=caller()
@the_window.event
def on_mouse_release(px,py,code,mod):
	on_mouse_motion_caller.fire(px,py,code,mod)

on_draw_caller=caller()
@the_window.event
def on_mouse_motion(px,py,dx,dy):
	on_mouse_motion_caller.fire(px,py,dx,dy)

on_draw_caller=caller()
@the_window.event
def on_draw():
	on_draw_caller.fire()

on_resize_caller=caller()
@the_window.event
def on_resize(sx,sy):
	on_resize_caller.fire(sx,sy)



SMALL=1e-6
VAO_MODE=gl_info.have_version(2) and 0
GLOBAL_ACCELERATION=v2(0,-128)

RELEASE=0
if RELEASE:
	import gc
	gc.disable()#no garbage collection
	pyglet.options['debug_gl']=False#no debug

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
glClearColor(1,1,1,1)



camp=null2
camd=1
camo=v2(1,0)







class State:
	def __init__(*_):
		pass

	def set(*_):
		pass

	def on(*_):
		return caller()

	def call(*_):
		pass

	def depend(*_):
		pass

state0=State()







#this might change my life
class Sequencer:
	def __init__(sequencer):
		sequencer.queue=[]

	def call(sequencer,time):
		sequencer.queue.append(time)

	def dump(sequencer,time):
		#print(sequencer.queue)
		pass



ammo=3

lastshot=0
def get_cooldown(et):
	lastshot=et
	print('shoot @',t)
	return 0.1

sequencer0=Sequencer()

sequencer0.dump(3)
sequencer0.call(get_cooldown)
sequencer0.dump(3.1)



















from mesh2 import Mesh2


rectangle_l=0
rectangle_p=[]
rectangle_c=[]
collision_meshes=[]

class Terrain:
	def __init__(self,p,s,c):
		global rectangle_l

		self.i=rectangle_l

		rectangle_l+=1
		rectangle_p.extend( 8*[None])
		rectangle_c.extend(12*[None])

		collision_meshes.append(Mesh2([null2]))

		self.kawatte(p,s,c)

	def kawatte(self,p,s,c):
		i=self.i
		px,py=p.x,p.y
		sx,sy=s.x,s.y
		cx,cy,cz=c.x,c.y,c.z

		i8=8*i
		rectangle_p[i8+0]=px+1*sx
		rectangle_p[i8+1]=py+1*sy
		rectangle_p[i8+2]=px+1*sx
		rectangle_p[i8+3]=py+0*sy
		rectangle_p[i8+4]=px+0*sx
		rectangle_p[i8+5]=py+0*sy
		rectangle_p[i8+6]=px+0*sx
		rectangle_p[i8+7]=py+1*sy

		i12=12*i
		rectangle_c[i12+ 0]=cx
		rectangle_c[i12+ 1]=cy
		rectangle_c[i12+ 2]=cz
		rectangle_c[i12+ 3]=cx
		rectangle_c[i12+ 4]=cy
		rectangle_c[i12+ 5]=cz
		rectangle_c[i12+ 6]=cx
		rectangle_c[i12+ 7]=cy
		rectangle_c[i12+ 8]=cz
		rectangle_c[i12+ 9]=cx
		rectangle_c[i12+10]=cy
		rectangle_c[i12+11]=cz

		collision_meshes[i].update_vertices([
			v2(px+1*sx,py+1*sy),
			v2(px+1*sx,py+0*sy),
			v2(px+0*sx,py+0*sy),
			v2(px+0*sx,py+1*sy)
		])















if VAO_MODE:
	rectangle_program=Program(
		Shader('shaders/rectv.glsl',GL_VERTEX_SHADER),
		Shader('shaders/rectf.glsl',GL_FRAGMENT_SHADER)
	)

	rectangle_camd_uniform=glGetUniformLocation(rectangle_program.id,b'camd')
	rectangle_camp_uniform=glGetUniformLocation(rectangle_program.id,b'camp')
	rectangle_camo_uniform=glGetUniformLocation(rectangle_program.id,b'camo')
	rectangle_wins_uniform=glGetUniformLocation(rectangle_program.id,b'wins')

	def draw_rects():
		pyglet.graphics.draw(
			4*rectangle_l,
			GL_QUADS,
			('v2f',rectangle_p),
			('c3f',rectangle_c)
		)
else:
	def draw_rects():
		for i in range(rectangle_l):
			i12=12*i
			glColor4f(rectangle_c[i12+0],rectangle_c[i12+1],rectangle_c[i12+2],1)

			i8=8*i
			glVertex2f(rectangle_p[i8+0],rectangle_p[i8+1])
			glVertex2f(rectangle_p[i8+2],rectangle_p[i8+3])
			glVertex2f(rectangle_p[i8+4],rectangle_p[i8+5])
			glVertex2f(rectangle_p[i8+6],rectangle_p[i8+7])









from math import tan,pi

def glPerspective(t,r,n,f):
		h=tan(pi/180*t)*n
		w=r*h
		glFrustum(-w,w,-h,h,n,f)





bullet_l=0
bullet_p=[]
bullet_o=[]

if VAO_MODE:
	bullet_program=Program(
		Shader('shaders/bulletv.glsl',GL_VERTEX_SHADER),
		Shader('shaders/bulletf.glsl',GL_FRAGMENT_SHADER)
	)

	bullet_camd_uniform=glGetUniformLocation(bullet_program.id,b'camd')
	bullet_camp_uniform=glGetUniformLocation(bullet_program.id,b'camp')
	bullet_camo_uniform=glGetUniformLocation(bullet_program.id,b'camo')
	bullet_wins_uniform=glGetUniformLocation(bullet_program.id,b'wins')

	def draw_bullets():
		pyglet.graphics.draw(
			4*bullet_l,
			GL_QUADS,
			('v2f',bullet_p)
		)
else:
	def draw_bullets():
		for i in range(bullet_l):
			glColor4f(1,0,0,bullet_o[i])

			i8=8*i
			glVertex2f(bullet_p[i8+0],bullet_p[i8+1])
			glVertex2f(bullet_p[i8+2],bullet_p[i8+3])
			glVertex2f(bullet_p[i8+4],bullet_p[i8+5])
			glVertex2f(bullet_p[i8+6],bullet_p[i8+7])







def hsv(h,s,v):
	c=v*s
	m=v-c
	h*=6
	x=m+c*(1-abs(h%2-1))
	c+=m
	if   h<1:return c,x,m
	elif h<2:return x,c,m
	elif h<3:return m,c,x
	elif h<4:return m,x,c
	elif h<5:return x,m,c
	else:    return c,m,x



#this should be a standard
def calc_skin_color(a):
	h=0.25*(1-a)*a
	s=0.25+0.5*a
	v=1-0.75*a
	return hsv(h,s,v)

def calc_clothing_color(a,b,c,d):
	h0=a+2*a*(a-1)**4
	s0=1-b
	v0=0.5*(1-c*c)
	h1=b+2*b*(b-1)**4
	s1=0.66*c**1.5
	v1=0.34*(1+d)*(1-d*d)
	return hsv(h0,s0,v0),hsv(h1,s1,v1)












#i need to work on state (user input's affect on the system)



characters=[]

characters_l=0
characters_p=[]
characters_c=[]

class Character:
	def __init__(self,p,v,c):
		#character stuff
		self.p,self.v=p,v
		self.c=c
		self.m=null2
		self.t=null2

		#geometry
		global characters_l
		self.i=characters_l
		characters_l+=1
		characters_p.extend( 8*[None])
		characters_c.extend(12*[None])

		#append so it does something i guess
		characters.append(self)

	def kawatte(self,i,p,o,c):
		px,py=p.x,p.y
		cx,cy,cz=c.x,c.y,c.z

		h=2
		r=0.5

		c,s=-o.y,o.x

		hc,hs=h*c,h*s
		rc,rs=r*c,r*s

		i8=i*8
		characters_p[i8+0]=px-rs+hc
		characters_p[i8+1]=py+rc+hs

		characters_p[i8+2]=px-rs
		characters_p[i8+3]=py+rc

		characters_p[i8+4]=px+rs
		characters_p[i8+5]=py-rc

		characters_p[i8+6]=px+rs+hc
		characters_p[i8+7]=py-rc+hs

		i12=12*i
		characters_c[i12+ 0]=cx
		characters_c[i12+ 1]=cy
		characters_c[i12+ 2]=cz
		characters_c[i12+ 3]=cx
		characters_c[i12+ 4]=cy
		characters_c[i12+ 5]=cz
		characters_c[i12+ 6]=cx
		characters_c[i12+ 7]=cy
		characters_c[i12+ 8]=cz
		characters_c[i12+ 9]=cx
		characters_c[i12+10]=cy
		characters_c[i12+11]=cz

	def step(self,dt):
		p,v=self.p,self.v
		b=p#before p

		v.x+=(self.t.x-v.x)*dt*10
		p.x+=v.x*dt*20

		p,v=aero_projectile(p,v,GLOBAL_ACCELERATION,0.005,dt)

		d=p-b
		cz,cn=map_raycast(r2(b,d))
		if d.norm()-cz>SMALL:#touch
			p=b+cz*d.unit()+SMALL*cn
			v=v.project(cn)
			self.cj=1
		else:#float
			self.cj=0

		#animate
		characters_tick=14*self.t.norm()*tick
		s=sin(characters_tick)
		self.kawatte(self.i,p+v2(0,s*s),cang(0.2*s),self.c)

		self.p,self.v=p,v

	def jump(self):
		if self.cj:
			self.v.y+=40

	def fat(self,t):
		self.t=v2(t,0)

	def use(self):
		global the_guy
		the_guy=self
		print('use character',self)

if VAO_MODE:
	def draw_characters():
		pyglet.graphics.draw(
			4*characters_l,
			GL_QUADS,
			('v2f',characters_p),
			('c3f',characters_c)
		)
else:
	import ctypes

	def draw_characters():
		for i in range(characters_l):
			i12=12*i
			glColor4f(characters_c[i12+0],characters_c[i12+1],characters_c[i12+2],1)

			i8=8*i
			glVertex2f(characters_p[i8+0],characters_p[i8+1])
			glVertex2f(characters_p[i8+2],characters_p[i8+3])
			glVertex2f(characters_p[i8+4],characters_p[i8+5])
			glVertex2f(characters_p[i8+6],characters_p[i8+7])






















char_c={}
char_c['w']=v3(0,0.75,0)
char_c['C']=v3(0.5,0.5,0.5)
char_c['-']=v3(0.8,0.8,0.8)

char_c['^']=v3(1,0,0)
char_c['>']=v3(1,0,0)
char_c['<']=v3(1,0,0)

char_c['J']=v3(1,0,1)

char_c['|']=v3(0.5,0.75,1)

char_c['W']=v3(0.2,0.4,1)

char_c['P']=v3(1,1,0)

def build_map(path):
	iy=0
	for row in open(path).readlines():
		ix1=0

		ix=0
		ch=row[0]

		for ch1 in row:
			if ch!=ch1:
				sx=ix1-ix

				px,py=2*ix,-4*iy
				sx,sy=2*sx,4

				if ch=='-':
					Terrain(v2(px,py+0.9*sy),v2(sx,0.1*sy),char_c[ch])
				elif ch!=' ':#newline case is handled naturally :P:P
					Terrain(v2(px,py),v2(sx,sy),char_c[ch])

				if ch=='P':
					Character(v2(px,py+10),v2(0,1),v3(*calc_skin_color(random()))).use()

				ix=ix1
				ch=ch1

			ix1+=1
		iy+=1








from math import inf

def map_raycast(r):
	fz=r.h.norm()
	fn=null2
	for rectm in collision_meshes:
		cz,cn=rectm.push_point(r)
		if cz<fz:
			fz=cz
			fn=cn
	return fz,fn











bullets=[]


from r2 import r2

#projectile with drag (only accurate for small t)
def aero_projectile(p,v,g,k,t):
	a=g-k*v.norm()*v
	return p+t*v+0.5*t*t*a,v+t*a#p,p'

class Bullet:
	def __init__(self,p,v):
		#projectile
		self.p,self.v=p,v

		#geometry
		global bullet_l
		self.i=bullet_l
		bullet_l+=1
		bullet_p.extend(8*[None])
		bullet_o.extend(1*[None])

		#bullshit
		self.step(null2,0,0.00001)

		#add to stepper
		bullets.append(self)

	def step(self,g,k,dt):
		p,v=self.p,self.v#in
		b=p
		p,v=aero_projectile(p,v,g,k,dt)
		cz,cn=map_raycast(r2(b,p-b))
		d=p-b
		if d.norm()-cz>SMALL:
			p=b+cz*d.unit()
			v=0.75*v.reflect(cn)#energy reduction
		self.kawatte(self.i,p,dt*v)
		self.p,self.v=p,v#out

	def kawatte(self,i,p,d):
		px,py=p.x,p.y
		dx,dy=d.x,d.y

		h=sqrt(dx*dx+dy*dy)
		r=0.2

		c,s=dx/h,dy/h#cos,sin

		hc,hs=h*c,h*s
		rc,rs=r*c,r*s

		i8=8*i
		bullet_p[i8+0]=px-rs+hc
		bullet_p[i8+1]=py+rc+hs
		bullet_p[i8+2]=px-rs
		bullet_p[i8+3]=py+rc
		bullet_p[i8+4]=px+rs
		bullet_p[i8+5]=py-rc
		bullet_p[i8+6]=px+rs+hc
		bullet_p[i8+7]=py-rc+hs

		bullet_o[i]=(6)*pi*r/(pi*r+2*h)#whatever*(circular_area ./ h->0)/circular_area

	def destroy():
		pass



from time import time
from random import random

build_map('maps/map0.bm')

camo=cang(0)
camd=100

from spring import spring
cam_spring=spring(v2(0,0),v2(0,0))
cam_spring.step(v2(0,0),0.1,0.1,0.1)

def step(dt):
	dt=max(SMALL,dt)#this isnt so nice

	global tick
	tick=time()#GET LEFT OVER FRAME TIME OR SOMETHING (FOR EVENTS) INSTEAD OF DOING THIS TIME SHIT

	for bullet in bullets:
		bullet.step(GLOBAL_ACCELERATION,0.005,dt)

	for character in characters:
		character.step(dt)

	global camp
	camp=the_guy.p

pyglet.clock.schedule(step)#this is bad but whatever





def update_wins_uniforms(wins):
	glUseProgram(rectangle_program.id)
	glUniform2f(rectangle_wins_uniform,wins.x,wins.y)

	glUseProgram(bullet_program.id)
	glUniform2f(bullet_wins_uniform,wins.x,wins.y)

#state0.on('draw','wins').connect(update_wins_uniforms)#on draw (if wins is different since last draw)



#def use_rectangle_program():
#	glUseProgram(rectangle_program.id)

#rectangle_uniform_change=state0.depend('rectangle_camp_uniform','rectangle_camo_uniform')
#rectangle_uniform_change.before.connect(use_rectangle_program)






if VAO_MODE:
	def _(sx,sy):
		#state0.set('wins',v2(sx,sy))
		update_wins_uniforms(v2(sx,sy))
	on_resize_caller.connect(_)

	def draw_scene():
		glClear(GL_COLOR_BUFFER_BIT)#can't make this assumption (i want better state management)

		#render rects
		glUseProgram(rectangle_program.id)
		glUniform1f(rectangle_camd_uniform,camd)
		glUniform2f(rectangle_camp_uniform,camp.x,camp.y)
		glUniform2f(rectangle_camo_uniform,camo.x,camo.y)
		draw_rects()

		draw_characters()

		#render bullets
		glUseProgram(bullet_program.id)
		glUniform1f(bullet_camd_uniform,camd)
		glUniform2f(bullet_camp_uniform,camp.x,camp.y)
		glUniform2f(bullet_camo_uniform,camo.x,camo.y)
		draw_bullets()
else:
	def draw_scene():
		glClear(GL_COLOR_BUFFER_BIT)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glPerspective(45,the_window.width/the_window.height,0.1,1000)

		glRotatef(180/pi*atan2(-camo.y,camo.x),0,0,1)
		glTranslatef(-camp.x,-camp.y,-camd)

		glBegin(GL_QUADS)

		draw_rects()
		draw_bullets()
		draw_characters()

		glEnd()

#state0.on('draw').connect(draw_scene)


























m0x,m0y=0,0
m1x,m1y=0,0



label=pyglet.text.Label('hello world',font_size=40,x=0.5*the_window.width,y=0.5*the_window.height)
label.color=(0,0,0,255)







def _():
	#state0.call('draw')
	draw_scene()

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0,the_window.width,0,the_window.height,-1,1)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	label.draw()
on_draw_caller.connect(_)

def _(code,mod):
	key=chr(code)
	if key==' ':
		the_guy.jump()
	else:
		the_guy.fat(key=='d' and 1 or key=='a' and -1 or 0)
on_key_press_caller.connect(_)

def _(code,mod):
	key=chr(code)
	if key!=' ':
		the_guy.fat(key=='d' and 0 or key=='a' and 0 or 0)#this is wrong but whatever lol
on_key_release_caller.connect(_)

def _(px,py,dx,dy):
	global camd
	camd+=2*dy
on_mouse_scroll_caller.connect(_)

def _(px,py,code,mod):
	p=v2(px,py)
	w=v2(the_window.width,the_window.height)
	c=v2(camp.x,camp.y)
	s=c+camd/w.y*(2*p-w)
	Bullet(the_guy.p,200*(s-the_guy.p).unit())
on_mouse_press_caller.connect(_)

def _(sx,sy):
	glViewport(0,0,sx,sy)
on_resize_caller.connect(_)




























pyglet.app.run()