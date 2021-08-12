
from battlefield import Battlefield

# Instaniation of Objects
robot_raiders_weapon = Weapon('Heavy Flamer Gun', 50)
robot_raiders_weapon2 = Weapon('Laser Assault Rifle', 50)
dino_warriors0 = Dinosaur('Slag', 35)
dino_warriors1 = Dinosaur('Sludge', 35)
dino_warriors2 = Dinosaur('Snarl', 35)
team_dino = Herd()
team_robo = Fleet()
thunderdome = Battlefield()

# Execution of Object Methods
team_dino.create_herd(dino_warriors0)
team_dino.create_herd(dino_warriors1)
team_dino.create_herd(dino_warriors2)
team_robo.create_fleet(robot_raiders0)
team_robo.create_fleet(robot_raiders1)
team_robo.create_fleet(robot_raiders2)

thunderdome.run_game()
thunderdome.display_welcome()
thunderdome.battle(2)
thunderdome.dino_turn(dino_warriors0)
dino_warriors0.attack(robot_raiders0)
thunderdome.robo_turn(robot_raiders0)
robot_raiders0.attack(dino_warriors0)