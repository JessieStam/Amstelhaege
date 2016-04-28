import math
import random
import numpy as np
import visual_amstelhaege
#import pygame


# matrix alleen nodig voor visualisatie

#elk huis wat is de afstand?

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

        #if self.housetype == "small":


class FieldMap (object):
    """
    Represents the 150x160m2 area on which the houses and water should be positioned.
    The map is made up of a list containing 160 lists, each containing 150 integer values.
    These tiles are either occupied or not occupied.
    """

    grid = []

    def __init__(self):
        """
        Initializes grid for the area. Initially this grid is filled with zeros of type integer.
        """
        # create grid filled with 0s (an int) using numpy
        #self.grid = np.zeros((320,300), dtype = int)
        self.grid = np.zeros((15,15), dtype = int)

        
        # code below is filling grid using iterations, in case the above doesn't work
            # self.grid = []
            # row = []
            # for i in range(0, 150):
            #   row.append(0)

            # for j in range (0, 160):
            #   self.grid.append(row)
                
        #for index, value in enumerate(grid) (store occupied locations in dictionary, we're not sure if we will use this yet)
        self.occupied = {}


    # def getOccupiedGround(self):
    #     """
    #     Returns occupied coordinates.
    #     """
    #     return self.occupied

    def setOccupiedGround(self, pos_top, pos_bottom, worth):
        """
        Places the houses onto the map.
        Changes the integer values for occupied positions to 1 for small house, 2 for medium house, 3 for large house.

        pos: a Position object.
        housetype: a house of certain size.
        """

        # for i in range (pos_top.x, pos_bottom.x + 1):
        #     #column
        #     for j in range(pos_top.y, pos_bottom.y + 1):
        #         self.grid[i][j] = worth

        self.grid[pos_top.y: pos_bottom.y + 1, pos_top.x: pos_bottom.x + 1] = worth
        self.occupied[(pos_top.x, pos_top.y)] = 300

        #10 want small house neemt 12 coords in beslag
        # if self.housetype == "small":
        #     self.occupied[self.pos] = SmallHouse()
        # elif self.housetype == "medium":
        #     self.occupied.update({self.pos:})
        # else self.housetype == "large":
        #     self.occupied.update({self.pos:})


        # if self.housetype == "small":
        #     self.grid



    def isGroundOccupied(self, x, y, width, depth):
        # MOET HOUSETYPE WORDEN MEEGEGEVEN?????
        for pos in self.occupied:
            for i in range(x, (x + width)):
                for j in range (y, (y + depth)):
                    if pos[0] == i and pos[1] == j:
                        return True

        return False

    # def getRandomPosition(self, width, depth):
    #     # """
    #     # Return a random position inside the room.
    #     # returns: a Position object.
    #     # """

 #        # get random numbers to generate a random position in room

 #        # constraints in de functie waar hij aangeroepen wordt
 #        ran_x = random.randint(0, self.width - 23) 
 #        ran_y = random.randint(0, self.depth - 23)
 #        ran_pos = Position(ran_x, ran_y)
 #        return ran_pos

    def amountGroundFree(self):
        # WAAROM MOET ALLES EERST EEN WAARDE KRIJGEN???
        begin_col_hor = 0
        begin_row_hor = 0
        end_col_hor = 0
        end_row_hor = 0
        begin_col_ver = 0
        begin_row_ver = 0
        end_col_ver = 0
        end_row_ver = 0
        begin_pos = Position(0,0)
        house = True
        # 300 x 320 grootte grid
        for col in range(0, 13):
            house == True
            for row in range (0, 13):
                if self.grid[col, row] > 1 and (self.grid[col, row - 1] < 2 or self.grid[col - 1, row] < 2):
                    begin_pos = (col, row)
                if self.grid[col, row] > 1 and self.grid[col, row + 1] < 2 or self.grid[col + 1, row] < 2:
                    begin_col_hor = col
                    begin_row_hor = row
                    house = False
                    print "here"
                elif house == False and self.grid[col, row + 1] > 1 and self.grid[col, row + 2] > 1:
                    end_col_hor = col + 1
                    end_row_hor = row + 1
                    house = True 
                    if self.occupied.get(begin_pos, -1) > (end_row_hor - begin_row_hor):
                        self.occupied[begin_pos] = (end_row_hor - begin_row_hor)
                        print self.occupied[begin_pos]

                if self.grid[col, row] > 1 and self.grid[col + 1, row] < 2:
                    begin_col_ver = col
                    begin_row_ver = row
                    house = False
                elif house == False and self.grid[col + 1, row] > 1 and self.grid[col + 2, row] > 1:
                    end_col_ver = col + 1
                    end_row_ver = row + 1
                    house = True 
                    if self.occupied.get(begin_pos, -1) > (end_row_ver - begin_row_ver):
                        self.occupied[begin_pos] = (end_row_ver - begin_row_ver)
                        print self.occupied[begin_pos]
                                           





