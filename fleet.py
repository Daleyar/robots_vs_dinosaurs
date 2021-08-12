from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.armory = []
        self.weapon_smith()
        self.create_fleet()

    def weapon_smith(self):
        weapon1 = Weapon("Heavy Flamer Gun", 50)
        weapon2 = Weapon("Laser Assault Rifle", 50)
        weapon3 = Weapon("Pulse Rifle", 50)
        self.armory.append(weapon1)
        self.armory.append(weapon2)
        self.armory.append(weapon3)

    def create_fleet(self):
        robot1 = Robot('SlaveBot','Heavy Flamer Gun')
        robot2 = Robot('Assaultron','Laser Assault Rifle')
        robot3 = Robot('Behemoth','Heavy Flamer Gun')
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)