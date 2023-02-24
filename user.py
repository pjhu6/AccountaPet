import json
import virtual_pet
import datetime

class User:
    def __init__(self, user_id, points=0, consumables=[], pet=None):
        self.user_id = user_id
        self.points = points
        self.consumables = consumables
        self.pet = pet

        self.to_json(filepath=f'{self.user_id}.json')


    def purchase(self, consumable):
        points -= consumable.cost
        self.consumables.append(consumable)

        self.to_json(filepath=f'{self.user_id}.json')
    

    def feed(self, consumable):
        self.pet.hunger -= consumable.hunger_value
        self.pet.happiness += consumable.happiness_value
        self.to_json(filepath=f'{self.user_id}.json')
        print(f"{self.pet.name} has been fed!")
        return self.statusToJson()


    def play(self):
        self.pet.happiness += 1
        self.pet.hunger += 1
        self.to_json(filepath=f'{self.user_id}.json')
        print(f"{self.name} had fun playing!")


    def recommend(self):
        # TODO: some search algorithm
        return "Dog food"


    def calculate_happiness(self):
        pass


    def statusToJson(self):
        return json.dumps({
            "hunger": self.pet.hunger,
            "happiness": self.pet.happiness,
        })


    def to_dict(self):
        data = {
            "user_id": self.user_id,
            "points": self.points,
            "consumables": self.consumables,
            "pet": None
        }
        if self.pet:
            pet = self.pet
            data["pet"] = {
                "name": pet.name,
                "species": pet.species,
                "hunger": pet.hunger,
                "happiness": pet.happiness,
                "birthday": pet.birthday.strftime("%Y-%m-%d")
            }
        return data


    def to_json(self, filepath):
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f, indent=4)


    @classmethod
    def from_dict(cls, data):
        user_id = data["user_id"]
        points = data["points"]
        consumables = data["consumables"]
        pet_data = data["pet"]
        pet = None
        if pet_data:
            name = pet_data["name"]
            species = pet_data["species"]
            hunger = pet_data["hunger"]
            happiness = pet_data["happiness"]
            birthday = datetime.datetime.strptime(pet_data["birthday"], "%Y-%m-%d")
            pet = virtual_pet.VirtualPet(name, species, hunger, happiness, birthday)
            
        return cls(user_id, points=points, consumables=consumables, pet=pet)


    @classmethod
    def from_json(cls, filepath):
        with open(filepath, "r") as f:
            data = json.load(f)
        return cls.from_dict(data)

