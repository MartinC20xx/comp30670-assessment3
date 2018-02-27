def parse_instruction(inst):
        
    parsed_inst = ['test',(10,10), (20,10)]
    
    if(parsed_inst[0] != 'turn on' and parsed_inst[0] != 'turn off' and parsed_inst[0] != 'switch'):
        return None   # error case
    
    #regex parse to list
    return parsed_inst

def process_instruction(parsed_inst):
    
    if(parsed_inst != None):
       
        if(parsed_inst[0] == 'turn on'):
            turn_on(parsed_inst[1], parsed_inst[2])
        
        if(parsed_inst[0] == 'turn off'):
            turn_off(parsed_inst[1], parsed_inst[2])
            
        if(parsed_inst[0] == 'switch'):
            turn_on(parsed_inst[1], parsed_inst[2])
    
    
        
        

def turn_on(start_index, stop_index):
    pass

def turn_off(start_index, stop_index):
    pass

def switch(start_index, stop_index):
    pass

