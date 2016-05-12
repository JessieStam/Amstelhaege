#PLEASEEEEE

import math
import random
import numpy as np
import visual_amstelhaege
# import pygame


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
    def __str__(self):
        return str(self.x) + ", " + str(self.y)

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
        self.grid = np.zeros((320,300), dtype = int)

        
        # code below is filling grid using iterations, in case the above doesn't work
            # self.grid = []
            # row = []
            # for i in range(0, 150):
            #   row.append(0)

            # for j in range (0, 160):
            #   self.grid.append(row)
                
        #for index, value in enumerate(grid) (store occupied locations in dictionary, we're not sure if we will use this yet)
        self.occupied = []


    # def getOccupiedGround(self):
    #     """
    #     Returns occupied coordinates.
    #     """
    #     return self.occupied

    def setOccupiedGround(self, pos_top, pos_bottom, tilevalue):
        """
        Places the houses onto the map.
        Changes the integer values for occupied positions from 0 to an interger
        from 1 to 5.

        pos: a Position object.
        housetype: a house of certain size.
        tilevalue: value of a house: 2 for small house, 3 for medium house, 
        4 for large house, 1 for free space, 5 for water.
        """

        # for i in range (pos_top.x, pos_bottom.x + 1):
        #     #column
        #     for j in range(pos_top.y, pos_bottom.y + 1):
        #         self.grid[i][j] = tilevalue

        # change value of grid positions
        self.grid[pos_top.y: pos_bottom.y + 1, pos_top.x: pos_bottom.x + 1] = tilevalue
       
        # dictionary update
        pos_top = Position(pos_top.x, pos_top.y)
        self.occupied.append(pos_top)

        #10 want small house neemt 12 coords in beslag
        # if self.housetype == "small":
        #     self.occupied[self.pos] = SmallHouse()
        # elif self.housetype == "medium":
        #     self.occupied.update({self.pos:})
        # else self.housetype == "large":
        #     self.occupied.update({self.pos:})


        # if self.housetype == "small":
        #     self.grid



    def isGroundOccupied(self, x, y, width, depth, free_m2):
        # MOET HOUSETYPE WORDEN MEEGEGEVEN????? Jessie denkt van niet,
        # want hij geeft true of false terug, niet de waarde van de tegel

        # Caitlin, moet pos niet gedefinieerd worden als zijnde een positie? Want nu kun je toch net zo goed "poep" schrijven eigenlijk? Hoe weet hij dat
        # het een pos is?

        freespace_pos = free_m2
        true_counter = 0

        for pos in self.occupied:
            # if self.grid[pos.y, pos.x - 12] == 1:
            #     freespace_pos =  12
            # if self.grid[pos.y, pos.x - 6] == 1 and 6 > freespace_pos:
            #     freespace_pos = 6
            # if self.grid[pos.y, pos.x - 4] == 1 and 4 > freespace_pos:
            #     freespace_pos = 4

            for i in range(x, (x + width)):
                for j in range (y, (y + depth)):
                    if self.grid[j, i] > 0:
                        if (self.grid[y, x - free_m2]) > 1 or (self.d[y, x + free_m2] > 1):
                            if (self.grid[y - free_m2, x]) > 1 or (self.d[y + free_m2, x] > 1):
                                return True
                        
            # for k in range(x, (x + width + freespace_pos)):
            #     for l in range (y, (y + depth + freespace_pos)):
            #         if self.grid[l, k] > 1:
            #             true_counter += 1
        return False




    def getRandomPosition(self, width, depth):
        """
        Return a random position inside the room.
        returns: a Position object.
        """

        # get random numbers to generate a random position in room
        # constraints in de functie waar hij aangeroepen wordt
        # minus 18 because every house extands 18 tiles to the right and down (16m + 2m free space)
        # used to be 23, dont know why
        ran_x = random.randint(0 + 12, width - 28) 
        ran_y = random.randint(0 + 12, depth - 28)
        ran_pos = Position(ran_x, ran_y)
        return ran_pos

    #def amountGroundFree(self):
        

        # WAAROM MOET ALLES EERST EEN WAARDE KRIJGEN???
        # begin_col_hor = 0
        # begin_row_hor = 0
        # end_col_hor = 0
        # end_row_hor = 0
        # begin_col_ver = 0
        # begin_row_ver = 0
        # end_col_ver = 0
        # end_row_ver = 0
        # begin_pos = Position(0,0)
        # house = True
        # # 300 x 320 grootte grid
        # for col in range(0, 13):
        #     house == True
        #     for row in range (0, 13):
        #         # if tile has a house value and tile left and tile above position have no house value, 
        #         # initialize starting position
        #         if self.grid[col, row] > 1 and (self.grid[col, row - 1] < 2 or self.grid[col - 1, row] < 2):
        #             begin_pos = (col, row)

        #         # if tile has a house value, and tile right of position has no house value or tile below 
        #         # position has no house value, initialize start column and start row and define end of house
        #         if self.grid[col, row] > 1 and self.grid[col, row + 1] < 2 or self.grid[col + 1, row] < 2:
        #             begin_col_hor = col
        #             begin_row_hor = row
        #             house = False
        #             print "here"
        #         # if house is false, and tile right of position has a house value or tile below
        #         # position has a house value, and positions to end of house
        #         elif house == False and self.grid[col, row + 1] > 1 and self.grid[col, row + 2] > 1:
        #             end_col_hor = col + 1
        #             end_row_hor = row + 1
        #             house = True 
        #             if self.occupied.get(begin_pos, -1) > (end_row_hor - begin_row_hor):
        #                 self.occupied[begin_pos] = (end_row_hor - begin_row_hor)
        #                 print self.occupied[begin_pos]

        #         # same function for when house is rotated???
        #         if self.grid[col, row] > 1 and self.grid[col + 1, row] < 2:
        #             begin_col_ver = col
        #             begin_row_ver = row
        #             house = False
        #         elif house == False and self.grid[col + 1, row] > 1 and self.grid[col + 2, row] > 1:
        #             end_col_ver = col + 1
        #             end_row_ver = row + 1
        #             house = True 
        #             if self.occupied.get(begin_pos, -1) > (end_row_ver - begin_row_ver):
        #                 self.occupied[begin_pos] = (end_row_ver - begin_row_ver)
        #                 print self.occupied[begin_pos]
                                           



