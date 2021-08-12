from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot1 = Robot('SlaveBot','Heavy Flamer Gun')
        robot2 = Robot('Assaultron','Laser Assault Rifle')
        robot3 = Robot('Behemoth','Heavy Flamer Gun')
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)