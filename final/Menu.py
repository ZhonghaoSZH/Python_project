"""
ITP 115, SP18 Final project
Student: Zhonghao SHI
SID: 5595127131
"""

from MenuItem import MenuItem

class Menu(object):

    #class variable
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    #constructor for the Menu object
    def __init__(self,csv_path):
        drink_list = []
        appetizer_list = []
        entree_list = []
        dessert_list = []
        self.__menuItemDictionary = {"Drink": drink_list, "Appetizer": appetizer_list, "Entree": entree_list, "Dessert": dessert_list}
        fileIn = open(csv_path, "r")
        for line in fileIn:
            line = line.split(",")
            new_Item = MenuItem(line[0], line[1],float(line[2]),line[3])
            self.__menuItemDictionary[line[1]].append(new_Item)

    # get the correct MenuItem from the dictionary using its type and index position
    def getMenuItem(self, dish_type, dish_index ):
        return self.__menuItemDictionary[dish_type][dish_index]

    # print the menu by type
    def printMenuItemsByType(self, dish_type):
        print("------" + dish_type + "------")
        index = 0
        for item in self.__menuItemDictionary[dish_type]:
            print(str(index) + ")  ", end="")
            print(item, end="")
            index += 1
    # print the number of items in the specific type
    def getNumMenuItemsByType(self,dish_type):
        return len(self.__menuItemDictionary[dish_type])







