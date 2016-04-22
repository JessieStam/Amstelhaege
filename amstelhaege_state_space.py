import math
import random
import numpy as np
#import pygame


# matrix alleen nodig voor visualisatie

#elk huis wat is de afstand?


class Position (object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

		#if self.housetype == "small":



class FieldMap (object):
	def __init__(self):
		self.grid = np.zeros((160,150), dtype = int)
		# self.grid = []
		# row = []
		# for i in range(0, 150):
		# 	row.append(0)

		# for j in range (0, 160):
		# 	self.grid.append(row)
				
		#for index, value in enumerate(grid):
		self.occupied = {}

	def getOccupiedGround(self):
		return self.occupied

	def setOccupiedGround(self, pos, housetype):
        self.pos = pos

		# 10 want small house neemt 12 coords in beslag
		if self.housetype == "small":
			self.occupied[self.pos] = SmallHouse()
		elif self.housetype == "medium":
			self.occupied.update({self.pos:})
		else:
			self.occupied.update({self.pos:})

	def isGroundOccupied(self, x, y, width, depth):
		# MOET HOUSETYPE WORDEN MEEGEGEVEN?????
		for pos in self.occupied:
			for i in range(x, (x + width)):
				for j in range (y, (y +depth)):
					if pos.x == i and pos.y == j:
						return True

		return False

	def getRandomPosition(self, width, depth):
        """
        Return a random position inside the room.

        returns: a Position object.
        """

        # get random numbers to generate a random position in room

        # constraints in de functie waar hij aangeroepen wordt
        ran_x = random.randint(0, self.width - 23) 
        ran_y = random.randint(0, self.depth - 23)
        ran_pos = Position(ran_x, ran_y)
        
        return ran_pos

class House (object):
	def __init__(self, x, y):
		field = FieldMap()
		pos = field.getRandomPosition()
	# FUNCTIES DIE VOOR ALLE HUIZEN GELDEN

	def getHousePosition(self):
		return self.pos

	def setHousePosition(self):
		while (isGroundOccupied(self.pos.x, self.pos.y, self.width, self.depth)):
			self.pos = field.getRandomPosition()

	#checken hoeveel meter huis tot andere huizen

	# checken of er al een huis staat <--- field

	#init van super aanroepen <--- googlen (house)

class SmallHouse (House):
	def __init__(self):
		self.width = 12.0
		self.depth = 12.0
		self.housetype = "small"

		

class MediumHouse (House):
	def __init__(self):
		self.width = 16.0
		self.depth = 13.5
		self.housetype = "medium"

		isGroundOccupied(self, x, y, width, depth):

class LargeHouse (House):
	def __init__(self):
		self.width = 23.0
		self.depth = 22.5
		self.housetype = "large"

		isGroundOccupied(self, x, y, width, depth):

