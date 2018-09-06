import random


class Recipe:
    def __init__(self, ingredients):
        self.ingredients = ingredients

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


    # set weight to 100 oz
    def normalize_weights(self):
        oz_counter = 0

        for ingredient in self.ingredients:
            oz_counter += ingredient.amount.get_quantity

        scale = 100 / oz_counter

        new_total_weight = 0
        for ingredient in self.ingredients:
            prev_quantity = ingredient.amount.get_quantity
            self.ingredients.amount.replace_quantity(scale * prev_quantity)
            new_total_weight += scale * prev_quantity

        if new_total_weight == 100:
            print('Success!')
