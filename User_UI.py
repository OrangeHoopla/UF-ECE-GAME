import pygame
import os
from time import sleep
from Fighting import Battles
class Menu():


    def __init__(self,uidisplay):
        self.uidisplay = pygame.display.set_mode((942,567))
        self.cage = Battles(['pixel_moore'])



    def check(self):
        print(pygame.event.get())
        #print("^^^")
        for event in pygame.event.get():
                #print("yessers")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        #print("yes it is me")
                        self.Pause()



                        
    def Pause(self):
        
        menu = pygame.image.load(os.path.join(
            'graphics',
            'PauseMenu.png'))

        point = pygame.image.load(os.path.join(
            'graphics',
            'menupointer.png'))

        location = 1
        
        
        
        
        game = True

        while game:
            
            self.uidisplay.blit(menu,(-325,10))
            self.uidisplay.blit(point,(-325,location*32 -20 ))

            pygame.display.update()
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        game = False



                    if event.key == pygame.K_DOWN:
                        location += 1

                    if event.key == pygame.K_UP:
                        location -= 1
                    if event.key == pygame.K_RETURN:
                        #self.cage.main()
                        
                        game = False
                        
                        
                       
            if location < 1:
                location = 1
            if location > 9:
                location = 9;

        if location == 5:
            self.cage.main()
        return location


    #needs to be cleaned up
    def dialog_box(self,Statement = ["..."]):
        #need to make a map ui so that It can be referened for this
        #background = pygame.image.load(os.path.join('Maps','town.png'))
        #background = pygame.transform.scale(background,(942,567))


        #self.uidisplay = pygame.display.set_mode((942,567))
        gameExit = False
        #self.uidisplay.blit(background,(0,0))
        font = pygame.font.Font("fonts/gen_1.ttf", 15)
        speed = .09
        x = 10
        y = 400
        text_box = pygame.image.load("graphics/text_box.png")

        for sentence in Statement:
            name = ''
            line = y + 25
            self.uidisplay.blit(text_box,(x,y))
            gameExit = False
            for letter in sentence:
                name += letter
                if len(name) > 25:
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

        

                    