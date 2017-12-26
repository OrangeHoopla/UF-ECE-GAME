import pygame
import os

class Menu():

    def check(self):

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.Pause()



                        
    def Pause(self):
        menu = pygame.image.load(os.path.join('graphics','PauseMenu.png'))
        point = pygame.image.load(os.join.path('graphics','menupointer.png'))
        location = 1
        
        
        
        
        game = True

        while game:
            
            gameDisplay.blit(menu,(-325,10))
            gameDisplay.blit(point,(-325,location*32 -20 ))

            pygame.display.update()
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        gameExit = True



                    if event.key == pygame.K_DOWN:
                        location += 1

                    if event.key == pygame.K_UP:
                        location -= 1
                    if event.key == pygame.K_RETURN:
                        MenuOption(location)
                        return
                       
            if location < 1:
                location = 1
            if location > 9:
                location = 9;

                    