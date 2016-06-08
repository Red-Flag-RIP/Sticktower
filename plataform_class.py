import pygame

brown=(205,133,63)

#generar plataformas de colision
class walls(pygame.sprite.Sprite):
	def __init__(self,w,h,p):
		pygame.sprite.Sprite.__init__(self)
		#apariencia del mapa
		self.image=pygame.Surface([w,h])
		self.rect=self.image.get_rect()
		self.rect.x=p[0]
		self.rect.y=p[1]

class visible(pygame.sprite.Sprite):
	def __init__(self,p):
		pygame.sprite.Sprite.__init__(self)
		#apariencia del mapa
		self.image=pygame.Surface([9,36])
		self.rect=self.image.get_rect()
		self.rect.x=p[0]
		self.rect.y=p[1]

class moving_line(pygame.sprite.Sprite):
	def __init__(self,w,p):
		pygame.sprite.Sprite.__init__(self)
		#apariencia del mapa
		self.image=pygame.Surface([w,1])
		self.rect=self.image.get_rect()
		self.rect.x=p[0]
		self.rect.y=p[1]

class plataform(pygame.sprite.Sprite):
	level=None
	d=3
	def __init__(self,p):
		pygame.sprite.Sprite.__init__(self)
		#apariencia del mapa
		self.image=pygame.image.load('images/plataform.png')
		self.rect=self.image.get_rect()
		self.rect.x=p[0]
		self.rect.y=p[1]
	
	def update(self):
		self.rect.x+=self.d
		online=pygame.sprite.spritecollide(self,self.level.line_list,False)
		for line in online:
			if self.rect.left<=line.rect.left:
				self.d=3
			if self.rect.right>=line.rect.right:
				self.d=-3

		
