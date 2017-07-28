import pygame
import time

pygame.init()




background = pygame.image.load("town.png")
size = (width, height) = background.get_size()
backgroundRect = background.get_rect()

gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('ECEmon version 1.1')
clock = pygame.time.Clock()

carImg = pygame.image.load('red.png')
cropped = pygame.Surface((50, 50))
display_width = backgroundRect.x
display_height = backgroundRect.y






def player(x =0,y = 0, tupl = [1, 0, 33, 33], count = 0):
    #print "count %f" %count
    tupl[0] = 33*int(count/5)
    gameDisplay.blit(carImg,(x,y),tupl)

    
    

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    #time.sleep(2)
    #V needs work 285,210,510,325
def obsticle(block,x,y):
    # dem constants have to do with the speed
    if (x-6) > block[0] and (x+6) < block[2]:
        if y > block[1] and y < block[3]:
            if -6 <= (y-block[3]): # has to be slightly greater than moving speed
                y = block[3]
            else: y = block[1]

            
        if y < block[3] and y > block[1]:
            y = block[3]

    if y > block[1] and y < block[3]:
        if x > block[0] and x < block[2]:
            if -6 <= (x-block[2]):
                x= block[2]
            else: x = block[0]
    return x,y
    




def navigator(level=0, x=150,y=180):
    if level == 0:
        intro()

    if level == 1:
        stage1(x,y)
    if level ==2:
        hospital(x,y)




def stage1(x=150,y=180):
    pygame.mixer.music.load('town.wav')
    background = pygame.image.load("town.png")
    #size = (width, height) = background.get_size()
    #backgroundRect = background.get_rect()
    #menu = pygame.image.load("PauseMenu.png")

    
    
    
    background = pygame.transform.scale(background,(942,567))
    hombreRect = background.get_rect()
    gameDisplay = pygame.display.set_mode((942,567))

    tupl = [33, 0, 33, 33]


    

    x_change = 0
    y_change = 0
    count = 0
    countc = 0
    portal_val = 0
    portal_x = 0
    portal_y = 0

    

    gameExit = False
    pygame.mixer.music.play(-1)
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    tupl = [1, 33, 33, 30]
                    countc += 1
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    tupl = [1, 64, 33, 32]
                    countc += 1

                if event.key == pygame.K_UP:
                    y_change = -5
                    tupl = [1, 96, 31, 33]
                    countc += 1

                if event.key == pygame.K_DOWN:
                    y_change = 5
                    tupl = [1, 0, 31, 33]
                    countc += 1
                if event.key == pygame.K_q:
                    print "yup"
                    pausemenu()
                

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                countc = 0
                count = 0
                


        x += x_change
        y += y_change
        count += countc

        #gameDisplay.fill(white)

        
        
        gameDisplay.blit(background,hombreRect)
        #gameDisplay.blit(menu,(-325,10))
        #message_display("tester")
        
        #car(500,-500)
        print "x: %f" %x
        print "y: %f" %y
        #basic borders
        
        if x < 36:
            x += 5
        if x > 840:
            x = 840
        if y > 517:
            y = 517
        if y < 30:
            y = 30
            #buildings
        x,y = obsticle([285,210,510,325],x,y)
        x,y = obsticle([490,0,840,190],x,y)
        x,y = obsticle([90,350,510,460],x,y)
        x,y = obsticle([140,25,345,140],x,y)
        x,y = obsticle([680,315,900,440],x,y)
        #walking animation
        if count > 19:
            count = 0
        
        player(x,y,tupl,count)
        #pokemon entrance
        if x >230 and x < 255:
            if y < 145 and y > (145 - 50):
                gameExit = True
                portal_val = 2
                portal_x = 460
                portal_y = 470

            
        
        
        pygame.display.update()
        clock.tick(30)
    pygame.mixer.music.fadeout(1500)
    navigator(portal_val,portal_x,portal_y)

def intro():

    pygame.mixer.music.load('intro.wav')
    pygame.mixer.music.play(-1)

    logo = pygame.image.load("smaller_intro.png")
    hombre = pygame.image.load("back.png")
    hombreRect = hombre.get_rect()

    size1 = (width, height) = hombre.get_size()
    logoRect = logo.get_rect()

    gameDisplay = pygame.display.set_mode(size1)
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameExit = True
                


        

        
        gameDisplay.blit(hombre,hombreRect)
        gameDisplay.blit(logo,(250,0))
        
        #car(500,-500)
    
            
        #if x 
        
        pygame.display.update()
        clock.tick(60)
    pygame.mixer.music.fadeout(500)
    navigator(1)

def hospital(x=150,y=180):
    background = pygame.image.load("hospital.png")
    background = pygame.transform.scale(background,(942,567))
    #size = (width, height) = background.get_size()
    #backgroundRect = background.get_rect()

    
    hombreRect = background.get_rect()
    #size1 = (width, height) = hombre.get_size()
    

    #gameDisplay = pygame.display.set_mode(size1)

    tupl = [33, 0, 33, 33]




    

    x_change = 0
    y_change = 0
    count = 0
    countc = 0

    

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    tupl = [1, 33, 33, 30]
                    countc += 1
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    tupl = [1, 64, 33, 32]
                    countc += 1

                if event.key == pygame.K_UP:
                    y_change = -5
                    tupl = [1, 96, 31, 33]
                    countc += 1

                if event.key == pygame.K_DOWN:
                    y_change = 5
                    tupl = [1, 0, 31, 33]
                    countc += 1

                if event.key == pygame.K_q:
                    print "yup"
                    pausemenu()
                    
                

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                countc = 0
                


        x += x_change
        y += y_change
        count += countc

        #gameDisplay.fill(white)

        
        
        gameDisplay.blit(background,hombreRect)
        #message_display("tester")
        
        #car(500,-500)
        print "x: %f" %x
        print "y: %f" %y
        #basic borders
        
        if x < 36:
            x += 5
        if x > 840:
            x = 840
        if y > 517:
            y = 517
        if y < 30:
            y = 30
            '''
        x,y = obsticle([285,210,510,325],x,y)
        x,y = obsticle([490,0,840,190],x,y)
        x,y = obsticle([90,350,510,460],x,y)
        '''
        x,y = obsticle([260,115,655,235],x,y)
        if count > 19:
            count = 0
        
        player(x,y,tupl,count)

        # the exit
        if x > 410 and x < 510:
            if y > 500:
                gameExit = True

            
        #if x 
        
        pygame.display.update()
        clock.tick(30)

    navigator(1,240,145)


def pausemenu():
    #gameDisplay = pygame.display.set_mode((942,567))
    menu = pygame.image.load('PauseMenu.png')
    point = pygame.image.load('menupointer.png')
    location = 1
    
    
    
    
    gameExit = False

    while not gameExit:
        
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
                   
        if location < 1:
        	location = 1
        if location > 9:
        	location = 9;
                




	    	
        

        
        

        
















navigator()
pygame.quit()
quit()
