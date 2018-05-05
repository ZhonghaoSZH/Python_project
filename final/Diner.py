"""
ITP 115, SP18 Final project
Student: Zhonghao SHI
SID: 5595127131
"""

from MenuItem import MenuItem

class Diner(object):

    # class variable
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    # constructor for the Diner object
    def __init__(self,diner_name):
        self.__name = diner_name
        self.__order = []
        self.__status = 0

    # getter for the name
    def getName(self):
        return self.__name

    # getter for the order
    def order_getter(self):
        return self.__order

    # getter for the status
    def status_getter(self):
        return self.__status

    # setter for the name
    def name_setter(self,new_name):
        self.__name = new_name

    # setter for the order
    def order_setter(self,new_order):
        self.__order = new_order

    # setter for the status
    def status_setter(self,new_status):
        self.__status = new_status

    # increment the status by one
    def updateStatus(self):
        self.__status += 1

    # print out the order for this diner
    def printOrder(self):
        for item in self.__order:
            print("-" , end="")
            print(item, end="")

    # print out the total cost for the diner
    def calculateMealCost(self):
        total_cost = 0.0
        for item in self.__order:
            total_cost += item.price_getter()
        return "%.2f" % round(total_cost,2)

    # __str__ for Diner class
    def __str__(self):
        return self.__name + " is currently " +  self.STATUSES[self.__status]






