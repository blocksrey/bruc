from pyglet.window import Window
from caller import Caller
from v2 import V2

the_window=Window(222,173,'bruc',1)#easter egg much?

on_key_press_caller=Caller()
@the_window.event
def on_key_press(code,mod):
	on_key_press_caller.fire(code,mod)

on_key_release_caller=Caller()
@the_window.event
def on_key_release(code,mod):
	on_key_release_caller.fire(code,mod)

on_mouse_scroll_caller=Caller()
@the_window.event
def on_mouse_scroll(px,py,dx,dy):
	on_mouse_scroll_caller.fire(V2(px,py),V2(dx,dy))

on_mouse_press_caller=Caller()
@the_window.event
def on_mouse_press(px,py,code,mod):
	on_mouse_press_caller.fire(V2(px,py),code,mod)

on_mouse_motion_caller=Caller()
@the_window.event
def on_mouse_release(px,py,code,mod):
	on_mouse_motion_caller.fire(V2(px,py),code,mod)

on_draw_caller=Caller()
@the_window.event
def on_mouse_motion(px,py,dx,dy):
	on_mouse_motion_caller.fire(V2(px,py),V2(dx,dy))

on_draw_caller=Caller()
@the_window.event
def on_draw():
	on_draw_caller.fire()

on_resize_caller=Caller()
@the_window.event
def on_resize(sx,sy):
	on_resize_caller.fire(V2(sx,sy))