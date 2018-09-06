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
        ingredient_temp = []
        for line in temp:
            line_split = line.split(" ", 2)
            line_split[2] = line_split[2][:-1]
            amount_temp = Amount(float(line_split[0]),line_split[1])
            ingredient_temp.append(Ingredient(line_split[2],amount_temp))
        recipe_temp = Recipe(ingredient_temp)
        recipes.append(recipe_temp)

"""
The selection_probability_array function takes an array of recipes and generates
an array of selection probabilities that correspond to the recipes based on the
aesthetic filter of recipe size.
    Input:
        breeding_pool -> the array of parent recipes
    Output:
        probs_array -> the array of each recipe's probability of being selected
"""
def selection_probability_array(breeding_pool)
    probs_array = []
    num_ingredients = 0
    for x in range(breeding_pool):
        num_ingredients += len(breeding_pool[x])

    for x in range(breeding_pool):
        probs_array.append(float(len(breeding_pool[x]) / num_ingredients))

    return probs_array


"""
The produce_new_generation function takes an array of recipes and generates an
new generation of offspring recipes based on the previous generation
(breeding_pool).
    Input:
        breeding_pool -> the array of parent recipes
    Output:
        new_generation -> the array of offspring recipes
"""
def produce_new_generation(breeding_pool):
    pool_size = len(breeding_pool)
    new_generation = []
    iter = pool_size
    while iter > 0:
        parent1 = rand.randInt(0, len[breeding_pool] - 1) # no selection is being done
        parent2 = rand.randInt(0, len[breeding_pool] - 1) # this is random selection
        new_generation.append(cross_over(parent1, parent2))
        iter--

    return new_generation



"""
The cross_over function takes two recipes and generates an offspring. The offspring
is created by picking random a pivot point in each parent and then randomly combini-
ng a subset from each parent bsed on their respective pivot point.
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
