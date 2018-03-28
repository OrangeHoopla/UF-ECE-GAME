import pygame
import os


class Battles():

    def __init__(self):
        self.uidisplay = pygame.display.set_mode((942,567))
        self.background = pygame.image.load(os.path.join('graphics','Battle_scene2.png'))
        self.background = pygame.transform.scale(self.background,(942,567))


    def main(self):
        gameExit = False
        pygame.mixer.music.load(os.path.join(
            'sounds',
            'battle_music.mp3'))
        pygame.mixer.music.play(-1)


        self.uidisplay.blit(self.background,(0,0))
        pygame.display.update()
        self.character_intro()


        while not gameExit:
            self.uidisplay.blit(self.background,(0,0))
            self.uidisplay.blit(self.character,(50,275))



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
