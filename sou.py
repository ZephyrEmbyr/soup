import glob
import numpy as np
import random as rand

txt_files = glob.glob("input/*.txt")












def crossover(recipe1, recipe2):
    pivot1 = rand.randInt(1, len(recipe1))
    pivot2 = rand.randInt(1, len(recipe2))
