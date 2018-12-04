import pygame
import os
from time import sleep

class Battles():

    def __init__(self,player,enemy):
        self.uidisplay = pygame.display.set_mode((942,567))
        self.background = pygame.image.load(os.path.join('graphics','Battle_scene2.png'))
        self.background = pygame.transform.scale(self.background,(942,567))
        self.enemy = pygame.image.load(os.path.join('graphics', enemy[0] + '.png'))


    def main(self,player,enemy):
        gameExit = False
        pygame.mixer.music.load(os.path.join(
            'sounds',
            'battle_music.mp3'))
        pygame.mixer.music.play(-1)

        RED = [255,0,0]
        GREEN = [0,255,0]
        BLACK = [0,0,0]
        GRAY = [169,169,169]

        x = 0
        y = 0
        fonts = pygame.font.Font("fonts/gen_1.ttf", 25)
        lv = pygame.font.Font("fonts/gen_1.ttf", 15)

        monitor = pygame.image.load('graphics/text_box2.png')
        monitor = pygame.transform.scale(monitor,(500,100))

        player_monitor = pygame.image.load('graphics/text_box2.png')
        player_monitor = pygame.transform.scale(monitor,(500,200))

        health = 3.56
        max_health = 4.00

        name = "Dr.Moore"
        num_health = "GPA {}/{}".format(health,max_health)
        disp_health = round(((health/max_health)*175),2)
        level = "Lv. {}".format(15)
        block = fonts.render(name, True, (0, 0, 0))
        block_level = lv.render(level, True, (0, 0, 0))
        block_health = lv.render(num_health, True, (0, 0, 0))



        self.uidisplay.blit(self.background,(0,0))
        pygame.display.update()
        self.character_intro()
        
        self.enemy_intro()













        while not gameExit:
            self.uidisplay.blit(self.background,(0,0))
            self.uidisplay.blit(self.character,(50,275))
            self.uidisplay.blit(self.enemy,(600,100))


            self.uidisplay.blit(monitor,(x,y))
            self.uidisplay.blit(block,(x+25,y+15))
            self.uidisplay.blit(block_level,(x+350,y+25))
            pygame.draw.rect(self.uidisplay, BLACK,(x+ 247, y+47, 181, 21))
            pygame.draw.rect(self.uidisplay, GRAY,(x+ 250, y+50, 175, 15))
            pygame.draw.rect(self.uidisplay, GREEN,(x+ 250, y+50, disp_health, 15))
            self.uidisplay.blit(block_health,(x+80,y+50))


            self.uidisplay.blit(player_monitor,(x + 450,y + 370))

            


            GREEN = [255-int(255*(health/max_health)),int(255*(health/max_health)),0]
            num_health = "GPA {}/{}".format(health,max_health)
            disp_health = int((health/max_health)*175)
            level = "Lv. {}".format(15)
            block = fonts.render(name, True, (0, 0, 0))
            block_level = lv.render(level, True, (0, 0, 0))
            block_health = lv.render(num_health, True, (0, 0, 0))



            pygame.display.update()
            


            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RETURN:
                            pygame.mixer.music.stop()
                            gameExit = True


    def character_intro(self):
        self.character = pygame.image.load(os.path.join('graphics','battle_you.png'))
        self.character = pygame.transform.scale(self.character,(300,300))
        for x in range (-150,50):
            self.uidisplay.blit(self.background,(0,0))
            self.uidisplay.blit(self.character,(x,275))
            pygame.display.update()
            #sleep(.00001)


    def enemy_intro(self):

        
        #self.character = pygame.transform.scale(self.character,(300,300))
        for x in range (750,600,-1):
            
            self.uidisplay.blit(self.background,(0,0))
            self.uidisplay.blit(self.character,(50,275))
            self.uidisplay.blit(self.enemy,(x,100))
            pygame.display.update()
            

