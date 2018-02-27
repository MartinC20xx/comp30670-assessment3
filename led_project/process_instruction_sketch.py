import numpy as np

def parseInstruction(inst):
        
    parsed_inst = ['','test',(10,10), (20,10)]
    
    if(parsed_inst[0] != 'turn on' and parsed_inst[0] != 'turn off' and parsed_inst[0] != 'switch'):
        return None   # error case
    
    #regex parse to list
    return parsed_inst

# create Grid called the first line of reading the instructions
def createGrid(size):
    grid = np.full((size, size), False)
    

def processInstruction(parsed_inst):
    
    if(parsed_inst != None):
       
        if(parsed_inst[1] == 'turn on'):
            turn_on(parsed_inst[2], parsed_inst[3])
        
        if(parsed_inst[1] == 'turn off'):
            turn_off(parsed_inst[2], parsed_inst[3])
            
        if(parsed_inst[1] == 'switch'):
            turn_on(parsed_inst[2], parsed_inst[3])
    
    
        
        

def turn_on(start_index, stop_index):
    pass

def turn_off(start_index, stop_index):
    pass

def switch(start_index, stop_index):
    pass

