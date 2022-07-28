print("Start Killem 2D Client")

import pyglet
from vec2 import Vec2
from vec3 import Vec3
import netc
from math import cos, sin

window0 = pyglet.window.Window(888, 692, "Killem 2D", 1) # easter egg much?

from gl import *







rect_prog = Program(
	Shader("rectv.glsl", GL_VERTEX_SHADER),
	Shader("rectf.glsl", GL_FRAGMENT_SHADER)
)

time_u = Uniform(rect_prog, "time")
camp_u = Uniform(rect_prog, "camp")
camo_u = Uniform(rect_prog, "camo")
wins_u = Uniform(rect_prog, "wins")

rect_prog.enable()


#from mesh2 import Mesh2

#the_mesh2 = Mesh2(
#	Vec2(+1, +1),
#	Vec2(+1, -1),
#	Vec2(-1, +1),
#	Vec2(-1, -1)
#)

#print(the_mesh2.get_aabb())
#print(the_mesh2.build_rays())



@window0.event
def on_resize(sx, sy):
	wins_u.set(sx, sy)

@window0.event
def on_key_press(code, _):
	pass

@window0.event
def on_key_release(code, _):
	pass


@window0.event
def on_mouse_press(px, py, code, _):
	pass

@window0.event
def on_mouse_release(px, py, code, _):
	pass

import random

def build_map(path):
	IY = 0
	for row in open(path).readlines():
		IX = 0
		for bar in row:
			if bar != ' ':
				append_rect(Vec2(IX, IY), Vec2(1, 1), Vec3(255, 180, 240))
			IX += 1
		IY += 1

build_map("map0.bm")

time = 0
camp = Vec3(0, 0, 0)
camo = 0

def step(dt):
	global time; time += dt
	global camp; camp = Vec3(0, 0, 0.05)
	global camo; camo = 0

@window0.event
def on_draw():
	time_u.set(time)
	camp_u.set(camp.x, camp.y, camp.z)
	camo_u.set(camo)

	glClear(GL_COLOR_BUFFER_BIT)

	draw_arrays()

pyglet.clock.schedule_interval(step, 1/60) # this is bad but whatever
pyglet.app.run()