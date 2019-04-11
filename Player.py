import pygame
from User_UI import Menu
import numpy as np
import os

class Player:

    def __init__(self):

        self.saving = False
        self.section = [1, 0, 31, 33]
        self.character_info = {"health":100,"max_health":55}
        self.sectionb = 0
        self.speed = 3
        self.changex = 0
        self.changey = 0
        self.x = 0
        self.y = 0
        self.count = 0
        self.char_display = pygame.display.set_mode((942,567))
        self.menu = Menu(self,self.char_display)
        self.level = 5;
        self.attack = 0;
        self.defense = 0;
        self.determination = 0;
        self.charm = 0;
        self.intelligence = 0;


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
                        #print("yes")
                        hold = self.menu.Pause()
                        if  hold == 6:
                            self.saving = True
                            self.menu.dialog_box(["The Game as been Saved."])
                            
                            
                            

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



    def load_character(self, name):

        self.character_info = np.load("Saves/" + name + ".npy").item()
        self.x = self.character_info['Location'][0]
        self.y = self.character_info['Location'][1]
        #self.level = 5;
        #self.attack = 0;
        #self.defense = 0;
        #self.determination = 0;
        #self.charm = 0;
        #self.intelligence = 0;
        


    def save_character(self):

        self.character_info['Location'][0] = self.x
        self.character_info['Location'][1] = self.y 
        np.save("Saves/"+ self.character_info['Name'] + ".npy", self.character_info)

