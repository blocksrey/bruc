from vec3 import Vec3
from pyglet.graphics import draw
from pyglet.gl import *

inde = 0
poss = []
cols = []

def append_rect(p, s, c):
	global inde;
	of = inde
	inde += 1

	global poss; poss += (
		0, 0,
		0, 0,
		0, 0,
		0, 0
	)

	global cols; cols += (
		0, 0, 0,
		0, 0, 0,
		0, 0, 0,
		0, 0, 0
	)

	def transform(p, s, c):
		px, py = p.x, p.y
		sx, sy = s.x, s.y
		cx, cy, cz = c.x, c.y, c.z

		poss[8*of + 0] = px + 1*sx
		poss[8*of + 1] = py + 1*sy
		poss[8*of + 2] = px + 1*sx
		poss[8*of + 3] = py + 0*sy
		poss[8*of + 4] = px + 0*sx
		poss[8*of + 5] = py + 0*sy
		poss[8*of + 6] = px + 0*sx
		poss[8*of + 7] = py + 1*sy

		cols[12*of +  0] = cx
		cols[12*of +  1] = cy
		cols[12*of +  2] = cz
		cols[12*of +  3] = cx
		cols[12*of +  4] = cy
		cols[12*of +  5] = cz
		cols[12*of +  6] = cx
		cols[12*of +  7] = cy
		cols[12*of +  8] = cz
		cols[12*of +  9] = cx
		cols[12*of + 10] = cy
		cols[12*of + 11] = cz

	transform(p, s, c)

	return transform

def draw_arrays():
	draw(
		int(0.5*len(poss)),
		GL_QUADS,
		("v2f", poss),
		("c3B", cols)
	)

from ctypes import *

uniformf = {}
uniformf[1] = glUniform1f
uniformf[2] = glUniform2f
uniformf[3] = glUniform3f
uniformf[4] = glUniform4f

class Uniform:
	def __init__(uniform, program, uniform_name):
		uniform.id = glGetUniformLocation(program.id, uniform_name.encode())

	def set(uniform, *args):
		uniformf[len(args)](uniform.id, *args)

class Shader:
	def __init__(shader, path, shader_type):
		shader.id = glCreateShader(shader_type)
		source = open(path).read().encode()
		glShaderSource(shader.id, 1, cast(source, POINTER(c_char)), c_int(len(source)))

class Program:
	def __init__(program, *shaders):
		program.id = glCreateProgram()

		for shader in shaders:
			glAttachShader(program.id, shader.id)

		glLinkProgram(program.id)

		info_log_result = c_int(0)
		glGetProgramiv(program.id, GL_INFO_LOG_LENGTH, byref(info_log_result))
		info_log_str = create_string_buffer(info_log_result.value)
		glGetProgramInfoLog(program.id, info_log_result, None, info_log_str)
		if info_log_str.value:
			print(info_log_str.value)

		status = c_int(0)
		glGetProgramiv(program.id, GL_LINK_STATUS, status)
		if not status.value:
			length = c_int(0)
			glGetProgramiv(program.id, GL_INFO_LOG_LENGTH, length)
			log = c_buffer(length.value)
			glGetProgramInfoLog(program.id, len(log), None, log)
			print(log.value.decode())

	def enable(program):
		glUseProgram(program.id)

	def disable(program):
		glUseProgram(0)