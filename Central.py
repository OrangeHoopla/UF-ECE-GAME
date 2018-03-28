import os, pygame
import time
from time import sleep
from Player import Player
from User_UI import Menu
from Maps import World




class Game:

    def __init__(self):
        pygame.init()
        self.location = World()

        self.gameDisplay = pygame.display.set_mode(self.location.size)
        pygame.display.set_caption('ECEmon version 2.0')
        self.clock = pygame.time.Clock()

        self.intro()
        #self.menu = Menu()
        self.player = Player()
        
        #insert loading screen basics


    def main(self):

        


            self.player.x = 150
            self.player.y = 150

            
            while True:

                self.gameDisplay.blit(self.location.background,(self.location.x,
                                                                self.location.y))
              
                print("X: {} Y: {}".format(self.player.x,
                                           self.player.y))

                self.player.move()

                self.player.x, self.player.y = self.location.map_check(self.player.x,
                                                                       self.player.y)
                #self.menu.check()
                pygame.display.update()

                self.clock.tick(30)

        


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
    user = Game()
    user.main()



