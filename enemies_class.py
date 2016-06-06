import pygame
from game import *
from player_class import *

class saw(pygame.sprite.Sprite):
	level=None
	d=-2
	contador=0
	def __init__(self,p):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('saw.png')
		self.rect=self.image.get_rect()
		self.rect.x=p[0]
		self.rect.y=p[1]
	def update(self):
		self.rect.x+=self.d
		online=pygame.sprite.spritecollide(self,self.level.line_list,False)
		for line in online:
			if self.rect.left<=line.rect.left:
				self.d=2
			if self.rect.right>=line.rect.right:
				self.d=-2
		if self.contador<=20:
			self.image=pygame.image.load('saw.png')
			self.contador+=1
		if self.contador >=20 and self.contador<=40:
			self.image=pygame.image.load('saw2.png')
			self.contador+=1
		if self.contador==40:
			self.contador=0

class arrow(pygame.sprite.Sprite):
	level=None
	d=-4
	def __init__(self,p):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('arrow_right.png')
		self.rect=self.image.get_rect()
		self.rect.x=p[0]
		self.rect.y=p[1]
		self.xin=p[0]
	def update(self):
		self.rect.x+=self.d
		if self.rect.x<=25:
			self.rect.x=self.xin

class guardian(pygame.sprite.Sprite):
	level=None
	contador=0
	def __init__(self,p):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('guardian.png')
		self.rect=self.image.get_rect()
		self.rect.x=p[0]
		self.rect.y=p[1]
	
