''' sets up all the basic set up options for the pet, contains virtual_pet '''

import datetime
import json


class VirtualPet:
    def __init__(self, name, species, hunger=0, happiness=5, birthday=datetime.datetime.now()):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.happiness = happiness
        self.birthday = birthday

    def getAge(self):
        today = datetime.datetime.now()
        delta = today - self.birthday
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30
        return f"{years} years {months} months {days} days old"

    def __str__(self):
        return f"{self.name} ({self.species}) - Hunger: {self.hunger}, Happiness: {self.happiness}"