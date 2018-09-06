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



def produce_new_generation(breeding_pool):
    pool_size = len(breeding_pool)
    parent1 = rand.randInt(0, len[breeding_pool] - 1)
    parent2 = rand.randInt(0, len[breeding_pool] - 1)
    new_generation = []
    iter = pool_size
    while(it)





"""
The cross_over funciton takes two recipes and generates an offspring. The offspring
is created by picking random pivot points in each parent and then randomly combini-
ng
    Inputs:
            recipe1 -> the first parent recipe
            recipe2 -> the second parent recipe
    Output:
            crossed_recipe -> the child recipe
"""
def cross_over(recipe1, recipe2):
    pivot1 = rand.randInt(1, len(recipe1)-1)      # creating random pivot indices
    pivot2 = rand.randInt(1, len(recipe2)-1)      # for both recipe strings

    if rand.randInt() % 2 == 0:                 # if it's even then we merge left
        crossed_recipe = recipe1[1:pivot1].append(# subset of recipe 1 with the right
        recipe2[pivot2:len(recipe2) - 1])       # subset of recipe 2 based on their pivots
    else:
        crossed_recipe = recipe2[1:pivot2].append(# left subset of recipe 2 with
        recipe1[pivot1:len(recipe1) - 1])       # the right subset of recipe 1

return crossed_recipe                             # we return the new crossover array
