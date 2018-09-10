import random
from Ingredient import *
from Amount import *


class Recipe:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.name = ""

    # pick a random ingredient and change the amount of that ingredient by a given scale
    def scale_random_ingredient_amount(self, change_factor):
        length = len(self.ingredients)
        if len(self.ingredients) == 0:
            return;
        elif len(self.ingredients) <= 1:
            random_index = 0
        else:
            random_index = random.randint(0, length-1)

        curr_quantity = self.ingredients[random_index].amount.quantity

        self.ingredients[random_index].amount.replace_quantity(curr_quantity * change_factor)

        return curr_quantity * change_factor

    # delete a random ingredient, return void
    def delete_random_ingredient(self):
        length = len(self.ingredients)
        if len(self.ingredients) == 0:
            return
        if len(self.ingredients) <= 1:
            random_index = 0
        else:
            random_index = random.randint(0, length-1)

        del self.ingredients[random_index]

        return

    def change_random_ingredient(self, new_name):
        if len(self.ingredients) == 0:
            return
        if len(self.ingredients) <= 1:
            random_index = 0
        else:
            random_index = random.randint(0,len(self.ingredients)-1)
        temp = self.ingredients[random_index]
        self.ingredients[random_index] = Ingredient(new_name, temp.amount)


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
        if(total == 0):
            return
        scale_factor = 100 / total
        for k in range(len(self.ingredients)):
            self.ingredients[k].amount.quantity = self.ingredients[k].amount.quantity * scale_factor

    def name_recipe(self):
        if len(self.ingredients) == 0:
            return "null soup"
        elif len(self.ingredients) == 1:
            return self.ingredients[0].name + " soup"
        else:
            arr = self.ingredients
            arr = sorted(arr, key = lambda Ingredient: Ingredient.amount.quantity, reverse = True)
            name = ""
            randint = random.randint(1, 100)
            if randint % 4 == 0:
                name = self.ingredients[0].name + "-y " + self.ingredients[1].name + " soup"
            elif randint % 4 == 1:
                name = "Tasty " + self.ingredients[0].name + " and " + self.ingredients[1].name + " soup"
            elif randint % 4 == 2:
                name = "Super " + self.ingredients[0].name + "-y " + self.ingredients[1].name + " soup"
            else:
                name = "Momma's " + self.ingredients[0].name + " and " + self.ingredients[1].name + " soup"

            self.name = name
            #select the top 2 (first 2) elements from arr -> create name
            #given x, y y-ey x soup
            #tomato, onion -> tomatoey onion soup


    def __str__(self):
        temp = ""
        for ingredient in self.ingredients:
            temp = temp + str(ingredient) + "\n"
        return temp;
