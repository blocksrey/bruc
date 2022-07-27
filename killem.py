print("Start Killem 2D Client")

import pyglet
from pyglet.gl import *

the_win = pyglet.window.Window(800, 600, "Killem 2D")

from vec2 import Vec2
from vec3 import Vec3
from gl import draw_rect


import netc


from math import cos, sin

#def shaderErrorLog(shader):
#	length
#	glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &length)
#
#	char *log = (char *)malloc((usize)length)
#	glGetShaderInfoLog(shader, length, &length, log)
#
#	return log
#
#def programErrorLog(program):
#
#	length
#	glGetProgramiv(program, GL_INFO_LOG_LENGTH, &length)
#
#	char *log = (char *)malloc((usize)length)
#	glGetProgramInfoLog(program, length, &length, log)
#	return log
#
#def createShader(prog, type, const char *src):
#
#	error = 0
#	r = glCreateShader(type)
#
#	glShaderSource(r, 1, &src, 0)
#	glCompileShader(r)
#
#	glGetShaderiv(r, GL_COMPILE_STATUS, &error)
#	print("Compiler error in shader\n", shaderErrorLog(r))
#
#	glAttachShader(prog, r)
#	return r
#
#def createProgram(char *vertSrc, char *fragSrc):
#
#	error = 0
#	prog = glCreateProgram()
#	vert = createShader(prog, GL_VERTEX_SHADER, vertSrc)
#	frag = createShader(prog, GL_FRAGMENT_SHADER, fragSrc)
#
#	glLinkProgram(prog)
#	glGetProgramiv(prog, GL_LINK_STATUS, &error)
#	print("Linker error in program\n", programErrorLog(prog))
#
#	glDetachShader(prog, vert)
#	glDetachShader(prog, frag)
#	glDeleteShader(vert)
#	glDeleteShader(frag)
#
#	glValidateProgram(prog)
#	glGetProgramiv(prog, GL_VALIDATE_STATUS, &error)
#	print("Linker error in program\n", programErrorLog(prog))
#
#	return prog

from gl import *

rect_prog = Program(
	Shader("rectv.glsl", GL_VERTEX_SHADER),
	Shader("rectf.glsl", GL_FRAGMENT_SHADER)
)

viewsize_u = Uniform(rect_prog, "viewsize_u")

rect_prog.enable()


viewsize_u.set(800, 600)


#from mesh2 import Mesh2

#the_mesh2 = Mesh2(
#	Vec2(+1, +1),
#	Vec2(+1, -1),
#	Vec2(-1, +1),
#	Vec2(-1, -1)
#)

#print(the_mesh2.get_aabb())
#print(the_mesh2.build_rays())



time = 0
while 1:
	dt = pyglet.clock.tick()

	time -= dt
	while time <= 0:
		time += 10

	glClear(GL_COLOR_BUFFER_BIT)

	draw_rect(Vec2(0, 0), Vec2(cos(time), sin(time)), Vec3(0.5, 0, 0))

	the_win.flip()