class UserStatus:
    def __init__(self, pet_status, items, recommendations):
        self.pet_status = pet_status
        self.items = items
        self.recommendations = recommendations

    def to_dict(self):
        return {
            'pet_status': self.pet_status.to_dict(),
            'items': [item.to_dict() for item in self.items],
            'recommendations': [reco_item.to_dict() for reco_item in self.recommendations]
        }

class PetStatus:
    def __init__(self, pet_name, img_name, status_name = 'None', effect_value = 0, pet_health = 100):
        self.pet_name = pet_name
        self.img_name = img_name
        self.status_name = status_name
        self.effect_value = effect_value
        self.pet_health = pet_health

    def to_dict(self):
        return {
            'pet_name': self.pet_name,
            'img_name': self.img_name,
            'status_name': self.status_name,
            'effect_value': self.effect_value,
            'pet_health': self.pet_health
        }
    
class Item:
    def __init__(self, item_id, item_name, item_amount):
        self.item_id = item_id
        self.item_name = item_name
        self.item_amount = item_amount

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'item_name': self.item_name,
            'item_amount': self.item_amount
        }