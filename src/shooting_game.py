from game_core import *
import math
import random

image_player = image('spaceship_own.png')
image_shot = image('bullet_own.png')
image_laser = image('laser.png')
image_missile = image('homing_own.png')
image_option = image('option.png')

sound_shot = sound('sounds_shot.wav')
sound_laser = sound('sounds_laser.wav')
sound_missile = sound('sounds_missile.wav')
sound_treasure = sound('sounds_treasure.wav')

SW, SH = 1, 9/16
options = []


def shot(s):
    s.x += s.vx
    s.y += s.vy

    if abs(s.x) > SW+s.sx or abs(s.y) > SH+s.sx:
        s.life = 0


def new_shot(x, y, v, dir, n, angle):
    for i in range(n):
        if n > 1:
            r = (dir + angle / (n-1) * (i - (n-1) / 2))
        else:
            r = dir

        rad = r * math.pi * 2

        vx = math.cos(rad) * v
        vy = math.sin(rad) * v

        create_object(shot, image_shot, 0.02, x, y, vx, vy, r=r)


def laser(l):
    l.x += l.vx

    if l.parent:
        l.y = l.parent.y

    if abs(l.x) > SW+l.sx or abs(l.y) > SH+l.sx:
        l.life = 0


def homing_missile(h):
    target = None
    target_d = float('inf')

    for e in group(enemy):
        d = math.dist((h.x, h.y), (e.x, e.y))

        if d < target_d:
            target, target_d = e, d

    vdir = math.atan2(h.vy, h.vx) / math.pi / 2

    if target:
        tdir = math.atan2(target.y-h.y, target.x-h.x) / math.pi / 2

        if vdir-tdir > 0.5:
            tdir += 1
        if tdir-vdir > 0.5:
            tdir -= 1

        vdir += (tdir - vdir) * 0.1
        v = math.dist((h.vx, h.vy), (0, 0))
        rad = vdir * math.pi * 2
        h.vx = math.cos(rad) * v
        h.vy = math.sin(rad) * v

    h.x += h.vx
    h.y += h.vy
    h.r = vdir

    if h.time % 2 == 0:
        create_object(homing_tail, image_missile, h.sx, h.x, h.y, r=h.r)

    h.time += 1

    if abs(h.x) > SW+h.sx or abs(h.y) > SH+h.sy:
        h.life = 0


def homing_tail(ht):
    ht.sy *= 0.95

    if ht.sy < 0.01:
        ht.life = 0


def option(o):
    o.time += 1

    o.sx = o.sy = 0.06 + math.sin(o.time * 0.2) * 0.01

    if o.tx[-1] != o.target.x or o.ty[-1] != o.target.y:
        o.tx.append(o.target.x)
        o.ty.append(o.target.y)
        o.x, o.y = o.tx[0], o.ty[0]
        del o.tx[0], o.ty[0]


def dropped_option(do):
    do.x += do.vx
    do.y += do.vy


def enemy(e):
    pass


def player(p):
    v = 0.02

    if key(A):
        p.x -= v
    if key(D):
        p.x += v
    if key(W):
        p.y += v
    if key(S):
        p.y -= v

    p.x = max(-SW+p.sx, min(SW-p.sx, p.x))
    p.y = max(-SH, min(SH, p.y))
    p.time -= 1

    if key(Z) and p.time <= 0:
        sound_shot.play()
        for o in group(player, option):
            new_shot(o.x, o.y, 0.05, 0, 1, 0.04)
        p.time = 5

    elif key(X):
        sound_laser.play()
        for o in group(player, option):
            create_object(laser, image_laser, 0.05, o.x, o.y, 0.07, parent=o)

    elif key(C) and p.time <= 0:
        sound_missile.play()
        for o in group(player, option):
            create_object(homing_missile, image_missile, 0.08, o.x, o.y, 0.03, life=10)
            p.time = 30


def stage(s):
    if random.random() < 0.001 and len(options) <3:
        size = 0.06
        create_object(dropped_option, image_option, size, SW+size, random.uniform(-SH+size, SH-size), -0.005, isOption=True)


def start():
    global options
    options = []

    score()

    create_object(player, image_player, 0.15, -0.9, 0)

    create_object(stage)


run(start, 1080, 720, (0.1, 0.1, 0.2), False, (1, 1, 1))
