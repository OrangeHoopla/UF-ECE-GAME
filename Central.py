import os, pygame
import time
from time import sleep
from Player import Player
from User_UI import Menu
from Maps import World
import glob



class Game:

    def __init__(self):
        pygame.init()
        self.location = World()

        self.gameDisplay = pygame.display.set_mode(self.location.size)
        pygame.display.set_caption('ECEmon version 2.2')
        self.clock = pygame.time.Clock()

        self.player = Player()
        
        self.intro()
        self.Loading_screen()
        
        

        
        #insert loading screen basics


    def main(self):

            
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

                #for saving maps and other items
                if self.player.saving:
                    
                    self.player.character_info['Location'][2] = self.location.current_info['Name']
                    self.player.save_character()
                    self.player.saving = False


        


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


    def Loading_screen(self):

        gameDisplay = pygame.display.set_mode((942,567))
        
        font = pygame.font.Font("fonts/gen_1.ttf", 15)
        menu = pygame.image.load("graphics/text_box.png")
        point = pygame.image.load('graphics/menupointer.png')
        background = pygame.image.load('graphics/new_load.png')

        background = pygame.transform.scale(background,(942,567))
        gameDisplay.blit(background,[0,0])
        
        block1 = font.render("Load save", True, (0, 0, 0))
        block2 = font.render("New Game", True, (0, 0, 0))
        location = 1
        gameExit = False

        while not gameExit:
            
            gameDisplay.blit(menu,(250,10))
            gameDisplay.blit(point,(-100,location*32 -20 ))
            
            gameDisplay.blit(block1,(300,40))
            gameDisplay.blit(block2,(300,70))
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
                        gameExit = True

                       
            if location < 1:
                location = 1
            if location > 2:
                location = 2;

        if location == 2:
            self.new_game()
            return
        else:
            self.display_load_options()
            return

        


    def new_game(self):
        guy = pygame.image.load("graphics/pixel_moore.png")
        guy = pygame.transform.scale(guy,(200,300))
        gameDisplay = pygame.display.set_mode((942,567))
        new_game = Menu(gameDisplay)
        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(guy,(600,50))
        

        text_box = pygame.image.load("graphics/text_box.png")
        gameExit = False
        name = ''
        font = pygame.font.Font("fonts/gen_1.ttf", 15)
        #gameDisplay.blit(prof,(10,250))
        new_game.dialog_box(["Welcome to the University of Florida","More importantly Welcome  to our Department","of Electrical and         Computer Engineering"])
        new_game.dialog_box(["at your stay here you     will be seeing A lot","well tell me your name     kid..."])
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        name += event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    if event.key == pygame.K_RETURN:
                        gameExit = True
                        #line 1
                        
                    if event.key == pygame.K_SPACE:
                        name += " "
                        
               
                block = font.render(name, True, (0, 0, 0))
                rect = block.get_rect()
                
                gameDisplay.blit(text_box,(10,400))
                gameDisplay.blit(block, (30,425))
                        
                pygame.display.update()
                
        new_game.dialog_box(["Alright " + name, "While here at UF you will have your GPA act as your health","because we're nice we will give you a 4.00 to start"])
        new_game.dialog_box(["Your grade level will represent your Rank","and as you learn things you will learn new skills"])

        self.player.character_info = {'Name': name, 'Location': [150, 150, 'HomeTown']}

    def display_load_options(self):
        gameDisplay = pygame.display.set_mode((942,567))
        gameDisplay.fill((53, 56, 43))
        font = pygame.font.Font("fonts/gen_1.ttf", 15)
        point = pygame.image.load('graphics/menupointer.png')
        files = glob.glob('Saves/*.npy')
        gameExit = False
        location = 1
        name = [file[6:-4] for file in files]
        menu = pygame.image.load("graphics/large_text_box.png")

        while not gameExit:
                
                gameDisplay.blit(menu,(250,10))
                gameDisplay.blit(point,(-100,location*32 -20 ))
                
                j = 1
                for i in name:
                    gameDisplay.blit(font.render(i, True, (0, 0, 0)),(300,10+j*30))
                    j += 1
               
               
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
                            gameExit = True

                           
                if location < 1:
                    location = 1
                if location > len(name):
                    location = len(name);





        self.player.load_character(name[location-1])
        self.location.load_map(self.player.character_info["Location"][2])





if __name__ == "__main__":
    user = Game()
    user.main()



