print('Start Killem 2D Client')

from vec2 import Vec2
from vec3 import Vec3
from math import sin, atan2, sqrt, tan, pi
import pyglet

from pyglet import font
import vec2
import vec3

from json import load

from pyglet.gl import *
from glutil import *

import os

data = load(open("settings.json"))


pyglet.options["vsync"] = True

background_color = (1, 1, 1)

pyglet.font.add_directory(f"gui/fonts/{data['font-family']}")

font = data["font-family"]
font = font.replace("sans-alternates", "Montserrat Alternates")
font = font.replace("sans-serif", "Playfair Display")
font = font.replace("sans", "Montserrat")

data = {
    "song" : "Bruc said what?",
    "music" : False,
    "effects" : False,
    "fps" : False,
    "username" : None,
}
player_stats = f"""
<h5>Player statistics</h5> 
<br>
<em>Kills:</em> 0
<br>
<em>Gold:</em> 100
<br>
<em>Wins:</em> 5
<br>
<em>Defeats:</font></em> 1
</font>
"""

screen = pyglet.canvas.Display().get_default_screen() # Get pyglet screen

title = pyglet.resource.image("gui/title.png")
play = pyglet.resource.image("gui/play.png")
exit = pyglet.resource.image("gui/exit.png")
blue_button_normal = pyglet.resource.image("gui/blue_button_normal.png")
blue_button_hover = pyglet.resource.image("gui/blue_button_hover.png")
blue_button_press = pyglet.resource.image("gui/blue_button_press.png")
checkbox_true = pyglet.resource.image("gui/checkbox_true.png")
checkbox_false = pyglet.resource.image("gui/checkbox_false.png")
checkbox_hover = pyglet.resource.image("gui/checkbox_hover.png")

music = {
    "Bruc said what?" : "sounds/track1.ogg",
    "Yeah Bruc said that" : "sounds/track2.ogg",
    "What you say to Bruc" : "sounds/track3.ogg"
}

pyglet.options["advanced_font_features"] = True


class TextWidget:
    
    def __init__(self, text, x, y, width, window, font):
        self.document = pyglet.text.document.UnformattedDocument(text)
        self.document.set_style(0, len(self.document.text), dict(color=(0, 0, 0, 255), font_name=font))

        font = self.document.get_font()
        height = font.ascent - font.descent + 15

        self.layout = pyglet.text.layout.IncrementalTextLayout(self.document, width, height)
        self.layout.position = x, y + 10
        self.layout.anchor_y = "center"

        self.caret = pyglet.text.caret.Caret(self.layout)
        
        # Rectangular outline
        pad = 5
        
        self.rectangle = pyglet.shapes.BorderedRectangle(x - pad, y - pad + 7, width + pad, height + pad, 3, border_color=(148, 148, 148))

        window.push_handlers(self)
    
    def draw(self):
        self.rectangle.draw()
        self.layout.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.rectangle.border_color = 148, 148, 148

        if self.hit_test(x, y):
            self.rectangle.border_color = 100, 100, 100

    def on_mouse_press(self, x, y, buttons, modifiers):
        if self.hit_test(x, y):
            self.layout.document.text = ""

    def hit_test(self, x, y):
        return (0 < x - self.layout.x < self.layout.width and
                0 < y - self.layout.y < self.layout.height)


