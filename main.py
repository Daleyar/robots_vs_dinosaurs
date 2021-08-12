# Imports:
from robot import Robot
from weapon import Weapon
from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet

# Instaniation of Objects
robot_raiders_weapon = Weapon('Heavy Flamer Gun', 50)
robot_raiders_weapon2 = Weapon('Laser Assault Rifle', 50)
robot_raiders0 = Robot('SlaveBot', robot_raiders_weapon)
robot_raiders1 = Robot('Assaultron', robot_raiders_weapon2)
robot_raiders2 = Robot('Behemoth', robot_raiders_weapon)
dino_warriors0 = Dinosaur('Slag', 35)
dino_warriors1 = Dinosaur('Sludge', 35)
dino_warriors2 = Dinosaur('Snarl', 35)
team_dino = Herd()
team_robo = Fleet()

# Execution of Object Methods
team_dino.create_herd(dino_warriors0)
team_dino.create_herd(dino_warriors1)
team_dino.create_herd(dino_warriors2)
team_robo.create_fleet(robot_raiders0)
team_robo.create_fleet(robot_raiders1)
team_robo.create_fleet(robot_raiders2)

print(robot_raiders2.weapon)