import pygame
import time
from time import sleep
import glob
from load_functions import reader, write

pygame.init()

# notes make teleport function and have the back ground move instead of character
#most important finish intro for new game
#add response function for responding to people
info = []
level = 0
global_x = 154
map_x = 0
map_y = 0
global_y = 170
background_x = 0
background_x = 0
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



    #time.sleep(2)
    #V needs work 285,210,510,325
def obsticle(block,x,y,m,v):
    global global_x
    global global_y
    global map_x
    global map_y
    block[0] = block[0] + map_x
    block[1] = block[1]+ map_y
    block[2] = block[2]+ map_x
    block[3] = block[3]+ map_y
    # dem constants have to do with the speed
    if (x-6) > block[0] and (x+6) < block[2]:
        if y > block[1] and y < block[3]:
            m,v = 0,0
            if -6 <= (y-block[3]): # has to be slightly greater than moving speed
                y = block[3]
            else: y = block[1]

            
        if y < block[3] and y > block[1]:
            y = block[3]

    if y > block[1] and y < block[3]:
        if x > block[0] and x < block[2]:
            m,v = 0,0
            if -6 <= (x-block[2]):
                x= block[2]
            else: x = block[0]

    
    global_x = x
    global_y = y
    return m,v
    




def navigator(level=0):
    global global_x
    global global_y
    if level == 0:
        intro()

    elif level == 1:
        stage1(global_x,global_y)
    elif level == 2:
        hospital()

    elif level == 3:
        new_load()
    elif level == 4:
        load_screen()
    elif level == 5:
        Display_loads()
    elif level == 6:
        Lab()
    elif level == 7:
        stage2()




def stage1(x=151,y=250):
    
    pygame.mixer.music.load('town.wav')
    background = pygame.image.load("town.png")
    #size = (width, height) = background.get_size()
    #backgroundRect = background.get_rect()
    #menu = pygame.image.load("PauseMenu.png")
    global global_x
    global global_y
    global map_y
    global map_x
    global level
    
    
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
    #pygame.mixer.music.play(-1)
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
                    x_change = 0
                    y_change = 0
                

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                countc = 0
                count = 0
                
        x_change,y_change = obsticle([285,210,510,325],global_x,global_y,x_change,y_change)
        x_change,y_change = obsticle([490,0,840,190],global_x,global_y,x_change,y_change)
        x_change,y_change = obsticle([90,350,510,460],global_x,global_y,x_change,y_change)
        x_change,y_change = obsticle([140,25,345,140],global_x,global_y,x_change,y_change)
        x_change,y_change = obsticle([680,315,900,440],global_x,global_y,x_change,y_change)


        global_x += x_change
        global_y += y_change
        count += countc

        gameDisplay.blit(background,(map_x,map_y))
        
        
        print "x: %f" %global_x
        print "y: %f" %global_y
        #basic borders
        
        if global_x < 36:
            global_x = 36
            #map_x += 5
        if global_x > 840:
            global_x = 840
            #map_x -= 5
        if global_y > 517:
            global_y = 517
            #map_y += 5
        if global_y < 30:
            global_y = 30
            #map_y -= 5
            #buildings
            
       
        
        #walking animation
        if count > 19:
            count = 0
        
        player(global_x,global_y,tupl,count)
        #hospital entrance
        pygame.display.update()
        gameDisplay.fill((0,0,0))
        if global_x - map_x >230 and global_x - map_x < 255:
            if global_y - map_y< 145 and global_y - map_y > (145 - 50):
                gameExit = True
                portal_val = 2
                portal_x = 457
                portal_y = 470
        #lab entrance
        if global_x - map_x >385 and global_x - map_x < 405:
            if global_y - map_y< 326 and global_y - map_y > (326 - 50):
                gameExit = True
                portal_val = 6
                portal_x = 457
                portal_y = 470
        #stage 2 entrance
        if global_y - map_y > 235 and global_y - map_y < 310:
            if global_x - map_x < 37 and global_x - map_x > (37-50):
                gameExit = True
                portal_val = 7
                portal_x = 820
                portal_y =200
                map_x = -2650
                map_y = -1220
                

            
        
        
        
        clock.tick(30)
    pygame.mixer.music.fadeout(1500)
    
    level = portal_val
    
    global_x = portal_x
    
    global_y = portal_y
    

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
    global level
    level = 4
    

