class Computer:

    def __init__ (self):
        self.__maxprice = 679

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice)) 

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()


c.maxprice = 1200
c.sell()

c.setMaxPrice(1200)
c.sell()

