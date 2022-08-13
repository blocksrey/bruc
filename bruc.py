import pyglet
from pyglet.gl import *
from v2 import v2,null2,cang
from v3 import v3,null3
from math import atan2,tan,pi
from glutil import *
from caller import Caller
from random import random
import character

the_window=pyglet.window.Window(4*222,4*173,'bruc')#easter egg much?

on_key_press_caller=Caller()
@the_window.event
def on_key_press(code,mod):
	on_key_press_caller.fire(code,mod)

on_key_release_caller=Caller()
@the_window.event
def on_key_release(code,mod):
	on_key_release_caller.fire(code,mod)

on_mouse_scroll_caller=Caller()
@the_window.event
def on_mouse_scroll(px,py,dx,dy):
	on_mouse_scroll_caller.fire(v2(px,py),v2(dx,dy))

on_mouse_press_caller=Caller()
@the_window.event
def on_mouse_press(px,py,code,mod):
	on_mouse_press_caller.fire(v2(px,py),code,mod)

on_mouse_motion_caller=Caller()
@the_window.event
def on_mouse_release(px,py,code,mod):
	on_mouse_motion_caller.fire(v2(px,py),code,mod)

on_draw_caller=Caller()
@the_window.event
def on_mouse_motion(px,py,dx,dy):
	on_mouse_motion_caller.fire(v2(px,py),v2(dx,dy))

on_draw_caller=Caller()
@the_window.event
def on_draw():
	on_draw_caller.fire()

on_resize_caller=Caller()
@the_window.event
def on_resize(sx,sy):
	on_resize_caller.fire(v2(sx,sy))













GLOBAL_ACCELERATION=v2(0,-128)

RELEASE=0
if RELEASE:
	import gc
	gc.disable()#no garbage collection
	pyglet.options['debug_gl']=False#no debug

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
glClearColor(1,1,1,1)
























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

#projectile with drag (only accurate for small t)
def aero_projectile(p,v,g,k,t):
	a=g-k*v.norm()*v#global acceleration+drag
	return p+t*v+0.5*t*t*a,v+t*a#p(t),p'(t)












































import block

VAO_MODE=gl_info.have_version(2)

if VAO_MODE:
	block.block_program=Program(
		Shader('shaders/blockv.glsl',GL_VERTEX_SHADER),
		Shader('shaders/blockf.glsl',GL_FRAGMENT_SHADER)
	)

	block_camd_uniform=glGetUniformLocation(block.block_program.id,b'camd')
	block_camp_uniform=glGetUniformLocation(block.block_program.id,b'camp')
	block_camo_uniform=glGetUniformLocation(block.block_program.id,b'camo')
	block_wins_uniform=glGetUniformLocation(block.block_program.id,b'wins')

	def draw_block():
		pyglet.graphics.draw(
			4*block.block_l,
			GL_QUADS,
			('v2f',block.block_p),
			('c4f',block.block_c)
		)

	def _(wins):
		glUseProgram(block.block_program.id)
		glUniform2f(block_wins_uniform,wins.x,wins.y)
	on_resize_caller.connect(_)

	def draw_scene():
		glClear(GL_COLOR_BUFFER_BIT)#can't make this assumption (i want better state management)

		#render block
		glUseProgram(block.block_program.id)
		glUniform1f(block_camd_uniform,camera.active_camera.d)
		glUniform2f(block_camp_uniform,camera.active_camera.p.x,camera.active_camera.p.y)
		glUniform2f(block_camo_uniform,camera.active_camera.o.x,camera.active_camera.o.y)
		draw_block()
else:
	def draw_block():
		for i in range(block.block_l):
			i16=16*i
			glColor4f(block.block_c[i16+0],block.block_c[i16+1],block.block_c[i16+2],block.block_c[i16+3])

			i8=8*i
			glVertex2f(block.block_p[i8+0],block.block_p[i8+1])
			glVertex2f(block.block_p[i8+2],block.block_p[i8+3])
			glVertex2f(block.block_p[i8+4],block.block_p[i8+5])
			glVertex2f(block.block_p[i8+6],block.block_p[i8+7])

	def draw_scene():
		glClear(GL_COLOR_BUFFER_BIT)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glPerspective(45,the_window.width/the_window.height,0.1,1000)

		glRotatef(180/pi*atan2(-camera.active_camera.o.y,camera.active_camera.o.x),0,0,1)
		glTranslatef(-camera.active_camera.p.x,-camera.active_camera.p.y,-camera.active_camera.d)

		glBegin(GL_QUADS)
		draw_block()
		glEnd()



















the_guy=character.Character(v2(50,100),null2,v3(1,0,0))



from map import Map,spawns
import bullet
import camera

on_game_start_caller=Caller()

def _():
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
		s=camera.active_camera.p+camera.active_camera.d/w.y*(2*mp-w)
		v=200*(s-the_guy.p).unit()
		bullet.Bullet(the_guy.p,v)
		camera.impulse(the_guy.p,0.1*v)
		the_guy.v-=0.02*v
	on_mouse_press_caller.connect(_)

	def _(mp,d):
		camera.active_camera.d+=2*d.y
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


	the_map=Map('maps/map0.bm')
	character.Character(spawns[int(len(spawns)*random())],null2,v3(*calc_skin_color(random()))).use()

	steppers=[
		character.step,
		bullet.step,
		camera.step
	]

	def step(dt):
		dt=max(1e-6,dt)#this isnt so nice

		for stepper in steppers:
			stepper(dt)

	pyglet.clock.schedule(step)
on_game_start_caller.connect(_)

on_game_start_caller.fire()

pyglet.app.run()