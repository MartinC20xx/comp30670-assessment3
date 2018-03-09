'''
Console script for led_tester.
'''
import sys
import click
from led_project import led_tester
#from led_tester import LEDTester
from led_project import input_reader
click.disable_unicode_literals_warning = True

@click.command()
@click.option('--input', default=None, help="Specify input file. File path or URL accepted")
def main(input=None):
    '''Console script for led_project'''
    
    input_test = './test_input.txt'
    
    first_input = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'
    input_a = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt'
    input_b = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt'  
    input_c = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt'
    input_d = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt'
      # read input file and convert to list of instruction lines 
    instructions_list = input_reader.read_input(input_d)
    # get grid size from first line of instructions list
    grid_size = int(instructions_list[0])
    # remove size line from instructions list
    instructions_list = instructions_list[1:]
    # create new LEDTester object
    tester = led_tester.LEDTester(grid_size)
    
    for instruction in instructions_list:
        line = input_reader.parse_line(instruction, grid_size)
        if(len(line) < 1):
            continue
        # seems to be processing 
        tester.process_line(line)
        
    print(tester.count_lights())
    
    return 0

if __name__ == '__main__':
    sys.exit(main())