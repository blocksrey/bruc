import pyglet
from pyglet.gl import *
from glutil import *
from events import *











RELEASE=0
if RELEASE:
	import gc
	gc.disable()#no garbage collection
	pyglet.options['debug_gl']=False#optimizations (unstable)






















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
	#import menu
	from v2 import V2,null2,cang
	from v3 import V3
	from math import atan2,tan,pi
	from random import random
	import character
	from geometry import draw_scene
	import bullet
	import bomb
	import camera
	from map import Map,spawns



	import signal,os

	def handler(signum,frame):
		#print('Signal handler called with signal',signum)
		exit(1)

	# Set the signal handler
	signal.signal(signal.SIGINT,handler)

	import network
	network.client()





	Map('maps/map0.bm')
	camera.Camera(null2,null2).use()
	char=character.Character(spawns[int(len(spawns)*random())],null2,V3(*calc_skin_color(random())))
	char.use()
	#network.send('newcharacter',char)

	ISA,ISD=0,0
	#the guy & bullets & camera
	def _(code,mod):
		key=chr(code)
		if key==' ':
			character.the_character.jump()
		if key=='d' or key=='a':
			character.the_character.fat(key=='d' and 1 or key=='a' and -1)
	on_key_press_caller.connect(_)

	def _(code,mod):
		key=chr(code)
		if character.the_character.t.x==1 and key=='d':
			character.the_character.fat(0)
		if character.the_character.t.x==-1 and key=='a':
			character.the_character.fat(0)
	on_key_release_caller.connect(_)

	def _(mp,code,mod):
		w=V2(the_window.width,the_window.height)
		s=camera.the_camera.p+camera.the_camera.d/w.y*(2*mp-w)
		frm=character.the_character.p+V2(0,2)
		v=100*(s-frm).unit()
		pyglet.media.load('sounds/shoot.mp3').play().pitch=0.95+0.1*random()
		#character.the_character.impulse(V3(0,50,0))
		character.the_character.v-=0.05*v
		camera.impulse(frm,v)

		if code==1:
			bullet.Bullet(frm,v)
			network.send('newbullet',frm,v)
		elif code==4:
			bomb.Bomb(frm,0.5*v)

	on_mouse_press_caller.connect(_)

	def _(mp,d):
		camera.the_camera.d+=2*d.y
	on_mouse_scroll_caller.connect(_)

	def _():
		draw_scene()

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(0,the_window.width,0,the_window.height,-1,1)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
	on_draw_caller.connect(_)

	def _(ws):
		glViewport(0,0,ws.x,ws.y)
	on_resize_caller.connect(_)

	steppers=[
		character.step,
		bullet.step,
		bomb.step,
		camera.step
	]

	import threading

	def step(dt):
		#print(threading.active_count())

		for stepper in steppers:
			stepper(dt)

	pyglet.clock.schedule(step)
on_game_start_caller.connect(_)

on_game_start_caller.fire()

pyglet.app.run()