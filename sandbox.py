import glob
import numpy as np
import random as rand

txt_files = glob.glob("input/*.txt")

print(len(txt_files))

recipes = []

for i in range(len(txt_files)):
    with open(txt_files[i]) as f:
        temp = f.readlines()
        ingredient_temp = []
        for line in temp:
            line_split = line.split(" ", 2)
            line_split[2] = line_split[2][:-1]
            amount_temp = Amount(line[0],line[1])
            ingredient_temp.append(Ingredient(line[3],amount_temp))
        recipes.append(Recipe(ingredient_temp))

print(recipes)
