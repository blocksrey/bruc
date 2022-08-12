print('start bruc client')

import pyglet
from pyglet.gl import *
from v2 import v2,null2,cang
from v3 import v3,null3
from math import sin,atan2,sqrt,inf,tan,pi
from glutil import *
from caller import caller
from r2 import r2
from sorty import sorty
from time import time
from random import random
from spacer import spacer
from cm2 import cm2
from spring import spring

the_window=pyglet.window.Window(4*222,4*173,'bruc')#easter egg much?

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
	on_mouse_scroll_caller.fire(v2(px,py),v2(dx,dy))

on_mouse_press_caller=caller()
@the_window.event
def on_mouse_press(px,py,code,mod):
	on_mouse_press_caller.fire(v2(px,py),code,mod)

on_mouse_motion_caller=caller()
@the_window.event
def on_mouse_release(px,py,code,mod):
	on_mouse_motion_caller.fire(v2(px,py),code,mod)

on_draw_caller=caller()
@the_window.event
def on_mouse_motion(px,py,dx,dy):
	on_mouse_motion_caller.fire(v2(px,py),v2(dx,dy))

on_draw_caller=caller()
@the_window.event
def on_draw():
	on_draw_caller.fire()

on_resize_caller=caller()
@the_window.event
def on_resize(sx,sy):
	on_resize_caller.fire(v2(sx,sy))












VAO_MODE=gl_info.have_version(2)
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
camd=50
camo=cang(0)












#this might change my life
class sequencer:
	def __init__(self):
		self.queue=sorty()

	def destroy():
		pass

	def call(self,time):
		self.queue.set('lol',time)
		print('sett')

	def dump(self,time):
		#print(self.queue)
		pass

the_sequencer=sequencer()

ammo=3

lastshot=0
def get_cooldown(et):
	lastshot=et
	print('shoot @',t)
	return 0.1

sequencer0=sequencer()

sequencer0.dump(3)
sequencer0.call(get_cooldown)
sequencer0.dump(3.1)


the_spacer=spacer()


















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

def glPerspective(t,r,n,f):
		h=tan(pi/180*t)*n
		w=r*h
		glFrustum(-w,w,-h,h,n,f)

def map_raycast(r):
	fh=r.l
	fn=null2
	for rectm in collidables:
		h,n=rectm.push_point(r)
		if h<fh:
			fh=h
			fn=n
	return fh,fn













































block_l=0
block_p=[]
block_c=[]

class Block:
	def __init__(self):
		global block_l
		self.i=block_l
		block_l+=1
		block_p.extend( 8*[None])
		block_c.extend(16*[None])
		self.transform(null2,null2,null2,null3,0)

	def destroy():
		pass

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













collidables=[]

