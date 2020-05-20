# -*- coding: cp936 -*-
class GameObject:
    def __init__(self,name):
        self.name = name

    def pickUp(self, player):
        pass
        #put code here to add the object
        #to the player's collection

class Coin(GameObject):    #继承GameObject
    def __init__(self, value):
        GameObject.__init__(self,"coin")
        self.value = value

    def spend(self, buyer, seller):
        pass
        #put code here to remove the coin
        #from the buyer's money and
        #add it to the seller's money
