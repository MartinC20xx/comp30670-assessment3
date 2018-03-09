'''
Console script for led_tester.
'''
import sys
import click
from led_project.led_tester import LEDTester
from led_project import input_reader
click.disable_unicode_literals_warning = True

@click.command()
@click.option('--input', default=None, help="Specify input file. File path or URL accepted")
def main(input=None):
    '''Console script for led_project'''
    
    # read input file and convert to list of instruction lines 
    instructions_list = input_reader.read_input(input)
    # get grid size from first line of instructions list
    grid_size = instructions_list[0]
    # remove size line from instructions list
    instructions_list = instructions_list[1:]
    # create new LEDTester object
    tester = LEDTester(grid_size)
    
    for instruction in instructions_list:
        line = input_reader.parse_line(instruction, grid_size)
        tester.process_line(line)
        
    print(tester.count_lights())
    

if __name__ == '__main__':
    sys.exit(main())