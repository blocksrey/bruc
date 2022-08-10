print('Start Killem 2D Client')

from vec2 import Vec2
from vec3 import Vec3
from math import cos, sin, atan2, sqrt
import pyglet
from pyglet.gl import *
from glutil import *
from camera import *

window0 = pyglet.window.Window(222, 173, 'Killem 2D', 1) # easter egg much?

VAO_MODE = gl_info.have_version(2) and 0

RELEASE = 0
if RELEASE:
	import gc; gc.disable() # no garbage collection
	pyglet.options['debug_gl'] = 0 # no debug

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)











from ray2 import Ray2
from mesh2 import Mesh2

the_mesh = Mesh2((Vec2(-4, -3), Vec2(4, -4), Vec2(-4, 3), Vec2(4, 3)))

print(the_mesh.project_ray(Ray2(Vec2(3.9, -14), Vec2(0, 20))))










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







class Sequencer:
	def __init__(sequencer):
		sequencer.queue = []

	def call(sequencer, time):
		sequencer.queue.append(time)

	def dump(sequencer, time):
		#print(sequencer.queue)
		pass



ammo = 3

lastshot = 0
def get_cooldown(et):
	lastshot = et
	print("shoot @", t)
	return 0.1

sequencer0 = Sequencer()

sequencer0.dump(3)
sequencer0.call(get_cooldown)
sequencer0.dump(3.1)



























# this needs to not be here (opengl < 2.x)
#rect_program = Program(
#	Shader('shaders/rectv.glsl', GL_VERTEX_SHADER),
#	Shader('shaders/rectf.glsl', GL_FRAGMENT_SHADER)
#)
#
#rect_camd_uniform = glGetUniformLocation(rect_program.id, b'camd')
#rect_camp_uniform = glGetUniformLocation(rect_program.id, b'camp')
#rect_camo_uniform = glGetUniformLocation(rect_program.id, b'camo')
#rect_wins_uniform = glGetUniformLocation(rect_program.id, b'wins')

rect_inde = -1
rect_poss = []
rect_cols = []

def add_rect():
	global rect_inde; rect_inde += 1
	global rect_poss; rect_poss += (0, )*8 # this is probably slow
	global rect_cols; rect_cols += (0, )*12

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


from math import tan, pi

def glPerspective(vt, ar, z0, z1):
		hh = tan(pi/180*vt)*z0
		hw = ar*hh
		glFrustum(-hw, hw, -hh, hh, z0, z1)

if VAO_MODE:
	def draw_rects():
		pyglet.graphics.draw(
			4*(rect_inde + 1),
			GL_QUADS,
			('v2f', rect_poss),
			('c3f', rect_cols)
		)
else:
	def draw_rects():
		for i in range(rect_inde + 1):
			glColor3f(rect_cols[12*i + 0], rect_cols[12*i + 1], rect_cols[12*i + 2])

			glVertex2f(rect_poss[8*i + 0], rect_poss[8*i + 1])
			glVertex2f(rect_poss[8*i + 2], rect_poss[8*i + 3])
			glVertex2f(rect_poss[8*i + 4], rect_poss[8*i + 5])
			glVertex2f(rect_poss[8*i + 6], rect_poss[8*i + 7])







#bullet_program = Program(
#	Shader('shaders/bulletv.glsl', GL_VERTEX_SHADER),
#	Shader('shaders/bulletf.glsl', GL_FRAGMENT_SHADER)
#)
#
#bullet_camd_uniform = glGetUniformLocation(bullet_program.id, b'camd')
#bullet_camp_uniform = glGetUniformLocation(bullet_program.id, b'camp')
#bullet_camo_uniform = glGetUniformLocation(bullet_program.id, b'camo')
#bullet_wins_uniform = glGetUniformLocation(bullet_program.id, b'wins')

bullet_inde = -1
bullet_poss = []
bullet_opac = []

def add_bullet():
	global bullet_inde; bullet_inde += 1
	global bullet_poss; bullet_poss += (0, )*8
	global bullet_opac; bullet_opac += (0, )*1

	return bullet_inde

def edit_bullet(i, p, d):
	px, py = p.x, p.y
	dx, dy = d.x, d.y

	h = sqrt(dx*dx + dy*dy)
	r = 0.2

	c, s = dx/h, dy/h # cos, sin

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

	bullet_opac[i] = (6)*pi*r/(pi*r + 2*h) # whatever*(circular_area ./ h->0)/circular_area

if VAO_MODE:
	def draw_bullets():
		pyglet.graphics.draw(
			4*(bullet_inde + 1),
			GL_QUADS,
			('v2f', bullet_poss)
		)
else:
	def draw_bullets():
		for i in range(bullet_inde + 1):
			glColor4f(1, 0.9, 0, bullet_opac[i])

			glVertex2f(bullet_poss[8*i + 0], bullet_poss[8*i + 1])
			glVertex2f(bullet_poss[8*i + 2], bullet_poss[8*i + 3])
			glVertex2f(bullet_poss[8*i + 4], bullet_poss[8*i + 5])
			glVertex2f(bullet_poss[8*i + 6], bullet_poss[8*i + 7])
























