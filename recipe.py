import random
from Ingredient import *
from Amount import *


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
    # def normalize_weights(self):
    #     oz_counter = 0
    #
    #     for ingredient in self.ingredients:
    #         oz_counter += ingredient.amount.quantity
    #
    #     scale = 100 / oz_counter
    #
    #     new_total_weight = 0
    #     for ingredient in self.ingredients:
    #         prev_quantity = ingredient.amount.quantity
    #         self.ingredients.amount.replace_quantity(scale * prev_quantity)
    #         new_total_weight += scale * prev_quantity
    #
    #     if new_total_weight == 100:
    #         print('Success!')

    def combine_duplicate_ingredients(self):
        ingredients_dict = {}
        for ingredient in self.ingredients:
            # ingredient_dict[ingredient.name] = (ingredient_dict.get(ingredient.name, 0) + ingredient.amount.quantity)
            if ingredient in ingredients_dict:
                ingredients_dict[ingredient.name] += ingredient.amount.quantity
            else:
                ingredients_dict[ingredient.name] = ingredient.amount.quantity
        ingredient_arr = []
        for key in ingredients_dict:
            ingredient_arr.append(Ingredient(key, Amount(ingredients_dict[key], "oz")))
        self.ingredients = ingredient_arr

    def add_elements_to_ingredients(self, new_arr):
        self.ingredients = self.ingredients + new_arr
        return

    def scale_to_100(self):
        total = 0
        for ingredient in self.ingredients:
            total = total + ingredient.amount.quantity
        scale_factor = 100 / total
        for k in range(len(self.ingredients)):
            self.ingredients[k].amount.quantity = self.ingredients[k].amount.quantity * scale_factor




    def __str__(self):
        temp = ""
        for ingredient in self.ingredients:
            temp = temp + str(ingredient) + "\n"
        return temp;
