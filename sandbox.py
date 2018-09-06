import glob
import numpy as np
import random as rand

txt_files = glob.glob("input/*.txt")

print(len(txt_files))

recipes = []

for i in range(len(txt_files)):
    with open(txt_files[i]) as f:
        recipes.append(f.readlines())

recipes_split = []

for recipe in recipes:
    recipe_temp = []
    for line in recipe:
        line_split = line.split(" ", 2)
        line_split[2] = line_split[2][:-1]
        recipe_temp.append(line_split)
    recipes_split.append(recipe_temp)


for recipe in recipes_split:
    print(recipe)
    print()
