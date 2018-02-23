# -*- coding: utf-8 -*-
import numpy as np

# going to try using numpy array with zeros and ones 
# https://stackoverflow.com/questions/21174961/how-to-create-a-numpy-array-of-all-true-or-all-false
# leds initialised to false/off
L = 10

grid = np.full((L, L), False)

print(grid)