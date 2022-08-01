print('Start Killem 2D Client')

from vec2 import Vec2
from vec3 import Vec3
#import netc
from math import cos, sin, atan2
import pyglet
from pyglet.gl import *
from ctypes import *
from gl import *

window0 = pyglet.window.Window(222, 173, 'Killem 2D', 1) # easter egg much?







rect_program = Program(
	Shader('shaders/rectv.glsl', GL_VERTEX_SHADER),
	Shader('shaders/rectf.glsl', GL_FRAGMENT_SHADER)
)

rect_tick_uniform = Uniform('tick')
rect_camp_uniform = Uniform('camp')
rect_camo_uniform = Uniform('camo')
rect_wins_uniform = Uniform('wins')

rect_tick_uniform.attach(rect_program)
rect_camp_uniform.attach(rect_program)
rect_camo_uniform.attach(rect_program)
rect_wins_uniform.attach(rect_program)

rect_inde = 0
rect_poss = []
rect_cols = []

def add_rect(p, s, c):
	global rect_inde
	of = rect_inde
	rect_inde += 1

	global rect_poss; rect_poss +=  8*(0, ) # this is probably slow
	global rect_cols; rect_cols += 12*(0, )

	def edit_rect(p, s, c):
		px, py = p.x, p.y
		sx, sy = s.x, s.y
		cx, cy, cz = c.x, c.y, c.z

		rect_poss[8*of + 0] = px + 1*sx
		rect_poss[8*of + 1] = py + 1*sy
		rect_poss[8*of + 2] = px + 1*sx
		rect_poss[8*of + 3] = py + 0*sy
		rect_poss[8*of + 4] = px + 0*sx
		rect_poss[8*of + 5] = py + 0*sy
		rect_poss[8*of + 6] = px + 0*sx
		rect_poss[8*of + 7] = py + 1*sy

		rect_cols[12*of +  0] = cx
		rect_cols[12*of +  1] = cy
		rect_cols[12*of +  2] = cz
		rect_cols[12*of +  3] = cx
		rect_cols[12*of +  4] = cy
		rect_cols[12*of +  5] = cz
		rect_cols[12*of +  6] = cx
		rect_cols[12*of +  7] = cy
		rect_cols[12*of +  8] = cz
		rect_cols[12*of +  9] = cx
		rect_cols[12*of + 10] = cy
		rect_cols[12*of + 11] = cz

	edit_rect(p, s, c)

	return edit_rect

def draw_rects():
	pyglet.graphics.draw(
		int(0.5*len(rect_poss)),
		GL_QUADS,
		('v2f', rect_poss),
		('c3B', rect_cols)
	)












bullet_program = Program(
	Shader('shaders/bulletv.glsl', GL_VERTEX_SHADER),
	Shader('shaders/bulletf.glsl', GL_FRAGMENT_SHADER)
)

bullet_tick_uniform = Uniform('tick')
bullet_camp_uniform = Uniform('camp')
bullet_camo_uniform = Uniform('camo')
bullet_wins_uniform = Uniform('wins')

bullet_tick_uniform.attach(bullet_program)
bullet_camp_uniform.attach(bullet_program)
bullet_camo_uniform.attach(bullet_program)
bullet_wins_uniform.attach(bullet_program)

bullet_inde = 0
bullet_poss = []

def add_bullet(p, d):
	global bullet_inde
	of = bullet_inde
	bullet_inde += 1

	global bullet_poss; bullet_poss +=  8*(0, )

	def edit_bullet(p, d):
		px, py = p.x, p.y

		t = atan2(d.y, d.x)
		c, s = cos(t), sin(t)

		h = d.norm()
		r = 0.05

		hc, hs = h*c, h*s
		rc, rs = r*c, r*s

		bullet_poss[8*of + 0] = px - rs + hc
		bullet_poss[8*of + 1] = py + rc + hs

		bullet_poss[8*of + 2] = px - rs
		bullet_poss[8*of + 3] = py + rc

		bullet_poss[8*of + 4] = px + rs
		bullet_poss[8*of + 5] = py - rc

		bullet_poss[8*of + 6] = px + rs + hc
		bullet_poss[8*of + 7] = py - rc + hs

	edit_bullet(p, d)

	return edit_bullet

def draw_bullets():
	pyglet.graphics.draw(
		int(0.5*len(bullet_poss)),
		GL_QUADS,
		('v2f', bullet_poss)
	)












char_cols = {}
char_cols['G'] = Vec3(0, 192, 0)
char_cols['C'] = Vec3(128, 128, 128)
char_cols['_'] = Vec3(200, 200, 200)
char_cols['P'] = Vec3(0, 0, 255)

char_cols['^'] = Vec3(255, 0, 0)
char_cols['>'] = Vec3(255, 0, 0)
char_cols['<'] = Vec3(255, 0, 0)

char_cols['J'] = Vec3(255, 0, 255)

char_cols['|'] = Vec3(128, 192, 255)

def build_map(path):
	iy = 0
	for row in open(path).readlines():
		ix = 0
		for char in row:
			if char != ' ' and char != '\n':
				add_rect(Vec2(ix, 2*iy), Vec2(1, 2), char_cols[char])
			ix += 1
		iy += 1















from time import time
from random import random

build_map('maps/map0.bm')

bullets = ()

for i in range(32):
	bullets += (add_bullet(Vec2(8*random(), 8*random()), Vec2(4*random(), 4*random())), )

tick = 0
camp = Vec3(0, 0, 30)
camo = 0

def step(_):
	#global tick; tick = time()
	global camp; camp = Vec3(0, 0, 30)
	global camo; camo = 0

	#for edit_bullet in bullets:
	#	edit_bullet(Vec2(0, 0), Vec2(4*cos(tick), 4*sin(tick)))

pyglet.clock.schedule_interval(step, 1/2) # this is bad but whatever




@window0.event
def on_resize(sx, sy):
	pass

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

@window0.event
def on_mouse_motion(px, py, dx, dy):
	pass

@window0.event
def on_draw():
	glClearColor(random(), random(), random(), random())
	glClear(GL_COLOR_BUFFER_BIT)

	rect_program.use()
	glUniform1f(rect_tick_uniform.id, tick)
	glUniform3f(rect_camp_uniform.id, camp.x, camp.y, camp.z)
	glUniform1f(rect_camo_uniform.id, camo)
	glUniform2f(rect_wins_uniform.id, window0.width, window0.height)
	draw_rects()

	bullet_program.use()
	glUniform1f(bullet_tick_uniform.id, tick)
	glUniform3f(bullet_camp_uniform.id, camp.x, camp.y, camp.z)
	glUniform1f(bullet_camo_uniform.id, camo)
	glUniform2f(bullet_wins_uniform.id, window0.width, window0.height)
	draw_bullets()

pyglet.app.run()