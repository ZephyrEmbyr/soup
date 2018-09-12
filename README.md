Party Quest 1: Let's Get Cooking -- by Team Tēm
Team Tēm: Kevin Chen, Javier Najera, James Wang, Alex Weinberger
--------------------------------------------------------------------------------
Our program, sou.py, is a genetic algorithm that generates soup recipes based on
a simplified version of Morris et al.'s 2012 PIERRE. It makes new recipes from
an inspirational set by crossing over recipes at 'random' (see Crossover
section). Every new recipe may be slightly changed before being added to the new
pool (see Mutation section). Each iteration returns a final pool of recipes
through cherrypicking the new and old pool for the 'fittest' recipes (see
Selection section). And, of course, these recipes have names (see Naming
section).
Python version 3.6 or higher.
Module Dependencies:
  - random
  - glob
  - numpy
--------------------------------------------------------------------------------
Basic set up:
  - Make sure that Amount.py, Ingredient.py, recipe.py, sou.py, and a file of
    recipe texts named input are in a single location.
  - Run sou.py.
What happens in a run of sou.py:
  1.You will be prompted to input a number of desired iterations. This is the
    number of times that a new and fitter recipe pool will be generated. The
    more iterations, the fitter the final recipe pool will be.
  2.The program will read the files in the folder "input", converting each text
    file to a recipe object of Ingredient objects and Amount objects, then
    adding all the recipe objects into a list to form the inspirational recipe
    pool. The pool is then sorted by fitness.
  3.With the inspirational recipe pool, a new generation is produced. For each
    recipe in the new generation, two parent recipes are chosen by weighted
    probability from the set of inspirational recipes based on each parent
    recipe's fitness. The breeding process crosses over the two parent recipes
    from the set to form a child recipe. When a list of child recipes equal in
    size to the inspirational set is populated, it is returned and then sorted.
  4.The fittest half of both the inspirational list and the new generation list
    are combined into a single resultant list of crème de la crème recipes,
    which is then sorted.
  5.Steps 3 and 4 are repeated for the number of desired iterations. (Except,
    each subsequent iteration will use the previous iteration's list of crème de
    la crème recipes as its inspirational pool.) <-- not included.
  6.Each recipe in the final list is printed.
Crossover:
  - This action takes two parent recipes to create a child recipe.
  - An index is randomly selected in each parent recipe's list of ingredients as
    their respective pivot point.
  - Both of the parent recipes are split into two on their unique pivot point.
  - Randomly, either
      - the first half of the first recipe is combined with the second half of
        the second recipe, or
      - the second half of the first recipe is combined with the first half of
        the first recipe to form the child recipe.
  - Based on chance, mutation may occur in the child recipe.
  - Duplicate ingredients in the child recipe are combined, after which all
    ingredients are scaled to sum to 100 units.
  - The child recipe is named and returned.
Mutation:
  - This action modifies a recipe without consulting parent recipes.
  - If a mutation is to occur (here set to a two percent chance), each mutation
    has an equal chance to occur.
  1.Add ingredient:
      - An ingredient from a list of inspirational ingredients is picked
        randomly
      - This ingredient is added to the recipe at a random amount between one
        and ten ounces.
  2.Delete ingredient:
      - A random ingredient is removed from the recipe.
  3.Change ingredient:
      - A random ingredient in the recipe is changed to a random ingredient
        from inspirational ingredients.
  4.Change amount:
      - A random ingredient in the recipe has its amount randomly changed to an
        amount of between 1 and 30 units.
Selection:
  - This action allows for a probabilistic favoring of fit recipes, that is,
    recipes with more ingredients.
  - An accumulative probability list of the same size as the recipe pool and
    where each index reflects the fitness of its recipe counterpart of the same
    index in the recipe pool is created.
  - Each index's entry is a number equal to the difference between the previous
    number and the number of ingredients of the respective recipe found in the
    same index in the recipe pool.
  - A random number between zero and the max accumulative probability in the
    recipe list is generated. Which ever recipe whose accumulative
    probability number is the tightest upper bound of the random number is the
    weighted randomly selected recipe.
Naming:
  - This action gives a soup recipe a representative name.
  - The soup's name is a prefix based on its ingredients appended by " soup".
      - For a recipe with no ingredients, the prefix is "null".
      - If the recipe only has one ingredient, the prefix is that ingredient.
      - Should there be more than one ingredient in the soup, the prefix is one
        of the following based on how well a randomly generated number from zero
        to one thousand can be divided by four:
            - Perfect division: ingredient1 + "-y " + ingredient2
                - e.g. "tomato-y flour soup"
            - Remainder one: "Tasty " + ingredient 1 + " and " + ingredient 2
                - e.g. "Tasty chicken breast and chicken broth soup"
            - Remainder two: "Super " + ingredient1 + "-y " + ingredient2
                - e.g. "Super dry onion soup mix-y green bean soup"
            - Else: "Momma's " + ingredient 1 + " and " + ingredient 2
                - e.g. "Momma's butter and apple soup"



