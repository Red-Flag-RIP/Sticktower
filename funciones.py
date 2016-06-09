import pygame
from game import *

gray=(105,105,105)
almost_black=(57,57,57)
pygame.init()
fuente = pygame.font.Font(None, 36) 

class button(pygame.sprite.Sprite):
	pressed=0
	mposx=0
	mposy=0
	def __init__ (self,tam,pos):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([tam[0],tam[1]])
		self.image.fill(gray)
		self.rect=self.image.get_rect()
		self.rect.x=pos[0]
		self.rect.y=pos[1]
		self.tam=[tam[0],tam[1]]
		self.mouse=[self.mposx,self.mposy]
	def update(self):
		if self.mouse[0]>self.rect.x:
			self.image.fill(almost_black)
		


def dead():
    

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        pygame.display.update()
        clock.tick(15) 
