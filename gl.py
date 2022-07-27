from vec3 import Vec3
from pyglet.graphics import draw
from pyglet.gl import *

# p0 + (tx, ty)*s : 0 <= tx < 1 && 0 <= ty < 1
def draw_rect(p0, s, c):
	p1 = p0 + s
	draw(
		6,
		GL_TRIANGLES,
		("v2f", (
			p0.x, p0.y,
			p1.x, p1.y,
			   0, p1.y,
			p0.x, p0.y,
			p1.x, p1.y,
			p1.x,    0
		)),
		("c3f", (
			c.x, c.y, c.z,
			c.x, c.y, c.z,
			c.x, c.y, c.z,
			c.x, c.y, c.z,
			c.x, c.y, c.z,
			c.x, c.y, c.z
		))
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







