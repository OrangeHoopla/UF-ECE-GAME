import pygame
from time import sleep
import os

class Player:

    def __init__(self):
        self.changex = 0
        self.changey = 0
        self.health = 4
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(os.path.join('graphics','red.png'))

        self.skills = {'Procrastination' : -1 , 'Nothing' : 0}


    def move(self):

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.changex = -3
                        
                    elif event.key == pygame.K_RIGHT:
                        self.changex = 3

                    elif event.key == pygame.K_UP:
                        self.changey = -3

                    elif event.key == pygame.K_DOWN:
                        self.changey = 3
                else:
                    self.changey = 0
                    self.changex = 0
        

        self.x += self.changex
        self.y += self.changey

