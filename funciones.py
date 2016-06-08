import pygame
from game import *


clock=pygame.time.Clock()
def paused(pause):

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
         

        pygame.display.update()
        clock.tick(15)  

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