def hospital():
    global global_x
    global map_x
    global map_x
    
    global level
    global global_y
    
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
                    pausemenu()
                    x_change = 0
                    y_change = 0
                    
                    
                

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                countc = 0
                count = 0
                
        x_change,y_change = obsticle([260,115,655,235],global_x,global_y,x_change,y_change)

        global_x += x_change
        global_y += y_change
        count += countc

        #gameDisplay.fill(white)

        
        
        gameDisplay.blit(background,hombreRect)
        #message_display("tester")
        
        #car(500,-500)
        print "x: %f" %global_x
        print "y: %f" %global_y
        #basic borders
        
        if global_x < 36:
            global_x += 5
        if global_x > 840:
            global_x = 840
        if global_y > 517:
            global_y = 517
        if global_y < 30:
            global_y = 30
            '''
        x,y = obsticle([285,210,510,325],x,y)
        x,y = obsticle([490,0,840,190],x,y)
        x,y = obsticle([90,350,510,460],x,y)
        '''
        
        if count > 19:
            count = 0
        
        player(global_x,global_y,tupl,count)

        # the eglobal_xit
        if global_x > 410 and global_x < 510:
            if global_y > 500:
                gameExit = True
        
        pygame.display.update()
        clock.tick(30)
    
    level = 1
    
    global_x = 240 + map_x
    
    global_y = 145 + map_y

    


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
                if event.key == pygame.K_RETURN:
                    MenuOption(location)
                    return
                   
        if location < 1:
            location = 1
        if location > 9:
            location = 9;

         

def MenuOption(value):
    if value == 4:
        result = display_option(["yes","no","sure","mabye?"])
        if result == 1:
            display_text(["you fucked up man."])
    if value == 5:
        display_text(["Your name is " + info[1]])
    if value == 6:
        #save
        #global info
        global global_x
        global global_y
        global level
        global info
        info[3] = global_x
        info[4] = global_y
        info[2] = level
        info[7] = map_x
        info[8] = map_y
        write(info)

        display_text(["The Game has been saved."])

def new_load():
    gameDisplay.fill((0, 0, 0))
    text_box = pygame.image.load("text_box.png")
    global info
    global level
    level = 1
    global global_x
    global global_y
    global map_x
    global map_y

    info.append("from_start.txt") 

    
    gameExit = False
    name = ''
    font = pygame.font.Font("font.ttf", 15)
    #gameDisplay.blit(prof,(10,250))
    display_text(["Welcome to the University of Florida","More importantly Welcome  to our Department","of Electrical and         Computer Engineering"],1)
    display_text(["at your stay here you     will be seeing A lot","well tell me your name     kid"],1)
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
                    info.append(name)
                if event.key == pygame.K_SPACE:
                    name += " "
                    
           
            block = font.render(name, True, (0, 0, 0))
            rect = block.get_rect()
            
            gameDisplay.blit(text_box,(10,400))
            gameDisplay.blit(block, (30,425))
                    
            pygame.display.update()
            clock.tick(30)
    info.append(1)
    info.append(global_x)
    info.append(global_y)
    #health
    info.append(4)
    #skills
    info.append("[]")
    #
    info.append(map_x)
    info.append(map_y)

                
def display_text(phrase = ["empty"],character = 0,speed = .07,x = 10, y = 400):
    text_box = pygame.image.load("text_box.png")
    if character == 1:
        prof = pygame.image.load("pixel_moore.png")
        gameDisplay.blit(prof,(x,y-150))
    font = pygame.font.Font("font.ttf", 15)
    
    #important to keep sentence under certain  ###27###
    #thatt was before second line implementation
    for sentence in phrase:
        name = ''
        line = y +25
        gameDisplay.blit(text_box,(x,y))
        gameExit = False
        for letter in sentence:
            name += letter
            if len(name) > 25:
                name = ''
                line = y + 60
            block = font.render(name, True, (0, 0, 0))
            gameDisplay.blit(block, (x + 25,line))
            pygame.display.update()
            clock.tick(30)                
            sleep(speed)
        for event in pygame.event.get():
                if event.type == pygame.K_RETURN:
                    pygame.event.clear(pygame.K_RETURN)
                    
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameExit = True
        name = ''
        block = font.render(name, True, (0, 0, 0))
        gameDisplay.blit(block, (30,line))
        pygame.display.update()

def load_screen():
    
    font = pygame.font.Font("font.ttf", 15)
    menu = pygame.image.load("text_box.png")
    point = pygame.image.load('menupointer.png')
    background = pygame.image.load('loadback.png')

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
    global level
    if location == 2:
        level = 3
    else: level = 5# display load in options


