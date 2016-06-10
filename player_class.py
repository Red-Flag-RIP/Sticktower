import pygame
from game import *
from funciones import *

class Player(pygame.sprite.Sprite):
	image=None
	level=None
	objeto=0
	movx=0
	movy=0
	contador=-1
	itr=7
	hp=100
	direccion=0
	down=1
	disparo=0
	exp=0
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
			self.direccion=0
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
			if self.contador>=self.itr*6 and self.contador<=self.itr*7:
				self.image=pygame.image.load('images/player_run_right1.png').convert_alpha()
				self.contador+=1
			if self.contador==self.itr*7:
				self.contador=0
		if self.movx==0:
			self.contador=0
			if self.direccion==0:
				self.image=pygame.image.load('images/player_startright.png').convert_alpha()
			if self.direccion==1:
				self.image=pygame.image.load('images/player_startleft.png').convert_alpha()
		if self.movx < 0:
			self.direccion=1
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
			if self.direccion==0:
				self.image=pygame.image.load('images/player_startright.png').convert_alpha()
			if self.direccion==1:
				self.image=pygame.image.load('images/player_startleft.png').convert_alpha()

			
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
			self.movy = -10

		#plataforma en movimiento
		if len(coll_movls) > 0 or self.rect.bottom >= height:
			self.movy = -10
	def climb(self):
		self.rect.y += 2
		collition_ls=pygame.sprite.spritecollide(self,self.level.wall,False)
		coll_movls=pygame.sprite.spritecollide(self,self.level.plataform_list,False)
		self.rect.y -= 2
        
		# Si es posible saltar, aumentamos velocidad hacia arriba
		if len(collition_ls) > 0 or self.rect.bottom >= height:
			self.movy = -6

		#plataforma en movimiento
		if len(coll_movls) > 0 or self.rect.bottom >= height:
			self.movy = -6
	
	def objects(self):
		if self.objeto.tipe==1:
			if self.disparo==1:
				self.objeto.disparo=1

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
	
		enemies_collition=pygame.sprite.spritecollide(self,self.level.enemies_list,False)
		for enemy in enemies_collition:
			if enemy.tipe==1:
				if self.objeto != 3:
					self.hp=0
					self.image=pygame.image.load('images/dead_tipe1.png')
					self.rect.x=self.rect.x+18
					self.rect.y=self.rect.y+18
			if enemy.tipe==2:
				if self.objeto <=1:
					self.hp=0
					self.image=pygame.image.load('images/dead_tipe2.png')
					self.rect.x=self.rect.x+30
					self.rect.y=self.rect.y-7
			if enemy.tipe==3:
				if self.objeto != 3:
					self.hp=0
					self.image=pygame.image.load('images/dead_tipe3.png')
			if enemy.tipe==4:
				self.hp-=3
			if enemy.tipe==10:
				self.hp=0
				self.image=pygame.image.load('images/dead_tipe2.png')
		
		grab_object=pygame.sprite.spritecollide(self,self.level.object_list,False)
		for obj in grab_object:
			obj.grab=1	
			self.objeto=obj.tipe
			if self.direccion==1:
				obj.direccion==1	
			if obj.tipe==3:
				self.hp=100
				self.level.object_list.remove(obj)
		if self.exp==1:
			
			self.image=pygame.image.load('images/explosion.png')
			

		
class proyectil(pygame.sprite.Sprite):
	player=None
	tipe=1
	def __init__(self, imagen,posa):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(imagen).convert_alpha()
		self.rect=self.image.get_rect()
		self.direccion=0	
		self.rect.x=posa[0]
		self.rect.y=posa[1]+15
		self.disparo=0
		self.grab=0
	def update(self):
		if self.disparo==1:
			if self.grab==1:
				self.rect.x=self.player.rect.x+33
				self.rect.y=self.player.rect.y+18
			self.rect.x+=5
			self.grab=0
			if self.rect.x>=width:
				self.grab=1
				self.disparo=0
		if self.grab==1:
			self.rect.x=-width
			
   
