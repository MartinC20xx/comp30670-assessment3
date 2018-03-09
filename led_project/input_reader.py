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
    line[1:] = list(map(lambda num: grid_size if num > grid_size else num, line[1:]))
    return line



   
input = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'
input_local = 'test_input.txt'


instructions = read_input(input_local)
print(instructions[0]=='1000')
print(instructions[3]=='turn off 199,133 through 461,193')
for instruction in instructions:
    print(instruction)
    
    