class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        pyglet.window.Window.__init__(self, 666, 519, "", 0, style=Window.WINDOW_STYLE_DIALOG)

        self.batch = pyglet.graphics.Batch()
  
        self.entry = TextWidget("Enter username", 333, 229, 230, self, font)
        
        self.frame = pyglet.gui.Frame(self)

        try:
            self.background = pyglet.graphics.OrderedGroup(0)
        except:
            self.background = pyglet.graphics.Group(order=0)

        self.play_button = pyglet.gui.PushButton(450, 93,
                                                 blue_button_press,
                                                 blue_button_normal,
                                                 blue_button_hover,
                                                 batch=self.batch,
                                                 group=self.background
                                                )
        
        self.exit_button = pyglet.gui.PushButton(450, 23,
                                                 blue_button_press,
                                                 blue_button_normal,
                                                 blue_button_hover,
                                                 batch=self.batch,
                                                 group=self.background
                                                )
        
        self.music_button = pyglet.gui.ToggleButton(333, 440,
                                                    checkbox_false,
                                                    checkbox_true,
                                                    checkbox_true,
                                                    batch=self.batch
                                                   )

        self.effects_button = pyglet.gui.ToggleButton(333, 380,
                                                      checkbox_false,
                                                      checkbox_true,
                                                      checkbox_true,
                                                      batch=self.batch
                                                     )

        self.fps_button = pyglet.gui.ToggleButton(333, 320,
                                                  checkbox_false,
                                                  checkbox_true,
                                                  checkbox_true,
                                                  batch=self.batch
                                                 )

        self.frame.add_widget(self.play_button)
        self.frame.add_widget(self.exit_button)
        self.frame.add_widget(self.music_button)
        self.frame.add_widget(self.effects_button)
        self.frame.add_widget(self.fps_button)

        try:
            self.foreground = pyglet.graphics.OrderedGroup(1)
        except:
            self.foreground = pyglet.graphics.Group(0)
            
        self.play_label = pyglet.text.Label("Play", font_name=font, font_size=14,
                                             x=500, y=113, color=(0, 0, 0, 255),
                                             batch=self.batch, group=self.foreground)

        self.exit_label = pyglet.text.Label("Exit", font_name=font, font_size=14,
                                            x=500, y=43, color=(0, 0, 0, 255),
                                            batch=self.batch, group=self.foreground)

        self.music_label = pyglet.text.Label("Play music", font_name=font, font_size=12,
                                             x=393, y=450, color=(0, 0, 0, 255),
                                             batch=self.batch, group=self.foreground)
        self.effects_label = pyglet.text.Label("Play effects", font_name=font, font_size=12,
                                             x=393, y=390, color=(0, 0, 0, 255),
                                             batch=self.batch, group=self.foreground)
        self.effects_label = pyglet.text.Label("Show fps", font_name=font, font_size=12,
                                             x=393, y=330, color=(0, 0, 0, 255),
                                             batch=self.batch, group=self.foreground)

        self.player_stats = pyglet.text.HTMLLabel(player_stats, x=23, y=200,
                                                  multiline=True, width=280,
                                                  batch=self.batch
                                                 )
        self.credits = pyglet.text.Label("Gameplay and design by Team 7Teen.",
                                         font_name=font, font_size=9,
                                         x=23, y=20, color=(0, 0, 0, 255),
                                         batch=self.batch
                                        )
        
        self.title = pyglet.sprite.Sprite(title, 20, self.height - 100, batch=self.batch)
        self.play = pyglet.sprite.Sprite(play, 456, 101.5, batch=self.batch, group=self.foreground)
        self.exit = pyglet.sprite.Sprite(exit, 456, 31, batch=self.batch, group=self.foreground)

        self.play.scale = 0.75
        self.exit.scale = 0.75

        self.labels = []

        x = 425

        for value in music:
            x -= 20
            label = pyglet.text.Label(value, font_name=font, font_size=11,
                                      x=28, y=x, color=(0, 0, 0, 255),
                                      batch=self.batch, group=self.foreground)
            self.labels.append(label)

        self.box = pyglet.shapes.BorderedRectangle(23, 230, 280, 195, border=3, batch=self.batch)

        self.play_button.set_handler("on_release", self._play)
        self.exit_button.set_handler("on_release", self._exit)
        self.music_button.set_handler("on_toggle", self.music)
        self.effects_button.set_handler("on_toggle", self.effects)
        self.fps_button.set_handler("on_toggle", self.fps)

        self.music_button.value = True
        self.effects_button.value = True
        self.fps_button.value = True

    def _play(self):
        """Called when the play button is pressed."""
        
        data["username"] = self.entry.layout.document.text
        self.close()
    
    def _exit(self):
        """Called when the exit button is pressed."""
        
        os._exit(0)
    
    def music(self, value):
        """Called when the music checkbox is pressed."""

        data["music"] = not value
    
    def effects(self, value):
        """Called when the effects checkbox is pressed."""

        data["effects"] = not value
    
    def fps(self, value):
        """Called when the fps checkbox is pressed."""

        data["fps"] = not value

    def on_draw(self):
        pyglet.gl.glClearColor(1, 1, 1, 1)

        self.clear()
        self.batch.draw()
        self.entry.draw()
        
    def on_mouse_motion(self, x, y, dx, dy):
        for label in self.labels:
            if x > label.x - label.content_width and \
                x < label.x + label.content_width and \
                y > label.y - label.content_height and \
                y < label.y + label.content_height:
                label.document.set_style(0, len(label.text), dict(font_size=12))
            else:
                label.document.set_style(0, len(label.text), dict(font_size=11))

    def on_mouse_press(self, x, y, button, modifiers):
        for label in self.labels:
            if x > label.x - label.content_width / 2 and \
                x < label.x + label.content_width / 2 and \
                y > label.y - label.content_height / 2 and \
                y < label.y + label.content_height / 2:
                label.document.set_style(0, len(label.text), dict(bold=True))
                data["song"] = music[label.document.text]
                
                for _label in self.labels:
                    if _label == label:
                        break
                    _label.document.set_style(0, len(label.text), dict(bold=False))
            else:
                label.document.set_style(0, len(label.text), dict(bold=False))

        self.entry.caret.on_mouse_press(x, y, button, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.entry.caret.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_text(self, text):
        self.entry.caret.on_text(text)

    def on_text_motion(self, motion):
        self.entry.caret.on_text_motion(motion)

    def on_text_motion_select(self, motion):
        self.entry.caret.on_text_motion_select(motion)
            
    def on_close(self):
        # Break out of the whole application event loop
        os._exit(0)

Window()

pyglet.app.run()

window0 = pyglet.window.Window(1110, 865, 'Killem 2D') # easter egg much?

VAO_MODE = gl_info.have_version(2) and 0
GLOBAL_ACCELERATION = Vec2(0, -128)

RELEASE = 0
if RELEASE:
    import gc; gc.disable() # no garbage collection
    pyglet.options['debug_gl'] = 0 # no debug

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glClearColor(1, 1, 1, 1)

camp = Vec2(0, 0)
camd = 1
camo = Vec2(1, 0)


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

# this might change my life as a programmer

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
    print('shoot @', t)
    return 0.1

sequencer0 = Sequencer()

sequencer0.dump(3)
sequencer0.call(get_cooldown)
sequencer0.dump(3.1)



















from mesh2 import Mesh2


rect_inde = -1
rect_poss = []
rect_cols = []
collision_meshes = []

class Terrain:
    def __init__(self, p, s, c):
        global rect_inde; rect_inde += 1
        global rect_poss; rect_poss += [None]*8 # this is probably slow
        global rect_cols; rect_cols += [None]*12

        self.i = rect_inde

        global collision_meshes; collision_meshes += [Mesh2([vec2.null])]

        self.edit(p, s, c)

    def edit(self, p, s, c):
        i = self.i
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

        collision_meshes[i].update_vertices([
            Vec2(px + 1*sx, py + 1*sy),
            Vec2(px + 1*sx, py + 0*sy),
            Vec2(px + 0*sx, py + 0*sy),
            Vec2(px + 0*sx, py + 1*sy)
        ])

if VAO_MODE: # OpenGL 2.x
    rect_program = Program(
        Shader('shaders/rectv.glsl', GL_VERTEX_SHADER),
        Shader('shaders/rectf.glsl', GL_FRAGMENT_SHADER)
    )

    rect_camd_uniform = glGetUniformLocation(rect_program.id, b'camd')
    rect_camp_uniform = glGetUniformLocation(rect_program.id, b'camp')
    rect_camo_uniform = glGetUniformLocation(rect_program.id, b'camo')
    rect_wins_uniform = glGetUniformLocation(rect_program.id, b'wins')

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

def glPerspective(vt, ar, z0, z1):
        hh = tan(pi/180*vt)*z0
        hw = ar*hh
        glFrustum(-hw, hw, -hh, hh, z0, z1)

bullet_inde = -1
bullet_poss = []
bullet_opac = []

def add_bullet_geometry():
    global bullet_inde; bullet_inde += 1
    global bullet_poss; bullet_poss += [None]*8
    global bullet_opac; bullet_opac += [None]*1

    return bullet_inde

if VAO_MODE:
    bullet_program = Program(
        Shader('shaders/bulletv.glsl', GL_VERTEX_SHADER),
        Shader('shaders/bulletf.glsl', GL_FRAGMENT_SHADER)
    )

    bullet_camd_uniform = glGetUniformLocation(bullet_program.id, b'camd')
    bullet_camp_uniform = glGetUniformLocation(bullet_program.id, b'camp')
    bullet_camo_uniform = glGetUniformLocation(bullet_program.id, b'camo')
    bullet_wins_uniform = glGetUniformLocation(bullet_program.id, b'wins')

    def draw_bullets():
        pyglet.graphics.draw(
            4*(bullet_inde + 1),
            GL_QUADS,
            ('v2f', bullet_poss)
        )
else:
    def draw_bullets():
        for i in range(bullet_inde + 1):
            glColor4f(1, 0, 0, bullet_opac[i])

            glVertex2f(bullet_poss[8*i + 0], bullet_poss[8*i + 1])
            glVertex2f(bullet_poss[8*i + 2], bullet_poss[8*i + 3])
            glVertex2f(bullet_poss[8*i + 4], bullet_poss[8*i + 5])
            glVertex2f(bullet_poss[8*i + 6], bullet_poss[8*i + 7])


def hsv(h, s, v):
    C = v*s
    m = v - C
    h *= 6
    X = m + C*(1 - abs(h%2 - 1))
    C += m
    if   h < 1: r, g, b = C, X, m
    elif h < 2: r, g, b = X, C, m
    elif h < 3: r, g, b = m, C, X
    elif h < 4: r, g, b = m, X, C
    elif h < 5: r, g, b = X, m, C
    else:       r, g, b = C, m, X
    return r, g, b

#def hsv(h, s, v):
#   C = v*s
#   m = v - C
#   h *= 6
#   X = m + C*h
#   C += m
#   o = [0, 0, 0]
#   o[floor(0.45*h%3)] = C
#   o[floor((1 - h)%3)] = X
#   o[floor((2 - 0.5*h)%3)] = m
#   return tuple(o)

#from random import random
#for x in range(40):
#   r, g, b = random(), random(), random()
#   h0, s0, v0 = hsv0(r, g, b)
#   h1, s1, v1 = hsv(r, g, b)
#   print(h0, s0, v0)
#   print(h1, s1, v1)
#   print(h0 == h1 and s0 == s1 and v0 == v1)
#   print()




# this should be a standard
def calc_skin_color(a):
    h = 0.25*(1 - a)*a
    s = 0.25 + 0.5*a
    v = 1 - 0.75*a
    return hsv(h, s, v)

def calc_clothing_color(a, b, c, d):
    h0 = a + 2*a*(a - 1)**4
    s0 = 1 - b
    v0 = 0.5*(1 - c*c)
    h1 = b + 2*b*(b - 1)**4
    s1 = 2/3*c**1.5
    v1 = 1/3*(1 + d)*(1 - d*d)
    return hsv(h0, s0, v0), hsv(h1, s1, v1)

characters = []

character_inde = -1
character_poss = []
character_cols = []


# i need to work on state (user input's affect on the system)



class Character:
    def __init__(self, p, v, c):
        self.p = p
        self.v = v
        self.c = c
        self.m = vec2.null
        self.t = vec2.null

        global character_inde; character_inde += 1
        global character_poss; character_poss += [None]*8
        global character_cols; character_cols += [None]*12

        self.i = character_inde

        self.edit(p, vec2.null, vec3.null)

        characters.append(self)

    def edit(self, p, o, c):
        i = self.i
        px, py = p.x, p.y
        cx, cy, cz = c.x, c.y, c.z

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

        character_cols[12*i +  0] = cx
        character_cols[12*i +  1] = cy
        character_cols[12*i +  2] = cz
        character_cols[12*i +  3] = cx
        character_cols[12*i +  4] = cy
        character_cols[12*i +  5] = cz
        character_cols[12*i +  6] = cx
        character_cols[12*i +  7] = cy
        character_cols[12*i +  8] = cz
        character_cols[12*i +  9] = cx
        character_cols[12*i + 10] = cy
        character_cols[12*i + 11] = cz

    def step(self, dt):
        p0 = self.p

        self.v.x += (self.t.x - self.v.x)*dt*10
        self.p.x += self.v.x*dt*20

        self.p, self.v = aero_projectile(self.p, self.v, GLOBAL_ACCELERATION, 0.01, dt)

        d = self.p - p0
        cz, cn = map_raycast(Ray2(p0, d))
        if d.norm() - cz > 1e-4: # touch
            self.p = p0 + d.unit()*cz + cn*1e-4
            self.v = self.v.project_norm(cn)
            self.cj = 1
        else: # air
            self.cj = 0
            pass
            #print("AIR")

        character_tick = 14*tick*self.t.norm()
        s = sin(character_tick)
        ox = 0
        oy = s*s - 0.2
        character_o = 0.2*sin(character_tick)
        self.edit(self.p + Vec2(ox, oy), vec2.cang(character_o), self.c)

    def jump(self):
        if self.cj:
            self.v.y += 40

    def try_to_move_lol(self, t):
        self.t = Vec2(t, 0)

    def use(self):
        global the_character; the_character = self
        print('Use character', self)

if VAO_MODE:
    def draw_characters():
        pyglet.graphics.draw(
            4*(character_inde + 1),
            GL_QUADS,
            ('v2f', character_poss),
            ('c3f', character_cols)
        )
else:
    def draw_characters():
        for i in range(character_inde + 1):
            glColor4f(character_cols[12*i + 0], character_cols[12*i + 1], character_cols[12*i + 2], 1)

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
                    Terrain(Vec2(px, py + 0.9*sy), Vec2(sx, 0.1*sy), char_cols[ch])
                elif ch != ' ': # newline case is handled naturally :P:P
                    Terrain(Vec2(px, py), Vec2(sx, sy), char_cols[ch])

                if ch == 'P':
                    Character(Vec2(px, py + 10), Vec2(0, 1), Vec3(*calc_skin_color(random()))).use()

                ix = ix1
                ch = ch1

            ix1 += 1
        iy += 1








from math import inf

def map_raycast(r):
    fz = r.h.norm()
    fn = vec2.null
    for rectm in collision_meshes:
        cz, cn = rectm.push_point(r)
        if cz < fz:
            fz = cz
            fn = cn
    return fz, fn











bullets = []


from ray2 import Ray2

# projectile with drag (only accurate for small t)
def aero_projectile(p, v, g, k, t):
    a = g - v*v.norm()*k
    return p + v*t + a*t*t*0.5, v + a*t # p, p'

class Bullet:
    def __init__(self, p, v):
        self.p, self.v = p, v
        self.i = add_bullet_geometry()
        self.step(vec2.null, 0, 0.0001) # god dammit
        bullets.append(self)

    def step(self, g, k, dt):
        p0 = self.p
        self.p, self.v = aero_projectile(self.p, self.v, g, k, dt)
        cz, cn = map_raycast(Ray2(p0, self.p - p0))
        d = self.p - p0
        if d.norm() - cz > 1e-4:
            self.p = p0 + d.unit()*cz
            self.v = self.v.reflect(cn)*0.75
        self.edit(self.i, self.p, self.v*dt)

    def edit(self, i, p, d):
        px, py = p.x, p.y
        dx, dy = d.x, d.y

        h = sqrt(dx*dx + dy*dy) # division by 0
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

    def destroy():
        pass



from time import time
from random import random

build_map("maps/map0.bm")

camo = vec2.cang(0)
camd = 100

def step(dt):
    global tick; tick = time()

    for bullet in bullets:
        bullet.step(GLOBAL_ACCELERATION, 0.01, dt)

    #character_index = -1 # technically this state is correct because it's not in the scope of character
    for character in characters:
        character.step(dt)

    global camp; camp = the_character.p

pyglet.clock.schedule_interval(step, 1/600) # this is bad but whatever

def update_wins_uniforms(wins):
    glUseProgram(rect_program.id)
    glUniform2f(rect_wins_uniform, wins.x, wins.y)

    glUseProgram(bullet_program.id)
    glUniform2f(bullet_wins_uniform, wins.x, wins.y)

#state0.on('draw', 'wins').connect(update_wins_uniforms) # on draw (if wins is different since last draw)

#def use_rect_program():
#   glUseProgram(rect_program.id)

#rect_uniform_change = state0.depend('rect_camp_uniform', 'rect_camo_uniform')
#rect_uniform_change.before.connect(use_rect_program)

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
        #glClearColor(*hsv0(0.3*tick%1, 1, 1), 1)

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

m0x, m0y = 0, 0
m1x, m1y = 0, 0

@window0.event
def on_key_press(code, mod):
    key = chr(code)
    if key == ' ':
        the_character.jump()
    else:
        the_character.try_to_move_lol(key == 'd' and 1 or key == 'a' and -1 or 0)

@window0.event
def on_key_release(code, mod):
    key = chr(code)
    if key != ' ':
        the_character.try_to_move_lol(key == 'd' and 0 or key == 'a' and 0 or 0) # this is wrong but whatever lol

@window0.event
def on_mouse_scroll(px, py, dx, dy):
    global camd; camd += 2*dy

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

    m0x, m0y = the_character.p.x, the_character.p.y

    Bullet(Vec2(m0x, m0y), Vec2(m1x - m0x, m1y - m0y)*10)

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

    # label.draw()

pyglet.app.run()