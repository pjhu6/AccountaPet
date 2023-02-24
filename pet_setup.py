''' sets up all the basic set up options for the pet, contains virtual_pet '''

import datetime

class VirtualPet:
    def __init__(self, name, species, hunger=0, happiness=5, birthday=datetime.datetime.now()):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.happiness = happiness
        self.birthday = birthday

    def feed(self):
        self.hunger -= 1
        self.happiness += 1
        print(f"{self.name} has been fed!")

    def play(self):
        self.happiness += 1
        self.hunger += 1
        print(f"{self.name} had fun playing!")

    def calculate_happiness(self):
        pass

    def __str__(self):
        return f"{self.name} ({self.species}) - Hunger: {self.hunger}, Happiness: {self.happiness}"