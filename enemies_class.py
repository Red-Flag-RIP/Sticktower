import pygame
from game import *
from player_class import *

width=36*20
height=540

class saw(pygame.sprite.Sprite):
	level=None
	d=-2
	contador=0
	def __init__(self,p):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/saw.png')
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
			self.image=pygame.image.load('images/saw.png')
			self.contador+=1
		if self.contador >=20 and self.contador<=40:
			self.image=pygame.image.load('images/saw2.png')
			self.contador+=1
		if self.contador==40:
			self.contador=0

class arrow(pygame.sprite.Sprite):
	level=None
	d=-4
	def __init__(self,p):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/arrow_right.png')
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
	def __init__(self,p):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/guardian.png')
		self.rect=self.image.get_rect()
		self.rect.x=p[0]
		self.rect.y=p[1]
class fire(pygame.sprite.Sprite):
	level=None
	contador=0
	itr=7
	def __init__(self,p):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/flames1.png')
		self.rect=self.image.get_rect()
		self.rect.x=p[0]
		self.rect.y=p[1]
	def update(self):
		if self.contador<self.itr:
				self.image=pygame.image.load('images/flames2.png').convert_alpha()
				self.contador+=1
		if self.contador>=self.itr and self.contador <=self.itr*2:
				self.image=pygame.image.load('images/flames3.png').convert_alpha()
				self.contador+=1
		if self.contador>=self.itr*2 and self.contador <=self.itr*3:
				self.image=pygame.image.load('images/flames4.png').convert_alpha()
				self.contador+=1
		if self.contador==self.itr*3: 
				self.image=pygame.image.load('images/flames1.png').convert_alpha()
				self.contador=0

class boss1(pygame.sprite.Sprite):
	level=None
	contador=0
	moving=0
	shot=False
	recarga=60
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/jefe1.png')
		self.rect=self.image.get_rect()
		self.rect.x=36*11
		self.rect.y=-582+36*3
		self.pi=[self.rect.x,self.rect.y]
	def update(self):
		if self.recarga>0 and self.rect.x==self.pi[0]:
			self.shot=True
			self.recarga-=1
		if self.recarga<=0:
			self.rect.x+=2.5
		if self.rect.x>=self.pi[0]+36*4:
			self.recarga+=1
		if self.recarga==60:
			self.rect.x-=2.5
			
			

def brensenham_bala(p1,p2,c):
	xi=p1[0]
	xf=p2[0]
	yi=p1[1]
	yf=p2[1]
	dx=xf-xi
	dy=yf-yi
	x=xi
	y=yi
	i=0
	sp=0.05
	if (dy < 0): 
  		dy=-dy; 
   		stepy=-sp
  	else:
	        stepy=sp
 	if (dx < 0):  
		dx=-dx 
        	stepx=-sp
  	else:
    		stepx =sp
	if dx>=dy:
		p=2*dy-dx
		dE=2*dy
		dNE=2*(dy-dx)
		while i!=c:
			x+=stepx
			i=i+1
			if p<0:
				p+=dE
			else:
				y+=stepy
				p+=dNE
	else:
		p=2*dx-dy
		dE=2*dx
		dNE=2*(dx-dy)
		while i!=c:
			y+=stepy
			i=i+1
			if p<=0:
				p+=dE
			else:
				x+=stepx
				p+=dNE
	return (x,y)

class gbala(pygame.sprite.Sprite):
	level=None
	p1=[]
	p2=[]
	contador=0
	d=0
	def __init__(self,posa,posb):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/g_bala.png')
		self.rect=self.image.get_rect()	
		self.rect.x=posa[0]+18
		self.rect.y=posa[1]+15
		self.pi=[posa[0]+18,posa[1]+15]
		self.pf=[posb[0],posb[1]]
	
	def update(self):
		if self.rect.x<=width:
			self.p1=[self.rect.x,self.rect.y+self.d]
			self.pf[1]+=self.d
			self.pi[1]+=self.d
			self.p2=[self.pf[0],self.pf[1]]
			np=brensenham_bala(self.p1,self.p2,self.contador)
			self.rect.x=np[0]
			self.rect.y=np[1]
			self.contador+=1
			self.d=0
		else:
			self.contador=0
			self.rect.x=self.pi[0]
			self.rect.y=self.pi[1]+self.d
			self.d=0

class boss_bala(pygame.sprite.Sprite):
	contador=0
	pindex=[]
	cambio=0
	shot=0
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('images/bbala.png')
		self.rect=self.image.get_rect()
		self.rect.x=36*10+18
		self.rect.y=-582+36*3+18
	
	def update(self):
		if self.rect.x>=width/2-36:
			self.rect.x-=2
			self.shot+=1
		else:
			self.cambio=1
		if self.cambio==1:
			self.pindex=[0,36*8]
			np=brensenham_bala([self.rect.x,self.rect.y],self.pindex,self.contador)
			self.rect.x=np[0]
			self.rect.y=np[1]
			self.shot+=1
			self.cambio=2
		if self.cambio==2:
			self.pindex=[36*10,height]
			np=brensenham_bala([self.rect.x,self.rect.y],self.pindex,self.contador)
			self.rect.x=np[0]
			self.rect.y=np[1]			
			self.shot+=1
			self.cambio=3
		if self.cambio==3:
			self.pindex=[0,36*3]
			np=brensenham_bala([self.rect.x,self.rect.y],self.pindex,self.contador)
			self.rect.x=np[0]
			self.rect.y=np[1]			
			self.shot+=1
			self.cambio=0
		if self.shot>=200:
			self.rect.x=36*10+18
			self.shot=0
		


		
