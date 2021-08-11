from weapon import Weapon


class Robot:
    #Constructor
    def __init__(self,name):
        self.name = name
        self.health = 250
        self.weapon = Weapon

    #Method
    def attack(self,dinosaur):void
