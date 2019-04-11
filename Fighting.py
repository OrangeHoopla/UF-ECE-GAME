import pygame
import os
from time import sleep
import json 


class Battles():

    def __init__(self,player,enemy):
        fp = open("Characters/me.txt")
        for i, line in enumerate(fp):
            if i == 1:
                me = line


        self.uidisplay = pygame.display.set_mode((942,567))
        self.background = pygame.image.load(os.path.join('graphics','Battle_scene2.png'))
        self.background = pygame.transform.scale(self.background,(942,567))
        self.enemy = json.loads(me)
        self.health = 4.00
        self.enemy_image = pygame.image.load(os.path.join('graphics',self.enemy["image"]))


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

        x = 92
        y = 50
        fonts = pygame.font.Font("fonts/gen_1.ttf", 15)
        lv = pygame.font.Font("fonts/gen_1.ttf", 15)

        monitor = pygame.image.load('graphics/text_box2.png')
        monitor = pygame.transform.scale(monitor,(500,100))

        player_monitor = pygame.image.load('graphics/text_box2.png')
        player_monitor = pygame.transform.scale(monitor,(400,150))

        
        health = 4.00
        max_health = 4.00

        
        num_health = "GPA {}/{}".format(health,max_health)
        disp_health = round(((health/max_health)*175),2)
        level = "Lv. {}".format(self.enemy["Level"])
        block = fonts.render(self.enemy["Name"], True, (0, 0, 0))
        block_level = lv.render(level, True, (0, 0, 0))
        block_health = lv.render(num_health, True, (0, 0, 0))



        self.uidisplay.blit(self.background,(0,0))
        pygame.display.update()
        self.character_intro()
        
        self.enemy_intro()

        one = fonts.render("Fight", True, (0, 0, 0))
        two = fonts.render("Run", True, (0, 0, 0))
        three = fonts.render("Debate", True, (0, 0, 0))
        four = fonts.render("Bag", True, (0, 0, 0))



        pos = 0
        tres = 0


        while not gameExit:
            self.uidisplay.blit(self.background,(0,0))
            self.uidisplay.blit(self.character,(50,275))
            self.uidisplay.blit(self.enemy_image,(600,100))


            self.uidisplay.blit(monitor,(x,y))
            self.uidisplay.blit(block,(x+25,y+15))
            self.uidisplay.blit(block_level,(x+350,y+25))
            pygame.draw.rect(self.uidisplay, BLACK,(x+ 247, y+47, 181, 21))
            pygame.draw.rect(self.uidisplay, GRAY,(x+ 250, y+50, 175, 15))
            pygame.draw.rect(self.uidisplay, GREEN,(x+ 250, y+50, disp_health, 15))
            self.uidisplay.blit(block_health,(x+80,y+50))


            self.uidisplay.blit(player_monitor,(x + 450,y + 370))

            #needs to be reviewed theres probably some not needed code in here
            if(self.health > 4): self.health = 4
            if(self.health <= 0): gameExit = True
            while(round(health,2) != round(self.health,2)):
                if(health > self.health):
                    health = health - 0.01
                else: health = health + 0.01
                GREEN = [255-int(255*(health/max_health)),int(255*(health/max_health)),0]
                num_health = "GPA {}/{}".format(self.health,max_health)
                disp_health = int((health/max_health)*175)

                block_level = lv.render(level, True, (0, 0, 0))
                block_health = lv.render(num_health, True, (0, 0, 0))
                pygame.draw.rect(self.uidisplay, GREEN,(x+ 250, y+50, disp_health, 15))
                self.uidisplay.blit(block_health,(x+80,y+50))
                self.uidisplay.blit(monitor,(x,y))
                self.uidisplay.blit(block,(x+25,y+15))
                self.uidisplay.blit(block_level,(x+350,y+25))
                pygame.draw.rect(self.uidisplay, BLACK,(x+ 247, y+47, 181, 21))
                pygame.draw.rect(self.uidisplay, GRAY,(x+ 250, y+50, 175, 15))
                pygame.draw.rect(self.uidisplay, GREEN,(x+ 250, y+50, disp_health, 15))
                self.uidisplay.blit(block_health,(x+80,y+50))
                pygame.display.update()
                sleep(0.03)


            self.uidisplay.blit(one,(x+490,y+410))
            self.uidisplay.blit(two,(x+650,y+410))
            self.uidisplay.blit(three,(x+490,y+470))
            self.uidisplay.blit(four,(x+650,y+470))
            pygame.draw.rect(self.uidisplay, RED, [570+pos, 450+tres, 150, 50], 5)



            pygame.display.update()
            


            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RETURN:
                            pygame.mixer.music.stop()
                            #gameExit = True
                            if(pos == 150 and tres == 45):
                                print("Bag")
                            if(pos == 150 and tres == 0):
                                self.dialog_box(["You ran away from your professor,","but they know you'll be back.. ","They always come back"])
                                gameExit = True
                            if(pos == 0 and tres == 45):
                                print("Debate")
                            if(pos == 0 and tres == 0):
                                self.Fight()

                        elif event.key == pygame.K_RIGHT:
                            pos = 150

                        elif event.key == pygame.K_LEFT:
                            pos = 0

                        elif event.key == pygame.K_DOWN:
                            tres = 45

                        elif event.key == pygame.K_UP:
                            tres = 0


    def character_intro(self):
        self.character = pygame.image.load(os.path.join('graphics','battle_you.png'))
        self.character = pygame.transform.scale(self.character,(300,300))
        for x in range (-150,50):
            self.uidisplay.blit(self.background,(0,0))
            self.uidisplay.blit(self.character,(x,275))
            pygame.display.update()
            


    def enemy_intro(self):

        for x in range(750,600,-1):
            
            self.uidisplay.blit(self.background,(0,0))
            self.uidisplay.blit(self.character,(50,275))
            self.uidisplay.blit(self.enemy_image,(x,100))
            pygame.display.update()


    def Fight(self):
            fonts = pygame.font.Font("fonts/gen_1.ttf", 15)
            player_monitor = pygame.image.load('graphics/text_box2.png')
            player_monitor = pygame.transform.scale(player_monitor,(400,150))
            x = 92
            y = 50
            

            one = fonts.render("Argue", True, (0, 0, 0))
            two = fonts.render("Solve", True, (0, 0, 0))
            three = fonts.render("Cry", True, (0, 0, 0))
            four = fonts.render("Cheat", True, (0, 0, 0))



            RED = [255,0,0]
            pos = 0
            tres = 0


            gameExit = False
            while not gameExit:

                self.uidisplay.blit(player_monitor,(x + 450,y + 370))
                self.uidisplay.blit(one,(x+490,y+410))
                self.uidisplay.blit(two,(x+650,y+410))
                self.uidisplay.blit(three,(x+490,y+470))
                self.uidisplay.blit(four,(x+650,y+470))
                pygame.draw.rect(self.uidisplay, RED, [570+pos, 450+tres, 150, 50], 5)



                pygame.display.update()
                


                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

                        if event.type == pygame.KEYDOWN:

                            if event.key == pygame.K_RETURN:
                                pygame.mixer.music.stop()

                                if(pos == 150 and tres == 45):
                                    self.health -= 0.50
                                    self.health = round(self.health,2)
                                if(pos == 150 and tres == 0):
                                    self.health -= 1.50
                                    self.health = round(self.health,2)
                                if(pos == 0 and tres == 45):
                                    self.health += 1.50
                                    self.health = round(self.health,2)
                                    self.dialog_box(["The professor feeds on your tears"])
                                if(pos == 0 and tres == 0):
                                    self.dialog_box(["You really thought that would work?"])
                                    sleep(2)
                                gameExit = True

                            elif event.key == pygame.K_RIGHT:
                                pos = 150

                            elif event.key == pygame.K_LEFT:
                                pos = 0

                            elif event.key == pygame.K_DOWN:
                                tres = 45

                            elif event.key == pygame.K_UP:
                                tres = 0

            
    def dialog_box(self,Statement = ["..."]):
            #need to make a map ui so that It can be referened for this
            #background = pygame.image.load(os.path.join('Maps','town.png'))
            #background = pygame.transform.scale(background,(942,567))


            #self.uidisplay = pygame.display.set_mode((942,567))
            gameExit = False
            #self.uidisplay.blit(background,(0,0))
            font = pygame.font.Font("fonts/gen_1.ttf", 15)
            speed = .09
            x = -3
            y = 475
            text_box = pygame.image.load("graphics/text_box.png")

            for sentence in Statement:
                name = ''
                line = y + 40
                self.uidisplay.blit(text_box,(x,y))
                gameExit = False
                for letter in sentence:
                    name += letter
                    if len(name) > 40:
                        name = ''
                        line = y + 60
                    block = font.render(name, True, (0, 0, 0))
                    self.uidisplay.blit(block, (x + 25,line))
                    #pygame.display.update((x,y,x+100,y+100))  
                    pygame.display.update()            
                    sleep(speed)

                while not gameExit:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

                        if event.type == pygame.KEYDOWN:

                            if event.key == pygame.K_RETURN:
                                
                                gameExit = True                            