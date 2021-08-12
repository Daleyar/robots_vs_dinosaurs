from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet
        self.herd = Herd

    def run_game(self):
        self.start_game = True
        print("**Game Starts**")

    def display_welcome(self): 
        print("Welcome to the END OF THE WORLD!")

    def battle(self,turn): 
        if(turn == 1 or turn == 3):
            self.battle = True
        elif(turn == 2 or turn == 4):
            self.battle = False
        else:
            print("Illegal turn")

    def dino_turn(self, dinosaur):
        if(self.battle == True):
            print("It's " + dinosaur.name + "'s " + "turn to FIGHT!")
        else:
            print(dinosaur.name + " is waiting for it's turn")
    def robo_turn(self, robot): 
        if(self.battle == False):
            print("It's " + robot.name + "'s " + "turn to FIGHT!")
        else:
            print(robot.name + " is waiting for it's turn")

    def show_dino_opponent_options(self): 
        pass

    def show_robo_opponent_options(self): 
        pass

    def display_winners(self): 
        pass