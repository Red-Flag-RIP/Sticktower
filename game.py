import pygame
from pygame.locals import *
from player_class import *
from enemies_class import *
from plataform_class import *

#colors
white=(255,255,255)

#global const

real_width=720
real_height=1080


width=36*20
height=540

window=pygame.display.set_mode([width,height])



class level(object):
	#move back
	move_y=0
	move_x=0
	
	wall=None
	enemies_list=None
	object_list=None
	plataform_list=None


	#muros que rodean el nivel
	mls=[[36,36*30,0,-height],[36*20,36,0,-height],[36,36*30,36*19,-height],[36*20,36,0,36*29]]
	
	def __init__(self):
		self.image=pygame.image.load("nivel1map.png")
		self.rect=self.image.get_rect()
		self.rect.x=0
		self.rect.y=-height
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
	
	def move_back_y(self,d):
		self.move_y=d
		for w in self.wall:
			w.rect.y+=d
		self.move_y=0

	def draw(self,window):
		#window.fill(white)
		self.wall.draw(window)
		self.enemies_list.draw(window)
		self.object_list.draw(window)
		self.plataform_list.draw(window)
	
		
	

class level1(level):
	#muros level 1
	wll=[ [36*6, 36, 36*7 , height-108],
	      [36*5, 36, 0, height-36*6],
	      [36*2, 36, 36*9, height-36*6],
	      [36*5, 36, 36*15, height-36*6],
	      [36*4, 36, 36*16, height-36*11],
	      [36*6, 36, 0, height-36*12],
	      [36*7, 36, 36*13, height-36*17],
	      [36*2, 36, 36*4, height-36*18],
	      [36, 36, 36*3, height-36*21],
	      [36*4, 36, 36*10, height-36*21],
	      [36*5, 36, 36*5, height-36*24],
	      [36*5, 36, 0, height-36*25],
	      [36*10, 36, 36*10, height-36*27]
	    ]
	lines=[ [36*17,36+18,height-18],
		[36*17,36+18,height-36*8] 
		]
	saw_position=[36*16,height-36/2]
	def __init__(self):
		level.__init__(self)
		
		for w in self.wll:
			plat=walls(w[0],w[1],[w[2],w[3]])
			self.wall.add(plat)
		
		for r in self.lines:
			road=moving_line(r[0],[r[1],r[2]])
			self.plataform_list.add(road)

		#for w in self.saw_position:
		sierra=saw(self.saw_position,[36+18,height-18],[(36*20)-36-18,height-18])
		self.enemies_list.add(sierra)
		

class background(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(imagen).convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=0
		self.rect.y=-height


if __name__ == '__main__':
	pygame.init()
	pygame.display.set_caption("Stick tower")

	#VARIABLE D QUE ME DEFINE LA VELOCIDAD DE CAMBIO DEL FONDO
	d=0
	
	#jugador
	player=Player()
	#player=Player([36,36])

	#FONDO
	back=background('nivel1map.png')

	#enemigos
	

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
	active_ls.add(back)
	active_ls.add(player)

	#dibujos
	active_ls.draw(window)
	actual_level.draw(window)
	
	speed=4

	end=False

	clock=pygame.time.Clock()
	pygame.key.set_repeat(10,50)
	while not end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end=True
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RIGHT:
					player.movx=speed
				if event.key==pygame.K_LEFT:
					player.movx=-speed
				if event.key==pygame.K_SPACE:
					player.jump()


			elif event.type==pygame.KEYUP:
				if event.key==pygame.K_RIGHT:
					player.movx=0
				if event.key==pygame.K_LEFT:
					player.movx=0
	
		if player.rect.y <= height/8:
			d=6
			player.rect.y+=d
			actual_level.move_back_y(d)
			back.rect.y+=d
		if player.rect.y == height-player.rect.height and d!=0:
			print 'You lose'	
		
		actual_level.update()
		active_ls.update()
		active_ls.draw(window)
		actual_level.draw(window)
		clock.tick(60)
		pygame.display.flip()			
					
