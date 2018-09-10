import glob
import numpy as np
import random as rand
from Amount import *
from recipe import *
from Ingredient import *

inspiring_ingredients = {}



def read_files(folder):
    txt_files = glob.glob(folder + "/*.txt")
    return_recipes = []
    for i in range(len(txt_files)):
        with open(txt_files[i]) as f:
            temp = f.readlines()
            ingredient_temp = []
            for line in temp:
                line_split = line.split(" ", 2)
                line_split[2] = line_split[2][:-1]
                amount_temp = Amount(float(line_split[0]),line_split[1])
                ingredient_temp.append(Ingredient(line_split[2],amount_temp))
                inspiring_ingredients[line_split[2]] = 1 #creating the inspiring set list of all possible ingredients
            recipe_temp = Recipe(ingredient_temp)
            recipe_temp.name_recipe()
            return_recipes.append(recipe_temp)
    return return_recipes

"""
The selection_probability_array function takes an array of recipes and generates
an array of selection probabilities that correspond to the recipes based on the
aesthetic filter of recipe size.
    Input:
        breeding_pool -> the array of parent recipes
    Output:
        probs_array -> the array of each recipe's probability of being selected
"""
def selection_probability_array(breeding_pool):
    probs_array = []
    accum = 0

    for x in breeding_pool:
        accum += len(x.ingredients)
        probs_array.append(accum)

    return probs_array


"""
The find_probs_array_index function will carry out a binary search on
the probs_array to find the index where accum can be found. Accum will be less
than or equal to the indexed probability.
    Inputs:
        accum -> a number
        probs_array -> an array of accumulative probabilities
    Output:
        an index number

def find_probs_array_index(accum, probs_array):
    half_way = (len(probs_array) - 1) // 2
    # when only one item left, item is accum
    # return index
    if len(probs_array) == 1:
        return 0
    # when accum is greater than half_way item, recursively check right of half_way
    # return recursive index + half_way index + 1
    elif accum > probs_array[half_way]:
        return half_way + 1 + find_probs_array_index(accum,
               probs_array[half_way + 1 : len(probs_array)])
    # when accum is less than half_way item, recursively check left of half_way inclusive
    # return recursive index without modification
    else:
        return find_probs_array_index(accum,
               probs_array[0 : half_way + 1])
"""

"""
Find the index accum in a probs_array.
"""
def find_probs_array_index(accum, probs_array):
    for i in range(len(probs_array)):
        if accum <= probs_array[i]:
            return i
    return none

"""
The produce_new_generation function takes an array of recipes and an array of
each recipe's probability of being selected to generate a new generation of
offspring recipes.
    Input:
        breeding_pool -> the array of parent recipes
        probs_array -> the array of probabilities
    Output:
        new_generation -> the array of offspring recipes
"""
def produce_new_generation(breeding_pool):
    probs_array = selection_probability_array(breeding_pool)
    pool_size = len(breeding_pool)
    max_accum = probs_array[len(probs_array) - 1]
    new_generation = []
    iter = pool_size
    while iter > 0:

        # generate random number
        accum1 = rand.randint(0, max_accum) # the first probability for selection
        accum2 = rand.randint(0, max_accum) # the second probability for selection

        # find parents from accums using
        # print("parent1:", find_probs_array_index(accum1, probs_array))
        # print("parent2:", find_probs_array_index(accum2, probs_array))
        # print(len(breeding_pool))
        parent1 = Recipe(breeding_pool[find_probs_array_index(accum1, probs_array)].ingredients)
        parent2 = Recipe(breeding_pool[find_probs_array_index(accum2, probs_array)].ingredients)

        # add parents to new generation
        new_generation.append(cross_over(parent1, parent2))
        iter = iter - 1

    return new_generation

"""
The produce_new_generation function takes an array of recipes and an array of
each recipe's probability of being selected to generate a new generation of
offspring recipes.
    Input:
        breeding_pool -> the array of parent recipes
        probs_array -> the array of probabilities
    Output:
        new_generation -> the array of offspring recipes

def produce_new_generation(breeding_pool, probs_array):
    pool_size = len(breeding_pool)
    new_generation = []
    iter = pool_size
    while iter > 0:
        parent1_index = rand.randInt(0, pool_size - 1)
        while parent1_index == parent2_index:
            parent2_index = rand.randInt(0, pool_size - 1)

        parent1 = rand.randInt(0, pool_size - 1) # no selection is being done
        parent2 = rand.randInt(0, pool_size - 1) # this is random selection
        new_generation.append(cross_over(parent1, parent2))
        iter = iter - 1

    return new_generation
"""



