import math
import random
import numpy as np
import visual_amstelhaege
from itertools import product, starmap

class Position (object):
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

    def __str__(self):
        return str(self.x) + ", " + str(self.y)    

class Fieldmap(object):
	grid = []

	def __init__(self):
		self.grid = np.zeros((15,15), dtype = int)
		self.occupied = []

	def setOccupiedGround(self, pos_top, pos_bottom, tilevalue):
		self.grid[pos_top.y: pos_bottom.y + 1, pos_top.x: pos_bottom.x + 1] = num_tilevalue

        # pos_top = Position(pos_top.x, pos_top.y)
        # self.occupied.append(pos_top)

     

ground_test = Fieldmap()
pos_linkhoek = Position(3, 2)
pos_rechthoek = Position(5, 4)
num_tilevalue = 3 

pos_free_space_small = (pos_linkhoek-2, pos_rechthoek + 2)
pos_free_space_bungalow = (pos_linkhoek - 6, pos_rechthoek +6)
pos_free_space_maison = (pos_linkhoek - 12, pos. rechterhoek +12)
 en dan nu checken of de ring hieromheen vrij is. 
 

# x, y = (3,3)
# cells = starmap(lambda a,b: (x + a, y + b), product((0, -1, 1), product(0, -1, +1)))
# print (list(cells)[1:])


# # size "house"
# X = 10
# Y = 10

# neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, (x+2)
#                                         for y2 in range (y-1, y+2)
#                                         if (-1 < x <= X and -1 < y <= Y and 
#                                             (x != x2 or y != y2) and (0 <= x2 <= X) and 
#                                             (0 <= y2 <= Y))

# print neighbors(5,5)                                        


# def house(self):
#     for row in range(15):
#         for column in range (15):
#             grid[].append(3)
#             return house

ground_test.setOccupiedGround(pos_linkhoek, pos_rechthoek, num_tilevalue)
print ground_test.grid




