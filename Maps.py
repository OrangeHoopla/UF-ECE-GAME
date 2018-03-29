import pygame
import os
import numpy as np 
from Fighting import Battles
'''
Storage file 
Map -> map file name
Obsticle -> array of tuples(x1,y1,x2,y2) that should be blocked on the map
Portal -> array of tuples(x1,y1,x2,y2,"name_of_file",new_x,new_y) 
if entered teleports person to certain point
Adjustable -> true or false
Map Spot -> tuple of where map is on the screen
name - > file name





'''

class World():

    def __init__(self):
        self.current_map = 0
        self.x = 0
        self.y = 0
        self.current_info = {}
        self.load_map("HomeTown")
        
        
        self.size =  self.background.get_size()
        



    def load_map(self, name):

        self.current_info = np.load("Maps/" + name + ".npy").item()
        self.background = pygame.image.load(os.path.join('Maps',self.current_info["Map"]))
        self.size =  self.background.get_size()

        if not self.current_info["Adjustable"]:
            self.background = pygame.transform.scale(self.background,(942,567))
        else:
            self.background = pygame.transform.scale(self.background,self.current_info["Scale"])


    def save_map(self, name):
        np.save("Maps/"+ name + ".npy", self.current_info)


    def map_check(self, x, y):
        #should iterate through all map based info
        global_x = x - self.x
        global_y = y - self.y


        for portal in self.current_info["Portal"]:

            if x > portal[0] and x < portal[2]:
                
                if y > portal[1] and y < portal[3]:

                    x = portal[5]
                    y = portal[6]
                    self.load_map(portal[4])



        for block in self.current_info["Obsticle"]:
            #old obsticle code that need to be cleaned
            if (x-6) > block[0] and (x+6) < block[2]:
                if y > block[1] and y < block[3]:
                    
                    if -6 <= (y-block[3]): # has to be slightly greater than moving speed
                        y = block[3]
                    else: y = block[1]

                elif y < block[3] and y > block[1]:
                    y = block[3]

            if y > block[1] and y < block[3]:
                if x > block[0] and x < block[2]:
                    
                    if -6 <= (x-block[2]):
                        x= block[2]
                    else: x = block[0]

        #screen border
        #(942,567)
        
        if x < 0:
            x = 0
        if x > 846:
            x = 846
        if y < 0:
            y = 0
        if y > 550:
            y = 549
        #hot mess
        if self.current_info["Adjustable"]:
            if x <= 0:
                
                x = 1
                self.x = self.x + 3
            if x >= 846:
                x = 845
                self.x = self.x - 3
            if y <= 0:
                y = 1
                self.y = self.y + 3
            if y >= 550:
                y = 549
                self.y = self.y - 3
            print("Glob_x: {} Glob_y: {}".format(global_x,global_y))
            if global_y-200 > self.current_info["Scale"][1]:
                #self.y = self.y-4
                #self.y = self.current_info["Scale"][1]
                global_y = self.current_info["Scale"][1]
            if global_x > self.current_info["Scale"][0]:
                x = self.current_info["Scale"][0] -5


        



        return x,y
            

        
