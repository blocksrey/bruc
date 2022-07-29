print("Start Killem 2D Client")

import pyglet
from vec2 import Vec2
from vec3 import Vec3
import netc
from math import cos, sin

window0 = pyglet.window.Window(222, 173, "Killem 2D", 1) # easter egg much?

from gl import *



rect_program = Program(
	Shader("shaders/rectv.glsl", GL_VERTEX_SHADER),
	Shader("shaders/rectf.glsl", GL_FRAGMENT_SHADER)
)

time_uniform = Uniform(rect_program, "time")
camp_uniform = Uniform(rect_program, "camp")
camo_uniform = Uniform(rect_program, "camo")
wins_uniform = Uniform(rect_program, "wins")

rect_program.enable()



#from mesh2 import Mesh2

#the_mesh2 = Mesh2(
#	Vec2(+1, +1),
#	Vec2(+1, -1),
#	Vec2(-1, +1),
#	Vec2(-1, -1)
#)

#print(the_mesh2.get_aabb())
#print(the_mesh2.build_rays())



#print(asd)
#asd[0] = 3
#print(asd)

@window0.event
def on_resize(sx, sy):
	wins_uniform.set(sx, sy)

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


cols = {}
cols["G"] = Vec3(0, 192, 0)
cols["C"] = Vec3(128, 128, 128)
cols["_"] = Vec3(200, 200, 200)
cols["P"] = Vec3(0, 0, 255)

cols["^"] = Vec3(255, 0, 0)
cols[">"] = Vec3(255, 0, 0)
cols["<"] = Vec3(255, 0, 0)

cols["J"] = Vec3(255, 0, 255)

cols["|"] = Vec3(128, 192, 255)

def build_map(path):
	iy = 0
	for row in open(path).readlines():
		ix = 0
		for char in row:
			if char != " " and char != "\n":
				append_rect(Vec2(ix, 2*iy), Vec2(1, 2), cols[char])
			ix += 1
		iy += 1

build_map("maps/map0.bm")



class ArrayHandler:
	def __init__(arrayhandler):
		pass



time = 0
camp = Vec3(0, 0, 0)
camo = 0

def step(dt):
	global time; time += dt
	global camp; camp = Vec3(8*cos(time*0.19), 8*sin(time*0.21), 20)
	global camo; camo = 0.1*sin(1.31*time)

pyglet.clock.schedule_interval(step, 1/60) # this is bad but whatever



@window0.event
def on_draw():
	time_uniform.set(time)
	camp_uniform.set(camp.x, camp.y, camp.z)
	camo_uniform.set(camo)

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	draw_arrays()

pyglet.app.run()