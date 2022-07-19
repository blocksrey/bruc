print("Start Killem 2D Client")




import pyglet
from pyglet.gl import *

pyglet.window.Window(800, 600, "Killem 2D")

glViewport(0, 0, 800, 600)

from vec2 import vec2
from vec3 import vec3
from gl import draw_rect
draw_rect(vec2(0, 0), vec2(1, 1), vec3(1, 0, 1))


import net_c



pyglet.app.run()