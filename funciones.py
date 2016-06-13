import pygame
from game import *

gray=(105,105,105)
almost_black=(57,57,57)
pygame.init()
fuente = pygame.font.Font('freesansbold.ttf', 26) 
clock=pygame.time.Clock()

def myquit():
	pygame.quit()
	sys.exit(0)

class button(pygame.sprite.Sprite):
	tipe=0
	pressed=0
	mouse=None
	text=None
	action=0
	def __init__ (self,pos):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/button.png')
		self.image.fill(gray)
		self.rect=self.image.get_rect()
		self.rect.x=pos[0]
		self.rect.y=pos[1]
	def update(self):
		if self.mouse[0]>=self.rect.left and self.mouse[0]<=self.rect.right and self.mouse[1]>=self.rect.top and self.mouse[1]<=self.rect.bottom:
			self.image=pygame.image.load('images/onbutton.png')
		else:
			self.image=pygame.image.load('images/button.png')
		if self.mouse[0]>=self.rect.left and self.mouse[0]<=self.rect.right and self.mouse[1]>=self.rect.top and self.mouse[1]<=self.rect.bottom and self.pressed==1:
			self.action=1
def music(archivo):
	pygame.mixer.music.load(archivo)
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(0.3)




		
        



