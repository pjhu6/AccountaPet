''' reccomend a food to buy based on the following criteria:
    1) Combination of pet states: search through pet critera states
                                  to find which ones apply based on set goals
    2) food available in shop
    3) current funds
'''

class PetFoodRecommendations:
    def __init__(self):
        self.food_recommendations = {
            "cat": ["dry food", "wet food", "tuna"],
            "dog": ["dry food", "wet food", "chicken", "beef"],
            "bird": ["seed mix", "fresh fruits", "vegetables"],
            "fish": ["pellets", "flakes", "frozen food"],
            "hamster": ["pellets", "fresh vegetables", "fruit"],
        }

    def get_recommendations(self, species):
        return self.food_recommendations.get(species, [])