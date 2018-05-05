"""
ITP 115, SP18 Final project
Student: Zhonghao SHI
SID: 5595127131
"""
from Menu import Menu
from Diner import Diner

class Waiter(object):

    # constructor for the Waiter object
    def __init__(self,menu):
        self.__menu = menu
        self.__diners = []

    # add a new diner
    def addDiner(self, new_diner):
        self.__diners.append(new_diner)

    # return the number of diners for this waiter
    def getNumDiners(self):
        return len(self.__diners)

    # print out the status of this diner
    def printDinerStatuses(self):
        for i in range(5):
            print("Diners who are " + Diner.STATUSES[i] + ":" )
            for diner in self.__diners:
                if(diner.status_getter()== i):
                    print("    " , end="")
                    print(diner)

    # take orders for the diners with the status of ordering
    def takeOrders(self):
        for diner in self.__diners:
            if(diner.status_getter() == 1):
                order_list = []
                for i in range(4):

                    self.__menu.printMenuItemsByType(Menu.MENU_ITEM_TYPES[i])
                    print(diner.getName() + ", please select a " + Menu.MENU_ITEM_TYPES[i] + " menu item number.")
                    checker = True
                    num = -1
                    while(checker):
                        num = input()
                        num = int(num)
                        if(type(num) == int and num < self.__menu.getNumMenuItemsByType(Menu.MENU_ITEM_TYPES[i]) and num >= 0):
                            checker = False

                    order_list.append(self.__menu.getMenuItem(Menu.MENU_ITEM_TYPES[i],num))

                diner.order_setter(order_list)
                print()
                print(diner.getName() + " ordered:")
                diner.printOrder()
                print()
    # calculate the total check for the diners with the status of paying
    def ringUpDiners(self):
        for diner in self.__diners:
            if (diner.status_getter() == 3):
                print(diner.getName() + ", your meal cost " + str(diner.calculateMealCost()))


    # say goodbye and remove it for the diners with the status of leaving
    def removeDoneDiners(self):
        for diner in self.__diners:
            if (diner.status_getter() == 4):
                print(diner.getName() + ", thank you for dining with us! Come again soon!")


        for i in reversed(range(len(self.__diners))):
            if(self.__diners[i].status_getter() == 4):
                del self.__diners[i]

    # advance the process for the simulation
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for diner in self.__diners:
            diner.updateStatus()

















