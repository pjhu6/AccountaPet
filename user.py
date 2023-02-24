class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.points = 0
        self.consumables = []
        self.pet = None

    def purchase(self, consumable):
        points -= consumable.cost
        self.consumables.append(consumable)