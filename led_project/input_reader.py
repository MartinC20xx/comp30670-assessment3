''' Reads an input file and returns a list of instruction lines ''' 
import requests
import re

def read_input(input):
    if(input.startswith('http://')):
        r = requests.get(input, stream=True)
        instructions_text = r.text
    else:
        instructions_text = input
    
    
    instructions_list = instructions_text.split(sep='\n')
    
    #this should be moved to another function for processing
    #instruction_pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
    
    return instructions_list
 
 
   
input = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'


instructions = read_input(input)
for instruction in instructions:
    
    #print(instruction_pattern.split(instruction))
   # print(instruction)
    #print(instruction_pattern.split(instruction))
        print(instruction)
    # probably just return the instructions_list from this file
    






    
#instructions_list = instructions_text.split(sep='\n')

#straight from the lecture notes
#instruction_pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 


#for instruction in instructions_list:
    
    #print(instruction_pattern.split(instruction))
   # print(instruction)
    # probably just return the instructions_list from this file
    




       
    


