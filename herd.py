from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self): 
        dino1 = Dinosaur('Slag', 35)
        dino2 = Dinosaur('Sludge', 35)
        dino3 = Dinosaur('Snarl', 35)
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
