"""
ITP 115, SP18 Final project
Student: Zhonghao SHI
SID: 5595127131
"""


class MenuItem(object):
    # Constructor for the MenuItem object
    def __init__(self,name,Dishtype,price,description):
        # private instance attributes
        self.__name = name
        self.__type = Dishtype
        self.__price = price
        self.__description = description

    # getter for the name
    def name_getter(self):
        return self.__name

    # getter for the type
    def type_getter(self):
        return self.__type

    # getter for the price
    def price_getter(self):
        return  self.__price

    #getter for the description
    def description_getter(self):
        return self.__description


    #setter for the name
    def name_setter(self, new_name):
        self.__name = new_name

    #setter for the type
    def type_setter(self, new_type):
         self.__type = new_type

    #setter for the price
    def price_setter(self, new_price):
         self.__price = new_price

    #setter for hte description
    def description_setter(self, new_des):
         self.__description = new_des

    # __str__ function for the MenuItem
    def __str__(self):
        return self.__name + "(" + self.__type + "):" + " $" + str(self.__price) + "\n" + "      " + self.__description

