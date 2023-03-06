
class Consumable:
    def __init__(self, id, name, cost = 0, hunger_value = 0, happiness_value = 0):
        self.id = id
        self.name = name
        self.cost = cost
        self.hunger_value = hunger_value
        self.happiness_value = happiness_value

    def getCost(self):
        return self.cost
    def getName(self):
        return self.name
    def getHungerValue(self):
        return self.hunger_value
    def getHappinessValue(self):
        return self.happiness_value
    def setCost(self,value): 
        self.cost = value
    def setHunger(self,value):
        self.hunger_value = value
    def setHappiness(self,value):
        self.happiness_value = value

    def __str__(self):
        return f"{self.id}, {self.cost}"


    