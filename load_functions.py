import glob
print glob.glob("*.txt")
def takeinputs():
	global info
	info[0] = raw_input("save.txt")
	inf0[1] = "hello"

def write(info1): # assumed file name is always first
	file = open(info[0],"w") 

	for i in info1:
		file.write(i + "\n")
		
		
def reader(filename):
	info = []
	file_object  = open(filename, "r")
	for line in file_object:
		
		 line = line[:-1]
		 info.append(line)
		
	file_object.close()

	return info

great = ["test.txt", "hello", "red","health","1","0"]
write(great)

print reader(great[0])
'''

import pygame
from pygame.locals import *

def name():
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    name = ""
    font = pygame.font.Font(None, 50)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    name = ""
            elif evt.type == QUIT:
                return
        screen.fill((0, 0, 0))
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()

if __name__ == "__main__":
    name()
    pygame.quit()

'''
