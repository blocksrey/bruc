import pyglet
from random import random,seed
from math import tau
import character
from shash import shash2
from bullet import Bullet
from v2 import cang

explosions=[]

class Explosion:
	def __init__(self,p):
		seed(shash2(p.x,p.y))
		for x in range(8):
			Bullet(p,300*cang(tau*random()))
		pyglet.media.load('sounds/explode'+str(int(2*random()))+'.mp3').play().pitch=0.9+0.1*random()
		offset=character.the_character.p-p
		character.the_character.impulse(100*offset/offset.square())

	def step(self,dt):
		pass

def step(dt):
	for explosion in explosions:
		explosions.step(dt)