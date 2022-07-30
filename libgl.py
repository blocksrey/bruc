from sys import platform
from ctypes import *

global gl

# this case isn't relevant to python3
if platform == "linux2":
	gl = CDLL("libOpenGL.so.0")

if platform == "linux":
	gl = CDLL("libGL.so.1")

if platform == "darwin":
	print("ahh, that's fine I guess")

if platform == "win32":
	print("EWWWW FUCK YOU")