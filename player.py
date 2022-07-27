import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.Surface((32, 64))
		self.image.fill('red')
		self.rect = self.image.get_rect(topleft=pos)

		# player movement
		self.v = pygame.math.Vector2(0, 0)
		self.s = 8
		self.g = 0.8
		self.jump_s = -16

	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.v.x = 1
		elif keys[pygame.K_LEFT]:
			self.v.x = -1
		else:
			self.v.x = 0

		if keys[pygame.K_SPACE]:
			self.jump()

	def apply_g(self):
		# analytical solution
		self.rect.y += self.v.y + 0.5*self.g*self.g
		self.v.y += self.g

	def jump(self):
		self.v.y = self.jump_s

	def update(self):
		self.get_input()
