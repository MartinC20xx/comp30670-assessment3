# -*- coding: utf-8 -*-
import numpy as np

# going to try using numpy array with zeros and ones 
# https://stackoverflow.com/questions/21174961/how-to-create-a-numpy-array-of-all-true-or-all-false
# leds initialised to false/off

input_file = 0 # placeholder for var for input file

#with open(input_file) as f:
    #for line in f:
        #method here for processing each line
        # look back at data analysis notes for open() file stuff.



L = 10 # test var for size. given in the first line of the input file

grid = np.full((L, L), False)


print(grid.dtype)
print(grid)