class Collidable:#lets do some inheritance
	def __init__(self,p,o,s,c,op):
		self.block=Block()
		collidables.append(cm2([null2]))
		self.transform(p,o,s,c,op)

	def destroy():
		pass

	def transform(self,p,o,s,c,op):
		self.block.transform(p,o,s,c,op)
		i=self.block.i
		i8=8*i
		collidables[i].update_vertices([
			v2(block_p[i8+0],block_p[i8+1]),
			v2(block_p[i8+2],block_p[i8+3]),
			v2(block_p[i8+4],block_p[i8+5]),
			v2(block_p[i8+6],block_p[i8+7])
		])










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
		pyglet.graphics.draw(
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
		glUniform1f(block_camd_uniform,camd)
		glUniform2f(block_camp_uniform,camp.x,camp.y)
		glUniform2f(block_camo_uniform,camo.x,camo.y)
		draw_block()
else:
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

		glRotatef(180/pi*atan2(-camo.y,camo.x),0,0,1)
		glTranslatef(-camp.x,-camp.y,-camd)

		glBegin(GL_QUADS)
		draw_block()
		glEnd()







#i need to work on state (user input's affect on the system)



characters=[]

class Character:
	def __init__(self,p,v,c):
		#character stuff
		self.p,self.v=p,v
		self.c=c
		self.m=null2
		self.t=null2
		self.cj=0#this is wrong

		#geometry
		self.block=Block()

		#append so it does something i guess
		characters.append(self)

	def destroy():
		pass

	def step(self,dt):
		p,v=self.p,self.v

		b=p
		p,v=aero_projectile(p,v,GLOBAL_ACCELERATION,0.005,dt)

		d=p-b
		h,n=map_raycast(r2(b,d))

		l=d.norm()
		if h+1e-6<l:
			#these are quantitatively the same but numerical stability is vastly different... (unstable one is faster but horrible for shallow angles)
			#p=b+h/l*d+1e-6*n
			#p=b+(h-1e-6)/l*d
			p=b+(h-1e-6)/l*d
			v=v.project(n)
			self.cj=n.dot(v2(0,1))>0.7

		#animate
		x=2*tick0%1
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
		global the_guy
		the_guy=self
		print('use character',self)























spawn_locations=[]




char_c={}
char_c['w']=v3(41,200,18)/255
char_c['C']=v3(0.7,0.9,0.7)
char_c['-']=v3(0.8,0.5,0.4)

char_c['^']=v3(242,27,63)/255
char_c['>']=v3(242,27,63)/255
char_c['<']=v3(242,27,63)/255

char_c['J']=v3(255,153,20)/255

char_c['|']=v3(0.5,0.75,1)

char_c['W']=v3(8,189,189)/255

char_c['P']=v3(0,0,0.2)

def build_map(path):
	iy=0
	for row in open(path).readlines():
		ix1=0

		ix=0
		ch=row[0]

		for ch1 in row:
			if ch!=ch1:
				sx=ix1-ix

				p=v2(2*ix,-4*iy)
				s=v2(2*sx,4)

				if ch=='-':
					Collidable(p+0.5*s+v2(0,0.45*s.y),cang(0),v2(s.x,0.1*s.y),char_c[ch],1)
				elif ch!=' ':#newline case is handled naturally :P:P
					Collidable(p+0.5*s,cang(0),s,char_c[ch],1)

				if ch=='P':
					spawn_locations.append(p+0.5*s)

				ix=ix1
				ch=ch1

			ix1+=1
		iy+=1
















bullets=[]

#projectile with drag (only accurate for small t)
def aero_projectile(p,v,g,k,t):
	a=g-k*v.norm()*v#global acceleration+drag
	return p+t*v+0.5*t*t*a,v+t*a#p(t),p'(t)

class Bullet:
	def __init__(self,p,v):
		self.p,self.v=p,v
		self.block=Block()
		bullets.append(self)

	def destroy():
		pass

	def step(self,g,k,dt):
		p,v=self.p,self.v

		b=p
		p,v=aero_projectile(p,v,g,k,dt)

		d=p-b
		h,n=map_raycast(r2(b,d))

		l=d.norm()
		if h+1e-6<l:
			p=b+h/l*d
			v=0.75*v.reflect(n)#energy reduction

		#bullet geometry (super elegant ngl)
		d=p-b
		h=d.norm()
		r=0.1
		self.block.transform(p,d/h,v2(h,2*r),v3(1,0,0),(6)*pi*r/(pi*r+2*h))

		self.p,self.v=p,v



















camp_spring=spring(null2,null2)
cama_spring=spring(0,0)

#the guy & bullets & camera
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

def _(mp,code,mod):
	w=v2(the_window.width,the_window.height)
	s=camp+camd/w.y*(2*mp-w)
	vel=200*(s-the_guy.p).unit()
	Bullet(the_guy.p,vel)
	camp_spring.v-=0.3*vel
	cama_spring.v+=v2(-0.01,0).dot(vel)
on_mouse_press_caller.connect(_)

def _(mp,d):
	global camd
	camd+=2*d.y
on_mouse_scroll_caller.connect(_)














def _():
	draw_scene()

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0,the_window.width,0,the_window.height,-1,1)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	#label.draw()
on_draw_caller.connect(_)

def _(ws):
	glViewport(0,0,ws.x,ws.y)
on_resize_caller.connect(_)
















build_map('maps/map0.bm')
Character(spawn_locations[int(len(spawn_locations)*random())],null2,v3(*calc_skin_color(random()))).use()



def step(dt):
	dt=max(1e-6,dt)#this isnt so nice

	global tick0
	tick0=time()#GET LEFT OVER FRAME TIME OR SOMETHING (FOR EVENTS) INSTEAD OF DOING THIS TIME SHIT

	for bullet in bullets:
		bullet.step(GLOBAL_ACCELERATION,0.005,dt)

	for character in characters:
		character.step(dt)

	camp_spring.step(the_guy.p,12,0.7,dt)
	cama_spring.step(0,20,0.6,dt)
	global camp
	global camo
	camp=camp_spring.p
	camo=cang(cama_spring.p)

pyglet.clock.schedule(step)#this is bad but whatever















pyglet.app.run()