import pygame
import os
import numpy as np 
'''
Storage file 
Map -> map file name
Obsticle -> array of tuples(x1,y1,x2,y2) that should be blocked on the map
Portal -> array of tuples(x1,y1,x2,y2,"name_of_file",new_x,new_y) 
if entered teleports person to certain point
Adjustable -> true or false
Map Spot -> tuple of where map is on the screen





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

		if not self.current_info["Adjustable"]:
			self.background = pygame.transform.scale(self.background,(942,567))


	def save_map(self, name):
		np.save("Maps/"+ name + ".npy", self.current_info)


	def map_check(self, x, y):
		#should iterate through all map based info
		for portal in self.current_info["Portal"]:

			if x > portal[0] and x < portal[2]:
				
				if y > portal[1] and y < portal[3]:

					x = portal[5]
					y = portal[6]
					self.load_map(portal[4])

		



		return x,y
			

		
