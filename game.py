import pygame


#colors
white=(255,255,255)

#global const

real_width=720
real_height=1080


width=1200
height=540



#generar plataformas de colision
class walls(pygame.sprite.Sprite):
	def __init__(self,w,h,p):
		pygame.sprite.Sprite.__init__(self)
		#apariencia del mapa
		self.image=pygame.Surface([w,h])
		self.rect=self.image.get_rect()
		self.rect.x=p[0]
		self.rect.y=p[1]
class level(object):
	wall=None
	enemies_list=None
	object_list=None
	plataform_list=None

	background=pygame.image.load("background.png")
	struct=pygame.image.load('walls1.png')

	#muros que rodean el nivel
	mls=[[36,36*30,0,-height],[36*20,36,0,-height],[36,36*30,36*19,-height],[36*20,36,0,36*29]]
	
	def __init__(self):
		self.wall=pygame.sprite.Group()
		self.enemies_list=pygame.sprite.Group()
		self.object_list=pygame.sprite.Group()
		self.plataform_list=pygame.sprite.Group()
		for muro in self.mls:
			pared=walls(muro[0],muro[1],[muro[2],muro[3]])
			self.wall.add(pared)
	def update(self):
		self.enemies_list.update()
		self.object_list.update()
		self.plataform_list.update()

	def draw(self,window):
		window.fill(white)
		window.blit(self.background,(-504,-504))
		window.blit(self.struct,(0,-height))
		self.wall.draw(window)
		self.enemies_list.draw(window)
		self.object_list.draw(window)
		self.plataform_list.draw(window)
	

class level1(level):
	#muros level 1
	wll=[ [36*6, 36, 36*7 , height-108],
	      [36*5, 36, 0, height-36*6],
	      [36*2, 36, 36*9, height-36*6],
	      [36*5, 36, 36*15, height-36*6]
	    ]
	def __init__(self):
		level.__init__(self)
		for w in self.wll:
			plat=walls(w[0],w[1],[w[2],w[3]])
			self.wall.add(plat)
class Player(pygame.sprite.Sprite):
	level=None
	movx=0
	movy=0
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		#apariencia del jugador
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(imagen).convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=48
		self.rect.y=height-self.rect.height
	def update(self):
		self.rect.x+=self.movx		
		
		collition_ls=pygame.sprite.spritecollide(self,self.level.wall,False)
		for muro in collition_ls:
            		if self.movx > 0:
				self.rect.right = muro.rect.left
			elif self.movx < 0:
				self.rect.left = muro.rect.right
if __name__ == '__main__':
	pygame.init()
	window=pygame.display.set_mode([width,height])
	pygame.display.set_caption("Stick tower")
	
	#jugador
	player=Player('player.png')

	#creando niveles
	level_list=[]
	level_list.append(level1())
	
	#nivel actual
	level_position=0
	actual_level=level_list[level_position]

	#nivel del jugador
	player.level=actual_level

	#listas
	active_ls=pygame.sprite.Group()
	active_ls.add(player)

	#dibujos
	actual_level.draw(window)
	active_ls.draw(window)

	end=False

	clock=pygame.time.Clock()
	
	pygame.key.set_repeat(10,100)
	while not end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end=True
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RIGHT:
					player.movx=6
				if event.key==pygame.K_LEFT:
					player.movx=-6

			elif event.type==pygame.KEYUP:
				if event.key==pygame.K_RIGHT:
					player.movx=0
				if event.key==pygame.K_LEFT:
					player.movx=0
		actual_level.update()
		active_ls.update()
		actual_level.draw(window)
		active_ls.draw(window)
		clock.tick(60)
		pygame.display.flip()			
					
