import math
import random
import numpy as np
import visual_amstelhaege

class Position (object):
    """
    Returns upper-left position of given object. 

    x: an x coordinate (integer).
    y: an y coordinate (integer).
    """
    def __init__(self, x, y):
        """
        Initializes position's x and y coordinate.
        """
        self.x = x
        self.y = y

    def get_x(self):
        """
        Returns the x coordinate of the given object.
        """
        return self.x

    def get_y(self):
        """
        Returns the y coordinate of the given object.
        """
        return self.y

class Fieldmap(object):
	grid = []

	def __init__(self):
		self.grid = np.zeros((15,15), dtype = int)
		self.occupied = {}

	def setOccupiedGround(self, pos_top, pos_bottom, tilevalue):
		self.grid[pos_top.y: pos_bottom.y + 1, pos_top.x: pos_bottom.x + 1] = tilevalue
		self.occupied[(pos_top.x, pos_top.y)] = 300


ground_test = Fieldmap()
pos_linkhoek = Position(1, 2)
pos_rechthoek = Position(4, 4)
num_tilevalue = 3 

ground_test.setOccupiedGround(pos_linkhoek, pos_rechthoek, num_tilevalue)
print ground_test.grid

 def analyze(self): de grid analyseren om waarde te berekenen.

 def move_house(current_state, move):
 	pos.x, pos.y = current_state

 	if move == 'up':
 		pos.x += 1
 	elif move == 'down':
 		pos.x -= 1
 	elif move == "right"
 		pos.y += 1
 	else:
 		pos.y -= 1
 	next_state = pos.x, pos.y	

 	return next_state			



