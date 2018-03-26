import pygame
from User_UI import Menu

import os

class Player:

    def __init__(self):
        self.menu = Menu()
        self.section = [1, 0, 31, 33]
        self.sectionb = 0
        self.speed = 3
        self.changex = 0
        self.changey = 0
        self.health = 4
        self.x = 0
        self.y = 0
        self.count = 0
        self.char_display = pygame.display.set_mode((942,567))

        self.image = pygame.image.load(
            os.path.join(
                'graphics',
                'red.png'))

        self.skills = {'Procrastination' : -1 , 'Nothing' : 0}


    def move(self):

        self.char_display.blit(self.image,
                            (self.x,
                             self.y),
                             self.section)
        
        #handles key board events and cycles through image to give
        #animation feel
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #moving the character
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:

                        self.changex = -self.speed
                        self.section = [1, 33, 33, 30]
                        self.count += 1
                        
                    elif event.key == pygame.K_RIGHT:

                        self.changex = self.speed
                        self.section = [1, 64, 33, 32]
                        self.count += 1

                    elif event.key == pygame.K_UP:

                        self.changey = -self.speed
                        self.section = [1, 96, 31, 33]
                        self.count += 1

                    elif event.key == pygame.K_DOWN:

                        self.changey = self.speed
                        self.section = [1, 0, 31, 33]
                        self.count += 1
                    #access the menu 
                    elif event.key == pygame.K_q:
                        print("yes")
                        self.menu.Pause()
                else:
                    self.changey = 0
                    self.changex = 0
                    self.count = 0
                    self.sectionb = 0
        

        self.x += self.changex
        self.y += self.changey
        self.sectionb += self.count
        self.section[0] = 33*int(self.sectionb/5)
        self.sectionb = self.sectionb%19

