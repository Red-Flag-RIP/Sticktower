import pygame
from pygame.locals import *
from player_class import *
from enemies_class import *
from plataform_class import *
from funciones import *
#colors
white=(255,255,255)
black=(0,0,0)
#global const

real_width=720
real_height=1080


width=36*20
height=540

pygame.init()

window=pygame.display.set_mode([width,height])

gameIcon = pygame.image.load('images/ico.png') 

pygame.display.set_icon(gameIcon)

class level(object):
	#move back
	move_y=0
	move_x=0
	player=None
	wall=None
	enemies_list=None
	object_list=None
	plataform_list=None
	line_list=None
	visible_objects=None

	#muros que rodean el nivel
	mls=[[36,36*30,0,-height],[36*20,36,0,-height],[36,36*30,36*19,-height],[36*20,36,0,36*29]]
	
	def __init__(self):
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
		self.visible_objects.update()
	
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
		for o in self.object_list:
			o.rect.y+=d
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
		[36*2,36*10+18,height-36*21-18]
		]
	saw_position=[  [36*16,height-36],
			[36*17-18,height-36*12],
			[36*4+18,height-36*19],
			[36*10+18,height-36*22]
		     ]
	plataform_position=[    [36*3,height-36*9], 
				[36*3,height-36*15]
			   ]
	
	sarrow= [       [36*19-25,height-36*4+18-3.5],
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
		roca=proyectil('images/rock.png',[36*3,-height+36*4+8])
		self.object_list.add(roca)
		escudo=shield('images/shield.png',[36*16,height-36])
		self.object_list.add(escudo)
		espada=sword('images/sword.png',[36*4,height-36*19])
		self.object_list.add(espada)
		vida=barra()
		self.visible_objects.add(vida)

class level2(level):
	wll=[   [36*3,36,36*9,height-36*3],
		[36*3,36,36*17,height-36],
		[36*3,36,0,height-36*5],
		[36*2,36,0,height-36*9],
		[36*7,36,36*13,height-36*9],
		[36*2,36,36*5,height-36*11],
		[36*2,36,36*10,height-36*13],
		[36*3,36,36*17,height-36*14],
		[36*2,36,36*10,height-36*16],
		[36*7,36,0,height-36*17],
		[36*18,36,36*2+5,height-36*20],
		[36*2,36,36*14,height-36*23],
		[36*2,36,36*5,height-36*24],
		[36*3,36,0,height-36*27],
		[36*6,36,36*14,height-36*27]
	    ]
	lpos=  [36*15,36+18,height-18]
		

	spos=  [36*16,height-36]
		
	apos=[  [36*19-25,height-36*2+18-3.5],
		[36*19-25,height-36*4+18-3.5],
		[36*19-25,height-36*10+18-3.5],
		[36*19-25,height-36*11+18-3.5],
		[36*19-25,height-36*12+18-3.5],
		[36*19-25,height-36*18+18-3.5]]
	gpos=[  [36,height-36*8],
		[36,height-36*16]]
	
	fpos=[  [36,height-36*6+18],[36+18,height-36*6+18],
		[36*16,height-36*10+18],[36*16+18,height-36*10+18]
		]

	def __init__(self):
		level.__init__(self)

		for w in self.wll:
			plat=walls(w[0],w[1],[w[2],w[3]])
			self.wall.add(plat)
		road=moving_line(self.lpos[0],[self.lpos[1],self.lpos[2]])
		self.line_list.add(road)
		sierra=saw(self.spos)
		sierra.level=self
		self.enemies_list.add(sierra)
		for a in self.apos:
			flecha=arrow(a)
			flecha.level=self
			self.enemies_list.add(flecha)
		for p in self.apos:
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
		vida=barra()
		self.visible_objects.add(vida)
		boss=boss2()
		self.enemies_list.add(boss)
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
	E_door=pygame.image.load('images/doorclosed.png')
	E_door_pos=[54,height-51]
	S_door=pygame.image.load('images/dooropen.png')
	S_door_pos=[width-36*4,-height+36*2-14]
	screen=pygame.image.load('images/Screen.png')
	explosion=pygame.image.load('images/explosion.png')
	m_ex=0
	pygame.display.set_caption("Stick tower")

	#VARIABLE D QUE ME DEFINE LA VELOCIDAD DE CAMBIO DEL FONDO
	d=0
	reach_bottom=0
	#jugador
	player=Player()
	#player=Player([36,36])

	#FONDO
	back=background('images/nivel1map.png')

	#enemigos
	blevel1=boss1()
	bossls=pygame.sprite.Group()
	bossls.add(blevel1)
	#balas
	ls_balas_nivel1=pygame.sprite.Group()
	for b in bpos:
		ls_balas_nivel1.add(gbala(b,[b[0]+width,b[1]+36*12]))
	
	boss_b=gbala([36*11-18-10,height-36*28],[0,height-36*20])
	boss_b.direccion=1
	ls_balas_nivel1.add(boss_b)
	#creando niveles
	level_list=[]
	level_list.append(level1())
	level_list.append(level2())
	#nivel actual
	level_position=0
	actual_level=level_list[level_position]

	#nivel del jugador
	actual_level.player=player
	for obj in actual_level.object_list:
		obj.player=player
	for v in actual_level.visible_objects:
		v.player=player
	player.level=actual_level
	blevel1.level=actual_level
	#listas
	active_ls=pygame.sprite.Group()
	active_ls.add(back)
	active_ls.add(player)
	active_ls.add(blevel1)
	

	#dibujos
	window.blit(E_door,E_door_pos)
	window.blit(S_door,S_door_pos)
	active_ls.draw(window)
	window.blit(player.image,(player.rect.x,player.rect.y))
	actual_level.draw(window)
	ls_balas_nivel1.draw(window)


	#Menu de pausa
	continuar=button([36*10,36*3],[width/4,height/8])
	menu=button([36*6,36*3],[width/3+18,3*height/8])
	tcontinuar=fuente.render("CONTINUAR.", True, white)
	tmenu=fuente.render("SALIR.", True, white)	
	
	speed=4
	
	fuente = pygame.font.Font(None, 36) 
	con_cuadros = 0
	tasa_cambio = 60
	tiempo_ini = 10
	seglim=0

	pause=False
	end_level=False
	end=False
	clock=pygame.time.Clock()
	pygame.key.set_repeat(10,50)

	
	while not end_level:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RIGHT:
					player.movx=speed
				if event.key==pygame.K_LEFT:
					player.movx=-speed
				if event.key==pygame.K_SPACE:
					player.jump()
				if event.key==pygame.K_UP:
					player.climb()
				if event.key==pygame.K_z:
					for obj in actual_level.object_list:
						if obj.grab==1:
							obj.disparo=1
			elif event.type==pygame.KEYUP:
				if event.key==pygame.K_RIGHT:
					player.movx=0
				if event.key==pygame.K_LEFT:
					player.movx=0
				if event.key == pygame.K_ESCAPE:
						pause=True
				if event.key == pygame.K_l:
						end_level=True
			
		#reloj

		total_segundos = con_cuadros // tasa_cambio
		minutos = total_segundos // 60
		segundos = total_segundos % 60
		tiempo_final = "Tiempo: {0:02}:{1:02}".format(minutos, segundos)
		texto = fuente.render(tiempo_final, True, black)
		con_cuadros += 1
	
		#MOVER OBJETOS CON EL FONDO
		if player.rect.y <= height/8:                              
			d=6
			reach_bottom=1
			player.rect.y+=d
			actual_level.move_back_y(d)
			back.rect.y+=d
			blevel1.rect.y+=d
			for b in ls_balas_nivel1:
				b.d=d
			boss_b.d=d
		else:
			d=0
		
		#interactuar con el hp del jugador
		if player.hp<=0:
			window.blit(screen,[-10,-10])
			dead()

		
		#Muere si toca el fondo	
		if player.rect.y == height-player.rect.height and reach_bottom!=0:
			player.hp=0	

		balas_collition=pygame.sprite.spritecollide(player,ls_balas_nivel1,False)
		for bala in balas_collition:
			if bala.direccion==0:
				if player.objeto <=1:
					player.hp-=20
					bala.rect.x=bala.pi[0]
					bala.rect.y=bala.pi[1]
			if bala.direccion==1:
				if player.objeto <=1:
					player.hp=0
					player.exp=1
					bala.rect.x=bala.pi[0]
					bala.rect.y=bala.pi[1]
		collide_boss=pygame.sprite.spritecollide(player,bossls,False)
		for boss in collide_boss:
			if player.objeto!=3:
				player.hp-=0
			
		for w in actual_level.plataform_list:
			w.player=player
		if blevel1.dead==1:
			ls_balas_nivel1.remove(boss_b)
			active_ls.remove(blevel1)

		if pause:
			  
			window.blit(continuar.image,[continuar.rect.x,continuar.rect.y])
			window.blit(menu.image,[menu.rect.x,menu.rect.y])
			window.blit(tcontinuar,[width/3+46,height/8+36])
			window.blit(tmenu,[width/3+36*2+18,3*height/8+36])
			while pause:
      				for event in pygame.event.get():

          				if event.type == pygame.QUIT:
              					pygame.quit()
					if event.type == pygame.KEYUP:
						if event.key == pygame.K_ESCAPE:
							pause=False
				window.fill(gray)
				mouse=pygame.mouse.get_pos()
				continuar.mposx=mouse[0]
				continuar.mposy=mouse[1]
				menu.mposx=mouse[0]
				menu.mposy=mouse[1]
				continuar.update()
				menu.update()
				window.blit(continuar.image,[continuar.rect.x,continuar.rect.y])
				window.blit(menu.image,[menu.rect.x,menu.rect.y])
				window.blit(tcontinuar,[width/3+46,height/8+36])
				window.blit(tmenu,[width/3+36*2+18,3*height/8+36])
        			clock.tick(60)
				
				pygame.display.flip()

		if player.rect.x>=width-36*4 and player.rect.x<=width-36*3 and player.rect.y>=36*1 and player.rect.y<=36*3 and blevel1.dead==1:
			end_level=True

		actual_level.update()
		active_ls.update()
		ls_balas_nivel1.update()
		active_ls.draw(window)
		actual_level.draw(window)
		E_door_pos[1]+=d
		S_door_pos[1]+=d
		window.blit(E_door,E_door_pos)
		window.blit(S_door,S_door_pos)
		ls_balas_nivel1.draw(window)
		window.blit(player.image,(player.rect.x,player.rect.y))
		window.blit(boss_b.image,(boss_b.rect.x,boss_b.rect.y))
		window.blit(texto, [10, 10])
		clock.tick(60)
		pygame.display.flip()
	
	end_level=False
	#Inicia un nuevo nivel
	d=0
	player.rect.x=48
	player.rect.y=height-player.rect.height
	bpos= [ [36,height-36*8],
		[36,height-36*16]
	      ]
	
	S_door_pos=[width-36*4,-height+36*2-14]
	S_door=pygame.image.load('images/doorclosed.png')

	ls_balas_nivel2=pygame.sprite.Group()
	for b in bpos:
		ls_balas_nivel2.add(gbala(b,[b[0]+width,b[1]+36*12]))
	player.hp=100
	active_ls.empty()
	reach_bottom=0
	back=background('images/nivel2map.png')
	level_position=1
	actual_level=level_list[level_position]

	#nivel del jugador
	actual_level.player=player
	for obj in actual_level.object_list:
		obj.player=player
	for v in actual_level.visible_objects:
		v.player=player
	for e in actual_level.enemies_list:
		e.player=player
	player.level=actual_level
	active_ls.add(back)
	active_ls.add(player)

	window.blit(E_door,E_door_pos)
	window.blit(S_door,S_door_pos)
	active_ls.draw(window)
	ls_balas_nivel2.draw(window)
	window.blit(player.image,(player.rect.x,player.rect.y))
	actual_level.draw(window)


	while not end_level:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RIGHT:
					player.movx=speed
				if event.key==pygame.K_LEFT:
					player.movx=-speed
				if event.key==pygame.K_SPACE:
					player.jump()
				if event.key==pygame.K_UP:
					player.climb()
				if event.key==pygame.K_z:
					for obj in actual_level.object_list:
						if obj.grab==1:
							obj.disparo=1
			elif event.type==pygame.KEYUP:
				if event.key==pygame.K_RIGHT:
					player.movx=0
				if event.key==pygame.K_LEFT:
					player.movx=0
				if event.key == pygame.K_ESCAPE:
						pause=True
	
		#MOVER OBJETOS CON EL FONDO
		if player.rect.y <= height/8:                              
			d=6
			player.rect.y+=d
			actual_level.move_back_y(d)
			back.rect.y+=d
			for b in ls_balas_nivel2:
				b.d=d
		else:
			d=0

		balas_collition=pygame.sprite.spritecollide(player,ls_balas_nivel2,False)
		for bala in balas_collition:
			if bala.direccion==0:
				if player.objeto <=1:
					player.hp-=20
					bala.rect.x=bala.pi[0]
					bala.rect.y=bala.pi[1]

		#interactuar con el hp del jugador
		if player.hp<=0:
			window.blit(screen,[-10,-10])
			dead()
		
		#Muere si toca el fondo	
		if player.rect.y == height-player.rect.height and reach_bottom!=0:
			player.hp=0		
				
		if pause:		  
			window.blit(continuar.image,[continuar.rect.x,continuar.rect.y])
			window.blit(menu.image,[menu.rect.x,menu.rect.y])
			window.blit(tcontinuar,[width/3+46,height/8+36])
			window.blit(tmenu,[width/3+36*2+18,3*height/8+36])
			while pause:
				for event in pygame.event.get():
	       				if event.type == pygame.QUIT:
	       					pygame.quit()
					if event.type == pygame.KEYUP:
						if event.key == pygame.K_ESCAPE:
							pause=False
				window.fill(gray)
				mouse=pygame.mouse.get_pos()
				continuar.mposx=mouse[0]
				continuar.mposy=mouse[1]
				menu.mposx=mouse[0]
				menu.mposy=mouse[1]
				continuar.update()
				menu.update()
				window.blit(continuar.image,[continuar.rect.x,continuar.rect.y])
				window.blit(menu.image,[menu.rect.x,menu.rect.y])
				window.blit(tcontinuar,[width/3+46,height/8+36])
				window.blit(tmenu,[width/3+36*2+18,3*height/8+36])
				clock.tick(60)
			
				pygame.display.flip()

		total_segundos = con_cuadros // tasa_cambio
		minutos = total_segundos // 60
		segundos = total_segundos % 60
		tiempo_final = "Tiempo: {0:02}:{1:02}".format(minutos, segundos)
		texto = fuente.render(tiempo_final, True, black)
		con_cuadros += 1

		actual_level.update()
		active_ls.update()
		ls_balas_nivel2.update()
		active_ls.draw(window)
		actual_level.draw(window)
		E_door_pos[1]+=d
		S_door_pos[1]+=d
		window.blit(E_door,E_door_pos)
		window.blit(S_door,S_door_pos)
		ls_balas_nivel2.draw(window)
		window.blit(player.image,(player.rect.x,player.rect.y))
		window.blit(texto, [10, 10])
		clock.tick(60)
		pygame.display.flip()
