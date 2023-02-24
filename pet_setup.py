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

        self.saveToJson()

    def feed(self):
        self.hunger -= 1
        self.happiness += 1
        self.saveToJson()
        print(f"{self.name} has been fed!")

    def play(self):
        self.happiness += 1
        self.hunger += 1
        self.saveToJson()
        print(f"{self.name} had fun playing!")

    def calculate_happiness(self):
        pass

    def getAge(self):
        today = datetime.datetime.now()
        delta = today - self.birthday
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30
        return f"{years} years {months} months {days} days old"
    
    def statusToJson(self):
        return json.dumps({
            "hunger": self.hunger,
            "happiness": self.happiness,
        })

    def saveToJson(self, fileName="pet.json"):
        pet_dict = {
            "name": self.name,
            "species": self.species,
            "hunger": self.hunger,
            "happiness": self.happiness,
            "birthday": self.birthday.strftime("%Y-%m-%d")
        }
        with open(fileName, "w") as f:
            json.dump(pet_dict, f)

    def __str__(self):
        return f"{self.name} ({self.species}) - Hunger: {self.hunger}, Happiness: {self.happiness}"

def readFromJson(fileName="pet.json"):
    with open(fileName, "r") as f:
        pet_dict = json.load(f)
    
    pet = VirtualPet(
        pet_dict["name"],
        pet_dict["species"],
        pet_dict["hunger"],
        pet_dict["happiness"],
        datetime.datetime.strptime(pet_dict["birthday"], "%Y-%m-%d")
    )
    return pet