character_inde = -1
character_poss = []

def add_character():
	global character_inde; character_inde += 1
	global character_poss; character_poss += (0, )*8

	return character_inde

def edit_character(i, p, o):
	px, py = p.x, p.y

	h = 2
	r = 0.5

	c, s = -o.y, o.x

	hc, hs = h*c, h*s
	rc, rs = r*c, r*s

	character_poss[8*i + 0] = px - rs + hc
	character_poss[8*i + 1] = py + rc + hs

	character_poss[8*i + 2] = px - rs
	character_poss[8*i + 3] = py + rc

	character_poss[8*i + 4] = px + rs
	character_poss[8*i + 5] = py - rc

	character_poss[8*i + 6] = px + rs + hc
	character_poss[8*i + 7] = py - rc + hs

if VAO_MODE:
	def draw_characters():
		pyglet.graphics.draw(
			4*(bullet_inde + 1),
			GL_QUADS,
			('v2f', bullet_poss)
		)
else:
	def draw_characters():
		glColor4f(0, 1, 1, 1)

		for i in range(character_inde + 1):
			glVertex2f(character_poss[8*i + 0], character_poss[8*i + 1])
			glVertex2f(character_poss[8*i + 2], character_poss[8*i + 3])
			glVertex2f(character_poss[8*i + 4], character_poss[8*i + 5])
			glVertex2f(character_poss[8*i + 6], character_poss[8*i + 7])































char_cols = {}
char_cols['w'] = Vec3(0, 0.75, 0)
char_cols['C'] = Vec3(0.5, 0.5, 0.5)
char_cols['-'] = Vec3(0.8, 0.8, 0.8)

char_cols['^'] = Vec3(1, 0, 0)
char_cols['>'] = Vec3(1, 0, 0)
char_cols['<'] = Vec3(1, 0, 0)

char_cols['J'] = Vec3(1, 0, 1)

char_cols['|'] = Vec3(0.5, 0.75, 1)

char_cols['W'] = Vec3(0.2, 0.4, 1)

char_cols['P'] = Vec3(1, 1, 0)

def build_map(path):
	iy = 0
	for row in open(path).readlines():
		ix1 = 0

		ix = 0
		ch = row[0]

		for ch1 in row:
			if ch != ch1:
				sx = ix1 - ix

				px, py = 2*ix, -4*iy
				sx, sy = 2*sx, 4

				if ch == '-':
					edit_rect(add_rect(), Vec2(px, py + 0.9*sy), Vec2(sx, 0.1*sy), char_cols[ch])
				elif ch != ' ': # newline case is handled naturally :P:P
					edit_rect(add_rect(), Vec2(px, py), Vec2(sx, sy), char_cols[ch])

				ix = ix1
				ch = ch1

			ix1 += 1
		iy += 1






from time import time
from random import random

build_map('maps/map0.bm')

bullets = []
characters = []

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
	global camo; camo = Vec2.cang(camo_spring.p)

	global camp; camp = Vec2(80 + 20*sin(0.5*tick), -20 + 10*cos(0.4*tick))

	for bullet in bullets:
		#vm = bullet['v'].norm()
		#ac = -p
		bullet['p'] += bullet['v']*dt + accel*0.5*dt*dt
		bullet['v'] += accel*dt
		edit_bullet(bullet['i'], bullet['p'], bullet['v']*dt)

	for character_index in characters:
		this_tick = tick*14

		s = sin(this_tick)

		ox = 0
		oy = s*s

		ori = 0.2*sin(this_tick)

		edit_character(character_index, Vec2(60 + 20*cos(tick + character_index) + ox, -10*sin(tick*0.9 + character_index) + oy), Vec2(cos(ori), sin(ori)))

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




label = pyglet.text.Label('hello', x = 10, y = 10)








if VAO_MODE:
	@window0.event
	def on_resize(sx, sy):
		#state0.set('wins', Vec2(sx, sy))
		update_wins_uniforms(Vec2(sx, sy))
		pass

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
else:
	@window0.event
	def on_resize(sx, sy):
		glViewport(0, 0, sx, sy)

	def draw_scene():
		glClearColor(0.2*(1 + sin(tick)), 0.2*(1 + cos(tick)), 0, 0)

		glClear(GL_COLOR_BUFFER_BIT)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glPerspective(45, window0.width/window0.height, 0.1, 1000)

		glRotatef(180/pi*atan2(-camo.y, camo.x), 0, 0, 1)
		glTranslatef(-camp.x, -camp.y, -camd)

		glBegin(GL_QUADS)

		draw_rects()
		draw_bullets()
		draw_characters()

		glEnd()

#state0.on('draw').connect(draw_scene)





























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
	bullet['v'] = Vec2(m1x - m0x, m1y - m0y)*10
	bullets += (bullet, )

	global characters; characters += (add_character(), )

	camo_spring.v += 5

@window0.event
def on_mouse_motion(px, py, dx, dy):
	#state0.set('mouse_position', Vec2(px, py))
	pass

@window0.event
def on_draw():
	#state0.call('draw')
	draw_scene()

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0, window0.width, 0, window0.height, -1, 1)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	#label.draw()

pyglet.app.run()