class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 200
        self.energy = 100
        
    def attack(self, robot): 
        robot.health -= self.attack_power
        self.energy -= 10 
        print(f"{self.name} attacks {robot.name}. {self.attack_power} damage dealt. Remaining health is {robot.health}.")   
        
        

