#import gc; gc.disable() # wut this?

print('Start Killem 2D Client')

from vec2 import Vec2
from vec3 import Vec3
#import netc
from math import cos, sin, atan2
import pyglet
from pyglet.gl import *
from glutil import *

window0 = pyglet.window.Window(222, 173, 'Killem 2D', 1) # easter egg much?



from caller import Caller

class State:
	def __init__(*_):
		pass

	def set(*_):
		pass

	def on(*_):
		return Caller()

	def call(*_):
		pass

	def depend(*_):
		pass



state0 = State()



glEnable(GL_BLEND);
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glClearColor(0, 0, 0.2, 0)



rect_program = Program(
	Shader('shaders/rectv.glsl', GL_VERTEX_SHADER),
	Shader('shaders/rectf.glsl', GL_FRAGMENT_SHADER)
)

rect_camd_uniform = glGetUniformLocation(rect_program.id, b'camd')
rect_camp_uniform = glGetUniformLocation(rect_program.id, b'camp')
rect_camo_uniform = glGetUniformLocation(rect_program.id, b'camo')
rect_wins_uniform = glGetUniformLocation(rect_program.id, b'wins')

rect_inde = -1
rect_poss = []
rect_cols = []

def add_rect():
	global rect_inde; rect_inde +=  1
	global rect_poss; rect_poss +=  8*(0, ) # this is probably slow
	global rect_cols; rect_cols += 12*(0, )

	return rect_inde

def edit_rect(i, p, s, c):
	px, py = p.x, p.y
	sx, sy = s.x, s.y
	cx, cy, cz = c.x, c.y, c.z

	rect_poss[8*i + 0] = px + 1*sx
	rect_poss[8*i + 1] = py + 1*sy
	rect_poss[8*i + 2] = px + 1*sx
	rect_poss[8*i + 3] = py + 0*sy
	rect_poss[8*i + 4] = px + 0*sx
	rect_poss[8*i + 5] = py + 0*sy
	rect_poss[8*i + 6] = px + 0*sx
	rect_poss[8*i + 7] = py + 1*sy

	rect_cols[12*i +  0] = cx
	rect_cols[12*i +  1] = cy
	rect_cols[12*i +  2] = cz
	rect_cols[12*i +  3] = cx
	rect_cols[12*i +  4] = cy
	rect_cols[12*i +  5] = cz
	rect_cols[12*i +  6] = cx
	rect_cols[12*i +  7] = cy
	rect_cols[12*i +  8] = cz
	rect_cols[12*i +  9] = cx
	rect_cols[12*i + 10] = cy
	rect_cols[12*i + 11] = cz

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

bullet_camd_uniform = glGetUniformLocation(bullet_program.id, b'camd')
bullet_camp_uniform = glGetUniformLocation(bullet_program.id, b'camp')
bullet_camo_uniform = glGetUniformLocation(bullet_program.id, b'camo')
bullet_wins_uniform = glGetUniformLocation(bullet_program.id, b'wins')

bullet_inde = -1
bullet_poss = []
bullet_tran = []

def add_bullet():
	global bullet_inde; bullet_inde += 1
	global bullet_poss; bullet_poss += 8*(0, )
	global bullet_tran; bullet_tran += 1*(0, )

	return bullet_inde

def edit_bullet(i, p, d):
	px, py = p.x, p.y

	t = atan2(d.y, d.x)
	c, s = cos(t), sin(t)

	h = d.norm()
	r = 0.2

	hc, hs = h*c, h*s
	rc, rs = r*c, r*s

	bullet_poss[8*i + 0] = px - rs + hc
	bullet_poss[8*i + 1] = py + rc + hs

	bullet_poss[8*i + 2] = px - rs
	bullet_poss[8*i + 3] = py + rc

	bullet_poss[8*i + 4] = px + rs
	bullet_poss[8*i + 5] = py - rc

	bullet_poss[8*i + 6] = px + rs + hc
	bullet_poss[8*i + 7] = py - rc + hs

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
			if char == 'P':
				global camd; camd = 20
				global camp; camp = Vec2(ix, -2*iy)
			elif char != ' ' and char != '\n':
				edit_rect(add_rect(), Vec2(ix, -2*iy), Vec2(1, 2), char_cols[char])
			ix += 1
		iy += 1



