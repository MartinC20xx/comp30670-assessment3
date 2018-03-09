''' Set of functions for reading and parsing the input file.'''
 
import requests
import re

        
def read_input(input):
    if(input.startswith('http://')):
        r = requests.get(input, stream=True)
        instructions_text = r.text
        instructions_list = instructions_text.split(sep='\n')
    else:
        
        buffer = open(input).read()
        instructions_list = buffer.split('\n')
                
    
    return instructions_list
 

def parse_line(instruction, grid_size):
    instruction_pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
    line = instruction_pattern.split(instruction)
    line = list(filter(None, line))
    line[1:] = [int(num) for num in line[1:]]
    
    # test numbers for out of range values. trim to nearest existing grid position
    line[1:] = list(map(lambda num: 0 if num < 0 else num, line[1:]))
    line[1:] = list(map(lambda num: (grid_size-1) if num > (grid_size-1) else num, line[1:]))
    return line


    
    


