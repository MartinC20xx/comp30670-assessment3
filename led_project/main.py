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

#actually, setup.py 'should install a script which reads input from a file'


L = 8 # test var for size. given in the first line of the input file

grid = np.full((L, L), False)

# two formats for selecting data from multi-d arr. double bracket and single bracket with comma.
# single bracket recommended in tutorial. 
# [:,:] rows, cols
# therefore, can have (0,0 through 999,0) == [0:999, 0:1] or [0:999, 0]
# i think i can do something like grid[0:999, 0:1] = True
# can change multiple values using slice notation and = to assign


print(grid.dtype, '\n')
print(grid, '\n')
grid[0:8,0:1] = True
print(grid)