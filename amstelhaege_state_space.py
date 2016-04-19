import math
import random

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
		self.width = 150
		self.depth = 160
		self.occupied = []

	def getOccupiedGround(self):
		return self.occupied

	def setOccupiedGround(self, pos, housetype):
        width_x = 0
        height_y = 0

		# 10 want small house neemt 12 coords in beslag
		if self.housetype == "small":
			width_x = 12.0
			heigth_y = 12.0
		elif self.housetype == "medium":
			width_x = 16.0
			height_y = 13.5
		else:
			width_x = 23.0
			height_y = 22.5

		for coord_x in range(int(pos.x), int(width_x)):
			for coord_y in range(int(pos.y), int(height_y)):
				self.pos = (coord_x, coord_y) 
				self.occupied.append(self.pos)
		
		# geen floats voor in range !?!?!?
		if self.housetype is not "small":
			self.occupied.append(pos.x + width_x, pos.y + height_y)

	def isGroundOccupied(self, x, y):
		check_coord = (x, y)

		if check_coord in self.occupied:
            return True
        return False

	def getRandomPosition(self, housetype):
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

class SmallHouse (object):
	def __init__(self):
		self.width = 12.0
		self.depth = 12.0
		self.housetype = "small"
		field = FieldMap()
		self.pos = field.getRandomPosition()

	def getSmallHousePosition(self):
		return self.pos

class MediumHouse (object):
	def __init__(self):
		self.width = 16.0
		self.depth = 13.5
		self.housetype = "medium"
		field = FieldMap()
		self.pos = field.getRandomPosition()

	def getSmallHousePosition(self):
		return self.pos

class LargeHouse (object):
	def __init__(self):
		self.width = 23.0
		self.depth = 22.5
		self.housetype = "large"
		field = FieldMap()
		self.pos = field.getRandomPosition()

	def getSmallHousePosition(self):
		return self.pos


