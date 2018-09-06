import glob
import numpy as np
import random as rand
from Amount import *
from recipe import *
from Ingredient import *
txt_files = glob.glob("input/*.txt")


recipes = []

for i in range(len(txt_files)):
    with open(txt_files[i]) as f:
        temp = f.readlines()
        # print("lines", temp, "\n\n\n")
        ingredient_temp = []
        for line in temp:
            line_split = line.split(" ", 2)
            line_split[2] = line_split[2][:-1]
            # print("linesplit", line_split, "\n")
            amount_temp = Amount(float(line_split[0]),line_split[1])
            ingredient_temp.append(Ingredient(line_split[2],amount_temp))
        recipe_temp = Recipe(ingredient_temp)
        recipes.append(recipe_temp)

for recipe in recipes:
    print(recipe)
    print()

# temp = Amount(10, "oz")
# print(temp)
#
# temp2 = Ingredient("beef", temp)
# print(temp2)
#
# temp3 = Recipe([temp2])
# print(temp3)
#
# print(recipes[0])