class shield(pygame.sprite.Sprite):
	player=None
	tipe=2    
	def __init__(self, imagen,posa):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(imagen).convert_alpha()
		self.rect=self.image.get_rect()
		self.direccion=0	
		self.rect.x=posa[0]
		self.rect.y=posa[1]+15
		self.grab=0
		self.disparo=0	
	def update(self):
		
		if self.grab==1:
			if self.direccion==0:
				self.rect.x=self.player.rect.x+23
				self.rect.y=self.player.rect.y+7
			if self.direccion==1:
				self.rect.x=self.player.rect.x-23
				self.rect.y=self.player.rect.y+7

class health(pygame.sprite.Sprite):
	player=None
	tipe=3
	def __init__(self, imagen,posa):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(imagen).convert_alpha()
		self.rect=self.image.get_rect()
		self.direccion=0	
		self.rect.x=posa[0]
		self.rect.y=posa[1]+15
		self.grab=0
		self.disparo=0	
	

class barra(pygame.sprite.Sprite):
	player=None
	boss=None
	b=0
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/barra1.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=54
		self.rect.y=height-46
	def update(self):
		if self.b==0:
			self.rect.x=self.player.rect.x+8
			self.rect.y=self.player.rect.y-9
			if self.player.hp>=95:
				self.image=pygame.image.load('images/barra1.png').convert_alpha()
			if self.player.hp>=80 and self.player.hp <=95:
				self.image=pygame.image.load('images/barra2.png').convert_alpha()
			if self.player.hp>=60 and self.player.hp <=80:
				self.image=pygame.image.load('images/barra3.png').convert_alpha()
			if self.player.hp>=40 and self.player.hp <=60:
				self.image=pygame.image.load('images/barra4.png').convert_alpha()
			if self.player.hp>=1 and self.player.hp <=40:
				self.image=pygame.image.load('images/barra5.png').convert_alpha()
			if self.player.hp<=0:
				self.image=pygame.image.load('images/barra6.png').convert_alpha()
		if self.b==1:
			self.rect.x=self.boss.rect.x+8
			self.rect.y=self.boss.rect.y-9
			if self.boss.hp>=95:
				self.image=pygame.image.load('images/barra1.png').convert_alpha()
			if self.boss.hp>=80 and self.boss.hp <=95:
				self.image=pygame.image.load('images/barra2.png').convert_alpha()
			if self.boss.hp>=60 and self.boss.hp <=80:
				self.image=pygame.image.load('images/barra3.png').convert_alpha()
			if self.boss.hp>=40 and self.boss.hp <=60:
				self.image=pygame.image.load('images/barra4.png').convert_alpha()
			if self.boss.hp>=1 and self.boss.hp <=40:
				self.image=pygame.image.load('images/barra5.png').convert_alpha()
			if self.boss.hp<=0:
				self.image=pygame.image.load('images/barra6.png').convert_alpha()
class gun(pygame.sprite.Sprite):
	direccion=0
	grab=0
	tipe=4
	player=None
	recarga=0
	disparo=0
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/gun.png')
		self.rect=self.image.get_rect()
		self.rect.x=36*2
		self.rect.y=height-36*28+26
	def update(self):
		if self.grab==1:
			self.rect.x=-width
			self.image=pygame.image.load('images/bala_player.png')
		if self.disparo==1 and self.recarga>0:
			if self.grab==1:
				self.rect.x=self.player.rect.x+33
				self.rect.y=self.player.rect.y+18
			self.rect.x+=5
			self.grab=0
			if self.rect.x>=width:
				self.grab=1
				self.disparo=0
		if self.grab==1:
			self.rect.x=-width
		

class ammo(pygame.sprite.Sprite):
	tipe=11
	direccion=0
	grab=0
	player=None
	gun=None
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/ammo.png')
		self.rect=self.image.get_rect()
		self.rect.x=36*18
		self.rect.y=height-36*21+24
	def update(self):
		if self.grab==1:
			self.rect.x=-width
			self.gun.recarga=10
