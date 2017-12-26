import os
import pygame
import time
from time import sleep
import glob
from Player import Player

pygame.init()

background = pygame.image.load(os.path.join('Maps','town.png'))
background = pygame.transform.scale(background,(942,567))
size =  background.get_size()


gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('ECEmon version 2.0')
clock = pygame.time.Clock()


class Game:

	def __init__(self):

		player = Player()
		#insert loading screen basics

		while True:


			player.move()

			#updates

			gameDisplay.blit(background,(0,0))
			gameDisplay.blit(player.image,(player.x,player.y))

			pygame.display.update()

			clock.tick(30)


	

    





if __name__ == "__main__":
	Game()