ground_test = FieldMap()
pos_linkhoek = Position(1, 2)
pos_rechthoek = Position(4, 4)
num_worth = 3 

ground_test.setOccupiedGround(pos_linkhoek, pos_rechthoek, num_worth)

pos_linkhoek = Position(8, 3)
pos_rechthoek = Position(13, 7)

ground_test.setOccupiedGround(pos_linkhoek, pos_rechthoek, num_worth)

for pos in ground_test.occupied:
    print pos

print ground_test.grid
print ground_test.isGroundOccupied(1, 2, 2, 3)
print ground_test.isGroundOccupied(0, 0, 3, 1)

ground_test.amountGroundFree()

visual_amstelhaege.runProgram(ground_test.grid)


class House (object):
  def __init__(self, x, y):
        self.field = FieldMap()
        self.house_freem2 = 2
        #pos = field.getRandomPosition()
  # FUNCTIES DIE VOOR ALLE HUIZEN GELDEN

  def getHousePosition(self):
        return self.pos

  def setHousePosition(self):
    # get random pos to set house
    self.pos = self.field.getRandomPosition()
    # check if ground for house and obligatory free m2 is already occupied
    while (isGroundOccupied((self.pos.x - self.free_m2), (self.pos.y - self.free_m2), (self.width + self.free_m2), (self.depth + self.free_m2))):
        self.pos = self.field.getRandomPosition()

    # calculate pos of left corner of house + obligatory free m2
    self.pos_top_m2 = (self.pos.x - self.free_m2), (self.pos.y - self.free_m2)
    # calculate pos of richt corner of house
    self.pos_bottom = ((self.pos.x + self.width), (self.pos.y + self.depth))
    # calculate pos of richt corner of house + obligatory free m2
    self.pos_bottom_m2 = ((self.pos_bottom.x + self.free_m2), (self.pos_bottom.y + self.free_m2))

    # set ground of house + obligatory free m2
    setOccupiedGround(self.pos_top_m2, self.pos_bottom_m2, self.house_freem2)
    # overwrite ground of house where only the house is at
    # OF MOET DEZE LAATSTE IN DE HOUSE CLASS ZELF????
    setOccupiedGround(self.pos, self.pos_bottom, self.house_gridworth)

#checken hoeveel meter huis tot andere huizen

# checken of er al een huis staat <--- field

#init van super aanroepen <--- googlen (house)

class SmallHouse (House):
    def __init__(self):
        self.width = 16
        self.depth = 16
        self.free_m2 = 2
        self.house_gridworth = 1

class MediumHouse (House):
    def __init__(self):
        self.width = 20
        self.depth = 15
        self.free_m2 = 3
        self.house_gridworth = 4

class LargeHouse (House):
    def __init__(self):
        self.width = 22
        self.depth = 21
        self.free_m2 = 6
        self.house_gridworth = 6

# class Water (object):
#     """docstring for ClassName"""
#     def __init__(self, arg):
#         self.total = 4800
        

