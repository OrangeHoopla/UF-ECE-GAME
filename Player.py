import pygame

import os

class Player:

    def __init__(self):
        self.section = [1, 0, 31, 33]
        self.sectionb = 0
        self.speed = 3
        self.changex = 0
        self.changey = 0
        self.health = 4
        self.x = 0
        self.y = 0
        self.count = 0

        self.image = pygame.image.load(
            os.path.join(
                'graphics',
                'red.png'))

        self.skills = {'Procrastination' : -1 , 'Nothing' : 0}


    def move(self):
        #handles key board events and cycles through image to give
        #animation feel
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

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