def cang(t):
	return Vec2(cos(t), sin(t))



from time import time
from random import random

build_map('maps/map0.bm')

bullets = []

accel = Vec2(0, -128)

tick0 = time()

from spring import Spring
camo_spring = Spring(0, 0)


m0x, m0y = 0, 0
m1x, m1y = 0, 0

def step(dt):
	global tick; tick = time() - tick0
	global camd; camd = 40 + 20*sin(tick)

	camo_spring.step(0, 12, 0.4, dt)
	global camo; camo = cang(camo_spring.p)

	global bullets; bullet = {}
	bullet['i'] = add_bullet()
	bullet['p'] = Vec2(m0x, m0y)
	bullet['v'] = Vec2(10, 10)*Vec2(m1x - m0x, m1y - m0y)
	bullets += (bullet, )

	for bullet in bullets:
		bullet['p'] += Vec2(dt, dt)*bullet['v'] + Vec2(0.5*dt*dt, 0.5*dt*dt)*accel
		bullet['v'] += Vec2(dt, dt)*accel
		edit_bullet(bullet['i'], bullet['p'], Vec2(dt, dt)*bullet['v'])

pyglet.clock.schedule_interval(step, 1/60) # this is bad but whatever



def update_wins_uniforms(wins):
	glUseProgram(rect_program.id)
	glUniform2f(rect_wins_uniform, wins.x, wins.y)

	glUseProgram(bullet_program.id)
	glUniform2f(bullet_wins_uniform, wins.x, wins.y)

#state0.on('draw', 'wins').connect(update_wins_uniforms) # on draw (if wins is different since last draw)



#def use_rect_program():
#	glUseProgram(rect_program.id)

#rect_uniform_change = state0.depend('rect_camp_uniform', 'rect_camo_uniform')
#rect_uniform_change.before.connect(use_rect_program)



def draw_scene():
	glClear(GL_COLOR_BUFFER_BIT) # can't make this assumption (i want better state management)

	# render rects
	glUseProgram(rect_program.id)
	glUniform1f(rect_camd_uniform, camd)
	glUniform2f(rect_camp_uniform, camp.x, camp.y)
	glUniform2f(rect_camo_uniform, camo.x, camo.y)
	draw_rects()

	# render bullets
	glUseProgram(bullet_program.id)
	glUniform1f(bullet_camd_uniform, camd)
	glUniform2f(bullet_camp_uniform, camp.x, camp.y)
	glUniform2f(bullet_camo_uniform, camo.x, camo.y)
	draw_bullets()

#state0.on('draw').connect(draw_scene)



@window0.event
def on_resize(sx, sy):
	#state0.set('wins', Vec2(sx, sy))
	update_wins_uniforms(Vec2(sx, sy))

@window0.event
def on_key_press(code, mod):
	pass

@window0.event
def on_key_release(code, mod):
	pass

@window0.event
def on_mouse_press(px, py, code, mod):
	cx, cy, cz = camp.x, camp.y, camd
	wx, wy = window0.width, window0.height

	global m0x, m0y; m0x, m0y = cx + cz*(2*px - wx)/wy, cy + cz*(2*py - wy)/wy

@window0.event
def on_mouse_release(px, py, code, mod):
	cx, cy, cz = camp.x, camp.y, camd
	wx, wy = window0.width, window0.height

	global m1x, m1y; m1x, m1y = cx + cz*(2*px - wx)/wy, cy + cz*(2*py - wy)/wy

	global bullets; bullet = {}
	bullet['i'] = add_bullet()
	bullet['p'] = Vec2(m0x, m0y)
	bullet['v'] = Vec2(10, 10)*Vec2(m1x - m0x, m1y - m0y)
	bullets += (bullet, )

	camo_spring.v += 40

@window0.event
def on_mouse_motion(px, py, dx, dy):
	#state0.set('mouse_position', Vec2(px, py))
	pass

@window0.event
def on_draw():
	#state0.call('draw')
	draw_scene()

pyglet.app.run()