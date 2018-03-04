'''
Currently all methods relating to instruction processing. May need refactoring.
'''




def process_line(self, grid, parsed_line):
    
    numbers = parsed_line[1:]
    # first test command is valid, if not, ignore line
    if(parsed_line[0] != 'turn on' and parsed_line[0] != 'turn off' and parsed_line[0] != 'switch'):
        pass # come back to this
    
    elif(parsed_line[0] == 'turn on'):
            turn_on(numbers)
        
    elif(parsed_line[0] == 'turn off'):
            turn_off(numbers)
            
    elif(parsed_line[0] == 'switch'):
            switch(numbers)
        

def turn_on(self, numbers):
    
    pass

def turn_off(self, numbers):
    pass

def switch(self, numbers):
    pass


def count_lights(self, grid):
    pass

