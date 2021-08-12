class Robot:
    def __init__(self,name,weapon):
        self.name = name
        self.health = 250
        self.weapon = weapon
        self.power = 100

    def attack(self,dinosaur): 
        dinosaur.health -= self.weapon.attack_power
        self.power -= 10
        print(f"{self.name} attacks {dinosaur.name} with {self.weapon.name}. {self.weapon.attack_power} damage dealt. Remaining health is {dinosaur.health}.") 
        

