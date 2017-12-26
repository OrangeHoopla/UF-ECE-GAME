import os, pygame
import time
from time import sleep
from Player import Player
from User_UI import Menu

pygame.init()

background = pygame.image.load(os.path.join('Maps','town.png'))
background = pygame.transform.scale(background,(942,567))
size =  background.get_size()


gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('ECEmon version 2.0')
clock = pygame.time.Clock()



class Game:

    def __init__(self):
        self.intro()
        menu = Menu()
        player = Player()
        #insert loading screen basics

        while True:


            player.move()
            menu.check()
            #updates

            gameDisplay.blit(background,(0,0))

            gameDisplay.blit(player.image,
                            (player.x,player.y),
                             player.section)

            pygame.display.update()

            clock.tick(30)


    def intro(self):

        pygame.mixer.music.load(os.path.join(
            'sounds',
            'intro.wav'))
        pygame.mixer.music.play(-1)


        logo = pygame.image.load(os.path.join(
            'graphics',
            'smaller_intro.png'))

        hombre = pygame.image.load(
            os.path.join('graphics','back.png'))


        hombreRect = hombre.get_rect()
        size1 = (width, height) = hombre.get_size()
        logoRect = logo.get_rect()
        gameDisplay = pygame.display.set_mode(size1)

        status = 1
        while status:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        status = 0
                        pygame.mixer.music.stop()
                        
            gameDisplay.blit(hombre,hombreRect)
            gameDisplay.blit(logo,(250,0))
            pygame.display.update()


    def navigation(self):
        if self.location == 1:
            print("thats all")






    

    





if __name__ == "__main__":
    Game()