# pos_linkhoek = Position(1, 2)
# pos_rechthoek = Position(4, 4)
# num_tilevalue = 3 

# ground_test.setOccupiedGround(pos_linkhoek, pos_rechthoek, num_tilevalue)

# pos_linkhoek = Position(8, 3)
# pos_rechthoek = Position(13, 7)

# ground_test.setOccupiedGround(pos_linkhoek, pos_rechthoek, num_tilevalue)

# for pos in ground_test.occupied:
#     print pos

# print ground_test.grid
# print ground_test.isGroundOccupied(1, 2, 2, 3)
# print ground_test.isGroundOccupied(0, 0, 3, 1)

# ground_test.amountGroundFree()






class House (object):
    """
    Basis for three house types and water
    """
    def __init__(self):
        """
        FieldMap: a class for the grid
        house_freem2: an int: obligatory free space aroud a house 
        """
        self.field = FieldMap()
        # this used to be 2, but it is 2m per side of the house, so 4?
        # and is this even 4, because it differs per house right?
        self.house_freem2 = 4
        pos = field.getRandomPosition()
        free_m2_tilevalue = 1
    # FUNCTIES DIE VOOR ALLE HUIZEN GELDEN

    def getHousePosition(self):
        return self.pos

    def setHousePosition(self):

        #     def isGroundOccupied(self, x, y, width, depth):
        # # MOET HOUSETYPE WORDEN MEEGEGEVEN????? Jessie denkt van niet,
        # # want hij geeft true of false terug, niet de waarde van de tegel
        # for pos in self.occupied:
        #     for i in range(x, (x + width)):
        #         for j in range (y, (y + depth)):
        #             if pos[0] == i and pos[1] == j:
        #                 return True

        # return False
        # get random pos to set house
        self.pos = self.field.getRandomPosition(300, 320)
        # check if ground for house and obligatory free m2 is already occupied
        
        # ik heb hier de - self.free_m2 die van x en y zijn afgetrokken weggehaald (zoals hieronder in de comment), want ze kunnen vrije ruimte delen
        # while (self.field.isGroundOccupied((self.pos.x), (self.pos.y), (self.width + self.free_m2), (self.depth + self.free_m2))):
        #     self.pos = self.field.getRandomPosition(300, 320)

        while (self.field.isGroundOccupied((self.pos.x - self.free_m2), (self.pos.y - self.free_m2), self.width, self.depth, self.free_m2)):
            self.pos = self.field.getRandomPosition(300, 320)
            print "occupied", self.pos.x, self.pos.y

        # calculate pos of left corner of house + obligatory free m2
        self.pos_top_m2 = Position((self.pos.x - self.free_m2), (self.pos.y - self.free_m2))
        print "self.pos_top_m2", self.pos_top_m2
        # calculate pos of right corner of house
        self.pos_bottom = Position((self.pos.x + self.width), (self.pos.y + self.depth))
        print "self.pos_bottom", self.pos_bottom
        # calculate pos of richt corner of house + obligatory free m2
        self.pos_bottom_m2 = Position((self.pos_bottom.x + self.free_m2), (self.pos_bottom.y + self.free_m2))
        print "self.pos_bottom_m2", self.pos_bottom_m2

        # set ground of house + obligatory free m2
        # maybe add the value that the tiles should have
        # set occupied ground veranderd de tegelwaarde in tilevalue for free_m2
        self.field.setOccupiedGround(self.pos_top_m2, self.pos_bottom_m2, 1)
        # overwrite ground of house where only the house is at different value
        # OF MOET DEZE LAATSTE IN DE HOUSE CLASS ZELF????
        self.field.setOccupiedGround(self.pos, self.pos_bottom, self.house_tilevalue)

#checken hoeveel meter huis tot andere huizen

# checken of er al een huis staat <--- field

#init van super aanroepen <--- googlen (house)

class SmallHouse (House):
    def __init__(self, field):
        self.field = field
        self.width = 16
        self.depth = 16
        self.free_m2 = 4
        self.house_tilevalue = 2

class MediumHouse (House):
    def __init__(self, field):
        self.field = field
        self.width = 20
        self.depth = 15
        self.free_m2 = 6
        self.house_tilevalue = 3

class LargeHouse (House):
    def __init__(self, field):
        self.field = field
        self.width = 22
        self.depth = 21
        self.free_m2 = 12
        self.house_tilevalue = 4

# class Water (object):
#     """docstring for ClassName"""
#     def __init__(self, arg):
#         self.total = 4800

field = FieldMap()
houselist = []
for i in range(0, 10):
    houselist.append(SmallHouse(field))
    houselist.append(MediumHouse(field))
    houselist.append(LargeHouse(field))
for house in houselist:
    house.setHousePosition()

for poss in field.occupied:

    print poss.x
    print poss.y

visual_amstelhaege.runProgram(field.grid)               