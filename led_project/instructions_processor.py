'''
Currently all methods relating to instruction processing. May need refactoring.
'''




def process_line(self, grid, parsed_line):
    
    numbers = parsed_line[1:]
    # first test command is valid, if not, ignore line
    if(parsed_line[0] != 'turn on' and parsed_line[0] != 'turn off' and parsed_line[0] != 'switch'):
        pass # come back to this
    
    elif(parsed_line[0] == 'turn on'):
            turn_on(grid, numbers)
        
    elif(parsed_line[0] == 'turn off'):
            turn_off(grid, numbers)
            
    elif(parsed_line[0] == 'switch'):
            switch(grid, numbers)
        

def turn_on(self, grid, numbers):
    row_start = numbers[0]
    row_end = numbers[2]
    col_start = numbers[1]
    col_end = numbers[3]
    
    grid[row_start:row_end, col_start:col_end] = True
    
def turn_off(self, grid, numbers):
    row_start = numbers[0]
    row_end = numbers[2]
    col_start = numbers[1]
    col_end = numbers[3]
    
    grid[row_start:row_end, col_start:col_end] = False

def switch(self, grid, numbers):
    row_start = numbers[0]
    row_end = numbers[2]
    col_start = numbers[1]
    col_end = numbers[3]
    
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if(grid[i][j] == False):
                grid[i][j] = True
            else:
                grid[i][j] = False
    



def count_lights(self, grid):
    pass