"""
The cross_over function takes two recipes and generates an offspring. The offspring
is created by picking random a pivot point in each parent and then randomly combini-
ng a subset from each parent based on their respective pivot point.
    Inputs:
        recipe1 -> the first parent recipe
        recipe2 -> the second parent recipe
    Output:
        crossed_recipe -> the child recipe
"""
#TODO: rename vars to make type clear
def cross_over(recipe1, recipe2):
    # print("recipe1:", recipe1)
    # print("recipe2:", recipe2)
    pivot1 = rand.randint(0, len(recipe1.ingredients) - 1)      # creating random pivot indices
    pivot2 = rand.randint(0, len(recipe2.ingredients) - 1)      # for both recipe strings
    #
    # print("pivot1:", pivot1, "pivot2:", pivot2)
    # print("part1:", recipe1.ingredients[0 : pivot1], "part2:",  recipe2.ingredients[pivot2 : len(recipe2.ingredients) - 1])

    final_recipe = Recipe([])

    if rand.randint(1,3)%2 == 0:                   # if it's even then we merge left
        final_recipe.add_elements_to_ingredients(recipe1.ingredients[0 : pivot1])
        final_recipe.add_elements_to_ingredients(recipe2.ingredients[pivot2 : len(recipe2.ingredients) - 1])
    else:
        final_recipe.add_elements_to_ingredients(recipe2.ingredients[0 : pivot2])
        final_recipe.add_elements_to_ingredients(recipe1.ingredients[pivot1 : len(recipe1.ingredients) - 1])

    mutation = rand.randint(1,1000)
    if(mutation > 20):
        pass
    elif(mutation > 15):
        add_ingredient(final_recipe)
    elif(mutation > 10):
        delete_ingredient(final_recipe)
    elif(mutation > 5):
        change_ingredient(final_recipe)
    else:
        change_amount(final_recipe)


    final_recipe.combine_duplicate_ingredients()
    final_recipe.scale_to_100()
    final_recipe.name_recipe()
    return final_recipe                                  # we return the new crossover array

"""
These next four functions are used for the possible mutations
that can be applied if a mutation occurs

add_ingredient adds a random ingredient (w/ a random amount between 1-10 units)
from the inspiring set to a recipe

delete_ingredient deletes a random ingredient from a recipe

change_ingredient changes the name of an ingredient in a recipe to that of
another ingredient in the inspiring set

change_amount selects an ingredient from the recipe and changes the amount to be
anywhere from 1-30 units
"""
def add_ingredient(recipe):
    random_ingredient = random.choice(list(inspiring_ingredients))
    new_ingredient = Ingredient(random_ingredient, Amount(rand.randint(1,10),"oz"))
    recipe.add_elements_to_ingredients([new_ingredient])
    return recipe

def delete_ingredient(recipe):
    recipe.delete_random_ingredient()
    return recipe


def change_ingredient(recipe):
    random_ingredient = random.choice(list(inspiring_ingredients))
    recipe.change_random_ingredient(random_ingredient)
    return recipe

def change_amount(recipe):
    recipe.scale_random_ingredient_amount(rand.randint(1,30))
    return recipe

'''
Start of the main method:
 - reads in the inspiring set of new_recipes and sorts it by fitness
 - creates a new generation of recipes and sorts it by fitness
 - take the first half of old and new recipes to get most fit 50% from each
 - repeat for n iterations based on user input
'''

num_iterations = input("number of iterations: ")

recipes = read_files("input")
recipes = sorted(recipes, key= lambda Recipe: len(Recipe.ingredients), reverse=True)
new_recipes = produce_new_generation(recipes)
new_recipes = sorted(new_recipes, key = lambda Recipe: len(Recipe.ingredients), reverse = True)


'''

'''
next_generation_recipes = recipes[0:int(len(recipes)/2)] + new_recipes[0:int(len(new_recipes)/2)]
next_generation_recipes = sorted(next_generation_recipes, key= lambda Recipe: len(Recipe.ingredients), reverse=True)

for k in range(int(num_iterations)-1):

    new_recipes = produce_new_generation(recipes)
    new_recipes = sorted(new_recipes, key = lambda Recipe: len(Recipe.ingredients), reverse = True)
    next_generation_recipes = recipes[0:int(len(recipes)/2)] + new_recipes[0:int(len(new_recipes)/2)]
    next_generation_recipes = sorted(next_generation_recipes, key= lambda Recipe: len(Recipe.ingredients), reverse=True)

counter = 0
for recipe in next_generation_recipes:
    counter = counter + 1
    print("recipe #" + str(counter) + ":", recipe.name)
    print(recipe)