def Display_loads():
    possible = glob.glob("*.txt")
    gameExit = False
    gameDisplay.fill((0,0,0))
    background = pygame.image.load('loadback.png')

    background = pygame.transform.scale(background,(942,567))
    gameDisplay.blit(background,[0,0])
    font = pygame.font.Font("font.ttf", 15)
    point = pygame.image.load('menupointer.png')
    menu = pygame.image.load('LoadMenu.png')
    location = 1

    while not gameExit:
        i = 1
        #gameDisplay.blit(menu,(250,10))
        gameDisplay.blit(point,(-325,location*32 -25 ))
        
        pygame.display.update()
        gameDisplay.blit(menu,(-95,-100))

        for name in possible:
            block = font.render(name[:-4], True, (0, 0, 0))
            gameDisplay.blit(block, (75,i*32))
            i +=1

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_DOWN:
                    location += 1

                if event.key == pygame.K_UP:
                    location -= 1
                if event.key == pygame.K_RETURN:
                    gameExit = True

        if location < 1:
            location = 1
        if location > len(possible):
            location = len(possible)
    global info
    global level
    global global_x
    global global_y
    global map_x
    global map_y
    
    info = reader(possible[location-1])

    
    level = int(info[2])
    global_x = int(info[3])
    global_y = int(info[4])
    map_x = int(info[7])
    map_y = int(info[8])

def display_option(options):
    
    gameExit = False
    point = pygame.image.load('menupointer.png')
    location = 1
    font = pygame.font.Font("font.ttf", 15)
    if len(options) == 2:
        menu = pygame.image.load('text_box.png')
        x = 10
        y = 450
        pointy_offset = 420
        wordx_offset = 50
        wordy_offset = 0


    if len(options) >= 3:
        x = -100
        y = 300
        pointy_offset = 375
        wordx_offset = 175
        wordy_offset = 100
        menu = pygame.image.load('LoadMenu.png')


    while not gameExit:
        i = 1
        #gameDisplay.blit(menu,(250,10))
        gameDisplay.blit(point,(-325,location*32 + pointy_offset ))
        
        pygame.display.update()
        gameDisplay.blit(menu,(x,y))

        for option in options:
            block = font.render(option, True, (0, 0, 0))
            gameDisplay.blit(block, (x+ wordx_offset,y + i*32 + wordy_offset))
            i +=1

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_DOWN:
                    location += 1

                if event.key == pygame.K_UP:
                    location -= 1
                if event.key == pygame.K_RETURN:
                    gameExit = True

        if location < 1:
            location = 1
        if location > len(options):
            location = len(options)

    return location

def battle(foe = 0):



    while not gameExit:
        i = 1
        #gameDisplay.blit(menu,(250,10))
        gameDisplay.blit(point,(-325,location*32 + pointy_offset ))
        
        pygame.display.update()
        

        

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def Lab():
    global global_x
    
    global level
    global global_y
    
    background = pygame.image.load("lab.png")
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
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    tupl = [1, 64, 33, 32]
                    countc += 1

                elif event.key == pygame.K_UP:
                    y_change = -5
                    tupl = [1, 96, 31, 33]
                    countc += 1

                elif event.key == pygame.K_DOWN:
                    y_change = 5
                    tupl = [1, 0, 31, 33]
                    countc += 1

                elif event.key == pygame.K_q:
                    pausemenu()
                    print "yup"
                    x_change = 0
                    y_change = 0
                    
            

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    print "key are up"
                    x_change = 0

                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                countc = 0
                count = 0
        gameDisplay.blit(background,hombreRect)
                
        #x_change,y_change = character(x_change,y_change,250,250,["why are you disappearing?"])

        global_x += x_change
        global_y += y_change
        count += countc

        #gameDisplay.fill(white)

        
        
        
        #message_display("tester")
        
        #car(500,-500)
        print "x: %f" %global_x
        print "y: %f" %global_y
        #basic borders
        
        if global_x < 36:
            global_x += 5
        if global_x > 840:
            global_x = 840
        if global_y > 517:
            global_y = 517
        if global_y < 30:
            global_y = 30
            '''
        x,y = obsticle([285,210,510,325],x,y)
        x,y = obsticle([490,0,840,190],x,y)
        x,y = obsticle([90,350,510,460],x,y)
        '''
        
        if count > 19:
            count = 0
        
        
        player(global_x,global_y,tupl,count)
        x_change,y_change = character(x_change,y_change,250,250,["why are you disappearing?"])
        x_change,y_change = character(x_change,y_change,400,400,["congrats you did it."])
        pygame.display.update()
        


        # the eglobal_xit
        if global_x > 410 and global_x < 510:
            if global_y > 500:
                gameExit = True
        
        
        clock.tick(30)
    
    level = 1
    global_x = 395
    global_y = 335




