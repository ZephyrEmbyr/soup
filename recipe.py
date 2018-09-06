import random


class Recipe:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __init__(self):
        self.ingredients = []

    # pick a random ingredient and change the amount of that ingredient by a given scale
    def scale_random_ingredient_amount(self, change_factor):
        length = self.ingredients.len()

        random_index = random.randint(0, length-1)

        curr_quantity = self.ingredients[random_index].amount.quantity

        self.ingredients[random_index].amount.replaceQuantity(curr_quantity * change_factor)

        return curr_quantity * change_factor

    # delete a random ingredient, return void
    def delete_random_ingredient(self):
        length = self.ingredients.len()

        random_index = random.randint(0, length-1)

        del self.ingredients[random_index]

        return