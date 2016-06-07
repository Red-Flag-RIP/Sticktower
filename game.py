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
	line_list=None
	visible_objects=None

	#muros que rodean el nivel
	mls=[[36,36*30,0,-height],[36*20,36,0,-height],[36,36*30,36*19,-height],[36*20,36,0,36*29]]
	
	def __init__(self):
		self.image=pygame.image.load("images/nivel1map.png")
		self.rect=self.image.get_rect()
		self.rect.x=0
		self.rect.y=-height
		self.wall=pygame.sprite.Group()
		self.enemies_list=pygame.sprite.Group()
		self.object_list=pygame.sprite.Group()
		self.plataform_list=pygame.sprite.Group()
		self.line_list=pygame.sprite.Group()
		self.visible_objects=pygame.sprite.Group()
		for muro in self.mls:
			pared=walls(muro[0],muro[1],[muro[2],muro[3]])
			self.wall.add(pared)
	def update(self):
		self.enemies_list.update()
		self.object_list.update()
		self.plataform_list.update()
		self.line_list.update()
	
	def move_back_y(self,d):
		self.move_y=d
		for w in self.wall:
			w.rect.y+=d
		for l in self.plataform_list:
			l.rect.y+=d
		for e in self.enemies_list:
			e.rect.y+=d
		for g in self.line_list:
			g.rect.y+=d
		self.move_y=0
		for b in self.visible_objects:
			b.rect.y+=d
	def draw(self,window):
		#window.fill(white)
		#self.wall.draw(window)
		self.enemies_list.draw(window)
		self.object_list.draw(window)
		self.line_list.draw(window)
		self.plataform_list.draw(window)
		self.visible_objects.draw(window)
		
	
		
	

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
		[36*17,36+18,height-36*8-18],
		[36*3,36*16,height-36*11-18],
		[36*17,36+18,height-36*14-18],
		[36*1,36*5,height-36*18-18],
		[36*3,36*10+18,height-36*21-18]
		]
	saw_position=[  [36*16,height-36],
			[36*17-18,height-36*12],
			[36*4+18,height-36*19],
			[36*10+18,height-36*22]
		     ]
	plataform_position=[    [36*3,height-36*9], 
				[36*3,height-36*15]
			   ]
	
	sarrow= [       [36*19-25,height-36+18-3.5],
			[36*19-25,height-36*4+18-3.5],
			[36*19-25,height-36*25+18-3.5]
		]

	gpos= [ [36,height-36*11],
		[36,height-36*24]
	      ]
	
	fpos= [ [36*4,height-36*7+18],[36*4+18,height-36*7+18],
		[36*17,height-36*7+18],[36*17+18,height-36*7+18],
		[36*3,height-36*13+18],[36*3+18,height-36*13+18],
		[36*15,height-36*18+18],[36*15+18,height-36*18+18]
	      ]
	
		
			
	def __init__(self):
		level.__init__(self)
		
		for w in self.wll:
			plat=walls(w[0],w[1],[w[2],w[3]])
			self.wall.add(plat)
		
		for r in self.lines:
			road=moving_line(r[0],[r[1],r[2]])
			self.line_list.add(road)
		for w in self.saw_position:
			sierra=saw(w)
			sierra.level=self
			self.enemies_list.add(sierra)
		for w in self.plataform_position:
			moving=plataform(w)
			moving.level=self
			self.plataform_list.add(moving)
		for a in self.sarrow:
			flecha=arrow(a)
			flecha.level=self
			self.enemies_list.add(flecha)
		for p in self.sarrow:
			base=visible([p[0]+25,p[1]-18+3.5])
			self.visible_objects.add(base)
		for g in self.gpos:
			guard=guardian(g)
			guard.level=self
			self.enemies_list.add(guard)
		for f in self.fpos:
			flame=fire(f)
			flame.level=self
			self.enemies_list.add(flame)
		

class background(pygame.sprite.Sprite):
	def __init__(self,imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(imagen).convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=0
		self.rect.y=-height


if __name__ == '__main__':
	bpos= [ [36,height-36*11],
		[36,height-36*24]
	      ]

	pygame.init()
	pygame.display.set_caption("Stick tower")

	#VARIABLE D QUE ME DEFINE LA VELOCIDAD DE CAMBIO DEL FONDO
	d=0
	
	#jugador
	player=Player()
	#player=Player([36,36])

	#FONDO
	back=background('images/nivel1map.png')

	#enemigos
	blevel1=boss1()

	#balas
	ls_balas_nivel1=pygame.sprite.Group()
	for b in bpos:
		ls_balas_nivel1.add(gbala(b,[b[0]+width,b[1]+36*12]))
	
	boss_b=boss_bala()
	ls_balas_nivel1.add(boss_b)
	boss_b.pindex=[0,-582]
	#creando niveles
	level_list=[]
	level_list.append(level1())
	
	#nivel actual
	level_position=0
	actual_level=level_list[level_position]

	#nivel del jugador
	player.level=actual_level
	blevel1.level=actual_level
	#listas
	active_ls=pygame.sprite.Group()
	active_ls.add(back)
	active_ls.add(player)
	active_ls.add(blevel1)
	

	#dibujos
	active_ls.draw(window)
	window.blit(player.image,(player.rect.x,player.rect.y))
	actual_level.draw(window)
	ls_balas_nivel1.draw(window)
	
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
	
		#MOVER OBJETOS CON EL FONDO
		if player.rect.y <= height/8:
			d=6
			player.rect.y+=d
			actual_level.move_back_y(d)
			back.rect.y+=d
			blevel1.rect.y+=d
			boss_b.rect.y+=d
			for b in ls_balas_nivel1:
				b.d=d
		#bala del jefe persigue	


		
		#Muere si toca el fondo	
		if player.rect.y == height-player.rect.height and d!=0:
			print 'You lose'	
		
		actual_level.update()
		active_ls.update()
		ls_balas_nivel1.update()
		active_ls.draw(window)
		actual_level.draw(window)
		ls_balas_nivel1.draw(window)
		window.blit(player.image,(player.rect.x,player.rect.y))
		clock.tick(60)
		pygame.display.flip()			
					
