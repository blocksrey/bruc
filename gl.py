from ctypes import *
from sys import platform
from shiz.lib import load_library

class c_void(Structure):
	# c_void_p is a buggy return type, converting to int, so
	# POINTER(None) == c_void_p is actually written as
	# POINTER(c_void), so it can be treated as a real pointer.
	_fields_ = [('dummy', c_int)]

gl = load_library("GL")

glcorearb = open("GL/glcorearb.h").read()

# these might not be right
types = {}
types["GLenum"] = c_uint
types["GLboolean"] = c_ubyte
types["GLbitfield"] = c_uint
types["GLvoid"] = None
types["GLbyte"] = c_char
types["GLshort"] = c_short
types["GLint"] = c_int
types["GLubyte"] = c_ubyte
types["GLushort"] = c_ushort
types["GLuint"] = c_uint
types["GLsizei"] = c_int
types["GLfloat"] = c_float
types["GLclampf"] = c_float
types["GLdouble"] = c_double
types["GLclampd"] = c_double
types["GLchar"] = c_char
types["void"] = None

ERROR = "SUCK IT"

# LMFAO THIS IS TRASH
def _get_restype(source, name):
	query = "APIENTRY " + name
	begin = None
	try:
		begin = source.index(query)
	except:
		return ERROR
	pdept = 0
	while 1:
		begin -= 1
		chara = source[begin]
		if chara == "*":
			pdept += 1
		if chara == "I":
			begin += 2
			break
	owari = source.index(" ", begin)
	ptype = source[begin:owari]
	for index in range(pdept):
		ptype = POINTER(ptype)
	return types[ptype]

# some kind of argument parser that i made
def _get_argtypes(source, name):
	query = name + " ("
	begin = None
	try:
		begin = source.index(query)
	except:
		return ERROR
	begin += len(query)
	owari = source.index(")", begin)
	uargs = source[begin:owari].split(",")
	fargs = ()
	for index in range(len(uargs)):
		param = uargs[index]
		ptype = None
		for separ in param.split(" "):
			try:
				ptype = types[separ]
				if ptype:
					break
			except:
				pass
		pdept = param.count("*")
		for index in range(pdept):
			ptype = POINTER(ptype)
		if ptype != None: # uhhhhh
			fargs += (ptype, )
	return fargs

# this is nice
def _get_constant(source, name):
	begin = None
	try:
		begin = source.index(name)
	except:
		return ERROR
	begin = source.index("0x", begin)
	owari = source.index("\n", begin)
	return int(source[begin:owari], 16)

def get_restype(name):
	restype = ERROR
	if restype == ERROR:
		restype = _get_restype(glcorearb, name)
	#if restype == ERROR:
	#	restype = _get_restype(glext, name)
	return restype

def get_argtypes(name):
	argtypes = ERROR
	if argtypes == ERROR:
		argtypes = _get_argtypes(glcorearb, name)
	#if argtypes == ERROR:
	#	argtypes = _get_argtypes(glext, name)
	return argtypes

def get_constant(name):
	constant = ERROR
	if constant == ERROR:
		constant = _get_constant(glcorearb, name)
	#if constant == ERROR:
	#	constant = _get_constant(glext, name)
	return constant

def get_function(name):
	restype = get_restype(name)
	if restype == ERROR:
		print("CANT FIND FUNCTION IN HEADER:", name)
		return ERROR
	argtypes = get_argtypes(name)
	if argtypes == ERROR:
		print("CANT FIND FUNCTION IN HEADER:", name)
		return ERROR
	function = gl[name]
	function.restype = restype
	function.argtypes = argtypes
	return function

glCreateShader = get_function("glCreateShader")
glShaderSource = get_function("glShaderSource")
glCreateProgram = get_function("glCreateProgram")
glAttachShader = get_function("glAttachShader")
glLinkProgram = get_function("glLinkProgram")
glGetProgramiv = get_function("glGetProgramiv")
glGetProgramInfoLog = get_function("glGetProgramInfoLog")
glUseProgram = get_function("glUseProgram")
glGetUniformLocation = get_function("glGetUniformLocation")

GL_INFO_LOG_LENGTH = get_constant("GL_INFO_LOG_LENGTH")

class Shader:
	def __init__(shader, path, type):
		shader.id = glCreateShader(type)

		source = open(path).read().encode()
		source_buffer_pointer = cast(c_char_p(source), POINTER(c_char))
		source_length = c_int(len(source))

		glShaderSource(shader.id, 1, byref(source_buffer_pointer), source_length)

class Program:
	def __init__(program, *shaders):
		program.id = glCreateProgram()
		for shader in shaders:
			glAttachShader(program.id, shader.id)
		glLinkProgram(program.id)

		def debug():
			info_log_result = c_int(0)
			glGetProgramiv(program.id, GL_INFO_LOG_LENGTH, byref(info_log_result))
			info_log_str = create_string_buffer(info_log_result.value)
			glGetProgramInfoLog(program.id, info_log_result, None, info_log_str)
			if info_log_str.value:
				print(info_log_str.value)

		debug()

	def use(program):
		glUseProgram(program.id)

uniform_callbacks = {}
uniform_callbacks[1] = get_function("glUniform1f")
uniform_callbacks[2] = get_function("glUniform2f")
uniform_callbacks[3] = get_function("glUniform3f")
uniform_callbacks[4] = get_function("glUniform4f")

class Uniform:
	def __init__(uniform, name):
		uniform.name = name.encode()
		#uniform.ids = ()

	def attach(uniform, program):
		#uniform.ids += (glGetUniformLocation(program.id, uniform.name), )
		uniform.id = glGetUniformLocation(program.id, uniform.name)

	def set(uniform, *args):
		uniform_callback = uniform_callbacks[len(args)]
		#for uniform_id in uniform.ids:
		uniform_callback(uniform.id, *args)