def character(m,v,locationx = 250,locationy = 250,statement = ["..."],person = 1):
    global global_x
    global global_y
    x = global_x
    y = global_y
    
    
    block = [locationx-20,locationy-20,locationx + 30,locationy + 30]
    block[0] = block[0] + map_x
    block[1] = block[1]+ map_y
    block[2] = block[2]+ map_x
    block[3] = block[3]+ map_y
    npc = pygame.image.load("red.png")
    if person == 0:
        tupl = [0, 0, 0, 0]
    if person == 1:
        tupl = [1, 0, 33, 33]
    obsticle([locationx-20,locationy-20,locationx + 30,locationy + 30],global_x,global_y,m,v)

    gameDisplay.blit(npc,(locationx,locationy),tupl)
    if (x-6) > block[0] and (x+6) < block[2]:
        if y > block[1] and y < block[3]:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print "1111111111111111"
                        display_text(statement)
                        m,v = 0,0
            

            
        

    if y > block[1] and y < block[3]:
        if x > block[0] and x < block[2]:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print "1111111111111111"
                        display_text(statement)
                        m,v = 0,0
    return m,v
            
    
def stage2():
    pygame.mixer.music.load('town.wav')
    background = pygame.image.load("stage2.png")
    #size = (width, height) = background.get_size()
    #backgroundRect = background.get_rect()
    #menu = pygame.image.load("PauseMenu.png")
    global global_x
    global global_y
    global map_y
    global map_x
    global level
    global_x
    
    
    background = pygame.transform.scale(background,(3600,1788))
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
    #pygame.mixer.music.play(-1)
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
                    x_change = 0
                    y_change = 0
                

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                countc = 0
                count = 0
                
        x_change,y_change = obsticle([3350,1625,3515,1725],global_x,global_y,x_change,y_change)
        
        x_change,y_change = obsticle([0,1705,3350,1800],global_x,global_y,x_change,y_change)
        '''
        x_change,y_change = obsticle([90,350,510,460],global_x,global_y,x_change,y_change)
        x_change,y_change = obsticle([140,25,345,140],global_x,global_y,x_change,y_change)
        x_change,y_change = obsticle([680,315,900,440],global_x,global_y,x_change,y_change)
        '''

        global_x += x_change
        global_y += y_change
        count += countc

        gameDisplay.blit(background,(map_x,map_y))
        
        
        print "x: %f" %global_x
        print "y: %f" %global_y
        print "true x: %f" %(global_x -map_x)
        print "true y: %f" %(global_y- map_y)
        #basic borders
        
        if global_x < 75:
            global_x = 75
            map_x += 5
        if global_x > 850:
            global_x = 850
            map_x -= 5
        if global_y > 500:
            global_y = 500
            map_y -= 5
        if global_y < 180:
            global_y = 180
            map_y += 5
            #buildings
            
       
        
        #walking animation
        if count > 19:
            count = 0
        
        player(global_x,global_y,tupl,count)
        pygame.display.update()
        gameDisplay.fill((0,0,0))
        #hospital entrance
        '''
        pygame.display.update()
        gameDisplay.fill((0,0,0))
        if global_x - map_x >230 and global_x - map_x < 255:
            if global_y - map_y< 145 and global_y - map_y > (145 - 50):
                gameExit = True
                portal_val = 2
                portal_x = 457
                portal_y = 470
        #lab entrance
        if global_x - map_x >385 and global_x - map_x < 405:
            if global_y - map_y< 326 and global_y - map_y > (326 - 50):
                gameExit = True
                portal_val = 6
                portal_x = 457
                portal_y = 470

                x = 850
                y top = 170
                y bot = 235
        '''
        if (global_y - map_y) > 1380 and (global_y - map_y) < 1450:
            if (global_x - map_x) > 3515 and global_x - map_x < (3515+50):
                gameExit = True
                portal_val = 1
                portal_x = 40
                portal_y = 275
                map_x = 0
                map_y = 0
                

            
        
        
        
        clock.tick(30)
    pygame.mixer.music.fadeout(1500)
    
    level = portal_val
    
    global_x = portal_x
    
    global_y = portal_y
    











    






        
                
                    
                        

            




            
        

        
        

        


while True:

    navigator(level)
pygame.quit()
quit()
