'''
Main led tester class. 
'''
import numpy as np

class LEDTester:
    
    def __init__(self, grid_size):
        # create the grid with the given size
        self.grid = np.full((grid_size, grid_size), False)
        
    

    def process_line(self, parsed_line):
        
        numbers = parsed_line[1:]
        # first test command is valid, if not, ignore line
        if(parsed_line[0] != 'turn on' and parsed_line[0] != 'turn off' and parsed_line[0] != 'switch'):
            pass
        
        elif(parsed_line[0] == 'turn on'):
                self.turn_on(numbers)
                
            
        elif(parsed_line[0] == 'turn off'):
                self.turn_off(numbers)
                
        elif(parsed_line[0] == 'switch'):
                self.switch(numbers)
               
    
    def turn_on(self, numbers):
        row_start = min(numbers[0],numbers[2])
        row_end = max(numbers[0], numbers[2])
        col_start = min (numbers[1], numbers[3])
        col_end = max(numbers[1], numbers[3])
        
        self.grid[row_start:row_end+1, col_start:col_end+1] = True
        
    def turn_off(self, numbers):
        row_start = min(numbers[0],numbers[2])
        row_end = max(numbers[0], numbers[2])
        col_start = min (numbers[1], numbers[3])
        col_end = max(numbers[1], numbers[3])
        
        self.grid[row_start:row_end+1, col_start:col_end+1] = False
    
    def switch(self, numbers):
        row_start = min(numbers[0],numbers[2])
        row_end = max(numbers[0], numbers[2])
        col_start = min (numbers[1], numbers[3])
        col_end = max(numbers[1], numbers[3])
        
        for i in range(row_start, row_end+1):
            for j in range(col_start, col_end+1):
                if(self.grid[i][j] == False):
                    self.grid[i][j] = True
                else:
                    self.grid[i][j] = False
        
    
    
    
    def count_lights(self):
        return self.grid.sum()
        