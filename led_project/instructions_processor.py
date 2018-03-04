'''
Currently all methods relating to instruction processing. May need refactoring.
'''

#def get_size(self, instructions_list):
   # pass



def process_line(self, grid, parsed_line):
    
    # first test command is valid, if not, ignore line
    if(parsed_line[0] != 'turn on' and parsed_line[0] != 'turn off' and parsed_line[0] != 'switch'):
        pass # come back to this
    
    elif(parsed_line[0] == 'turn on'):
        
            numbers = parsed_line[1:]
            grid_size = main.g
        
            turn_on(numbers)
        
    elif(parsed_inst[1] == 'turn off'):
            turn_off(parsed_inst[2], parsed_inst[3])
            
    elif(parsed_inst[1] == 'switch'):
            turn_on(parsed_inst[2], parsed_inst[3])
        

def turn_on(self, numbers, grid_size):
    
    
    pass

def turn_off(self):
    pass

def switch(self):
    pass

def count_lights(self, grid):
    pass

