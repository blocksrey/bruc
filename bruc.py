import pyglet
from pyglet.gl import *
from glutil import *
from events import *











RELEASE=0
if RELEASE:
	import gc
	gc.disable()#no garbage collection
	pyglet.options['debug_gl']=False#no debug
























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














glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
glClearColor(1,1,1,1)

from caller import Caller

on_game_start_caller=Caller()

def _():
	import menu
	from v2 import v2,null2,cang
	from v3 import v3
	from math import atan2,tan,pi
	from random import random
	import character
	from geometry import draw_scene
	import bullet
	import camera
	from map import Map,spawns

	GLOBAL_ACCELERATION=v2(0,-128)

	the_map=Map('maps/map0.bm')
	character.Character(spawns[int(len(spawns)*random())],null2,v3(*calc_skin_color(random()))).use()

	print(character.active_character.p)

	#the guy & bullets & camera
	def _(code,mod):
		key=chr(code)
		if key==' ':
			character.active_character.jump()
		else:
			character.active_character.fat(key=='d' and 1 or key=='a' and -1 or 0)
	on_key_press_caller.connect(_)

	def _(code,mod):
		key=chr(code)
		if key!=' ':
			character.active_character.fat(key=='d' and 0 or key=='a' and 0 or 0)#this is wrong but whatever lol
	on_key_release_caller.connect(_)

	def _(mp,code,mod):
		w=v2(the_window.width,the_window.height)
		s=camera.active_camera.p+camera.active_camera.d/w.y*(2*mp-w)
		print(character.active_character.p)
		v=200*(s-character.active_character.p).unit()
		bullet.Bullet(character.active_character.p,v)
		camera.impulse(character.active_character.p,0.1*v)
		character.active_character.v-=0.05*v
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