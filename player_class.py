import pygame
from game import *


class Player(pygame.sprite.Sprite):
	image=None
	level=None
	movx=0
	movy=0
	contador=-1
	itr=7
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#apariencia del jugador
		self.image=pygame.image.load('images/player_startright.png').convert_alpha()
		#self.image=pygame.Surface(imagen)
		self.rect=self.image.get_rect()
		self.rect.x=48
		self.rect.y=height-self.rect.height
	
	def look(self):
		if self.movx > 0:
			if self.contador<self.itr:
				self.image=pygame.image.load('images/player_run_right1.png').convert_alpha()
				self.contador+=1
			if self.contador>=self.itr and self.contador <=self.itr*2:
				self.image=pygame.image.load('images/player_run_right2.png').convert_alpha()
				self.contador+=1
			if self.contador>=self.itr*2 and self.contador <=self.itr*3:
				self.image=pygame.image.load('images/player_run_right3.png').convert_alpha()
				self.contador+=1
			if self.contador>=self.itr*3 and self.contador<=self.itr*4:
				self.image=pygame.image.load('images/player_run_right4.png').convert_alpha()
				self.contador+=1
			if self.contador>=self.itr*4 and self.contador<=self.itr*5:
				self.image=pygame.image.load('images/player_run_right4.png').convert_alpha()
				self.contador+=1
			if self.contador>=self.itr*5 and self.contador<=self.itr*6:
				self.image=pygame.image.load('images/player_run_right5.png').convert_alpha()
				self.contador+=1
			if self.contador==self.itr*6:
				self.contador=0
				self.image=pygame.image.load('images/player_run_right1.png').convert_alpha()
		if self.movx==0:
			self.contador=0
			self.image=pygame.image.load('images/player_startright.png').convert_alpha()
		
		if self.movx < 0:
			if self.contador<self.itr:
				self.image=pygame.image.load('images/player_run_left1.png').convert_alpha()
				self.contador+=1
			if self.contador>=self.itr*1 and self.contador <=self.itr*2:
				self.image=pygame.image.load('images/player_run_left2.png').convert_alpha()
				self.contador+=1
			if self.contador>=self.itr*2 and self.contador <=self.itr*3:
				self.image=pygame.image.load('images/player_run_left3.png').convert_alpha()
				self.contador+=1
			if self.contador>=self.itr*3 and self.contador<=self.itr*4:
				self.image=pygame.image.load('images/player_run_left4.png').convert_alpha()
				self.contador+=1
			if self.contador>=self.itr*4 and self.contador<=self.itr*5:
				self.image=pygame.image.load('images/player_run_left4.png').convert_alpha()
				self.contador+=1
			if self.contador>=self.itr*5 and self.contador<=self.itr*6:
				self.image=pygame.image.load('images/player_run_left5.png').convert_alpha()
				self.contador+=1
			if self.contador==self.itr*6:
				self.contador=0
				self.image=pygame.image.load('images/player_run_left1.png').convert_alpha()
		if self.movx==0:
			self.contador=0
			self.image=pygame.image.load('images/player_startright.png').convert_alpha()

	def gravity(self):
		if self.movy==0:
			self.movy=1
		else:
			self.movy+=.35
		if self.rect.y >= height-self.rect.height and self.movy >=0:
			self.movy=0
			self.rect.y = height - self.rect.height
	def jump(self):
		self.rect.y += 2
		collition_ls=pygame.sprite.spritecollide(self,self.level.wall,False)
		coll_movls=pygame.sprite.spritecollide(self,self.level.plataform_list,False)
		self.rect.y -= 2
        
		# Si es posible saltar, aumentamos velocidad hacia arriba
		if len(collition_ls) > 0 or self.rect.bottom >= height:
			self.movy = -12

		#plataforma en movimiento
		if len(coll_movls) > 0 or self.rect.bottom >= height:
			self.movy = -12
			
	def update(self):
		self.look()
		self.gravity()
		self.rect.x+=self.movx		
		collition_ls=pygame.sprite.spritecollide(self,self.level.wall,False)
		coll_movls=pygame.sprite.spritecollide(self,self.level.plataform_list,False)

		#colision por los lados
		for muro in collition_ls:
            		if self.movx > 0:
				self.rect.right = muro.rect.left
			elif self.movx < 0:
				self.rect.left = muro.rect.right
		for muro in coll_movls:
            		if self.movx > 0:
				self.rect.right = muro.rect.left
			elif self.movx < 0:
				self.rect.left = muro.rect.right

		#colision superior/inferior
		self.rect.y+=self.movy
		collition_ls=pygame.sprite.spritecollide(self,self.level.wall,False)
		coll_movls=pygame.sprite.spritecollide(self,self.level.plataform_list,False)
		for muro in collition_ls:
            		if self.movy > 0:
				self.rect.bottom = muro.rect.top
				self.movy=0
			elif self.movy < 0:
				self.rect.top = muro.rect.bottom
			self.movy=0
		for muro in coll_movls:
            		if self.movy > 0:
				self.rect.bottom = muro.rect.top
				self.movy=0
			elif self.movy < 0:
				self.rect.top = muro.rect.bottom
				
			self.movy=0	
