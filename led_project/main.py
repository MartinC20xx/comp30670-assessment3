'''Console script for led_project.'''

import sys
import click
import re
import numpy as np
from led_project import input_reader, instructions_processor
click.disable_unicode_literals_warning = True

@click.command()
@click.option('--input', default=None, help="Specify input file. File path or URL accepted")
def main(input=None):
    '''Console script for led_project'''
    print('input: ', input)
    
    # read input file and convert to list of instruction lines 
    instructions_list = input_reader.read_input(input)
    # find grid size and create and initialise grid
    grid_size = instructions_list[0]
    create_grid(grid_size)
    # parse instructions using regex (from module notes)
    instruction_pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
    
    #actual turning on/off of the lights
    for instruction in instructions_list:
    
        # each instruction_line is a list from a parsed line of instructions
        instruction_line = instruction_pattern.split(instruction)
        instructions_processor.process_line(instruction_line)
    
    
    print("Light count: ", instructions_processor.count_lights())
 
    
def create_grid(self, size):
    return np.full((size, size), False)
    
       

if __name__ == '__main__':
    sys.exit(main())