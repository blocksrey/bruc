from pyglet.gl import *
from ctypes import *

class Shader:
	def __init__(shader,path,type):
		shader.id=glCreateShader(type)

		source=open(path).read().encode()
		source_buffer_pointer=cast(c_char_p(source),POINTER(c_char))
		source_length=c_int(len(source))

		glShaderSource(shader.id,1,byref(source_buffer_pointer),source_length)

class Program:
	def __init__(program,*shaders):
		program.id=glCreateProgram()
		for shader in shaders:
			glAttachShader(program.id,shader.id)
		glLinkProgram(program.id)

		def debug():
			info_log_result=c_int(0)
			glGetProgramiv(program.id,GL_INFO_LOG_LENGTH,byref(info_log_result))
			info_log_str=create_string_buffer(info_log_result.value)
			glGetProgramInfoLog(program.id,info_log_result,None,info_log_str)
			if info_log_str.value:
				print(info_log_str.value)

		debug()

	def use(program):
		glUseProgram(program.id)

uniform_callbacks={}
uniform_callbacks[1]=glUniform1f
uniform_callbacks[2]=glUniform2f
uniform_callbacks[3]=glUniform3f
uniform_callbacks[4]=glUniform4f

class Uniform:
	def __init__(uniform,name):
		uniform.name=name.encode()
		#uniform.ids=()

	def attach(uniform,program):
		#uniform.ids+=(glGetUniformLocation(program.id,uniform.name),)
		uniform.id=glGetUniformLocation(program.id,uniform.name)

	def set(uniform,*args):
		uniform_callback=uniform_callbacks[len(args)]
		for uniform_id in uniform.ids:
			uniform_callback(uniform_id,*args)