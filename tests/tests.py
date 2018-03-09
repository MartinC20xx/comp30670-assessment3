# -*- coding: utf-8 -*-

# from .context import led_project - need to ask about this, if going to use this context file at all
from led_project import main, input_reader, instructions_processor

import numpy as np
import pytest
from led_project.main import parse_line
from led_project.led_tester import LED_tester

class TestSuite():
    """Basic test cases."""
    
    # test input reader
    # might need to __init__ instance here then access from object rather than just module name
    # self problem was coming from the fact that there was no class / object instance involved
    
    
    def test_read_local_input_line(self):
        sample_instructions_list = input_reader.read_input('./test_input.txt') 
        assert sample_instructions_list[3] == 'turn off 4,4 through 6,6'
    
        
    def test_read_url_input_line(self):
        sample_instructions_list = input_reader.read_input('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt') 
        assert sample_instructions_list[5] == 'turn off 390,473 through 1341,1378'
    
    # test input line parsing
    
    
    
    #########3
    # test grid creation
    
    def test_grid_init(self):
        grid = LED_tester(15).grid
        assert (grid[0][0] == False) and (grid.sum() == 0)
        
    def test_grid_size(self): 
        grid = LED_tester(15).grid
        assert grid.size == 225
        
    ######
    
    def test_line_parse(self):
        sample_instructions_list = input_reader.read_input('./test_input.txt') 
        parsed_line = main.parse_line(self,sample_instructions_list[1], 10)
        assert parsed_line == ['turn on', 3, 3, 8, 8]



    def test_out_of_bounds_behavior(self):
        grid_size = 10
        test_line = 'turn off -7,-7 through 12,12'
        parsed_line = main.parse_line(self, test_line, grid_size)
        
        assert parsed_line == ['turn off', 0, 0, grid_size, grid_size]
        
        # change to grid size - 1
        
        
        
        
        
    # test process line

    def test_turn_on_from_off(self):
        tester = LED_tester(2)
        numbers = [0, 0, 1, 1]
        tester.turn_on(tester.grid, numbers)
        
        assert tester.grid[0][0] == True
       
    
    def test_turn_on_when_on(self):
        tester = LED_tester(2)
        tester.grid[:] = True
        numbers = [0, 0, 1, 1]
        tester.turn_on(tester.grid, numbers)
        
        assert tester.grid[0][0] == True
    
        
    def test_turn_off_from_on(self):
        tester = LED_tester(2)
        tester.grid[:] = True
        numbers = [0, 0, 1, 1]
        tester.turn_off(tester.grid, numbers)
        
        assert tester.grid[0][0] == False
     
    
    def test_turn_off_when_off(self):
        tester = LED_tester(2)
        numbers = [0, 0, 1, 1]
        tester.turn_off(tester.grid, numbers)
        
        assert tester.grid[0][0] == False
        
        
    def test_switch_when_on(self):
        tester = LED_tester(2)
        tester.grid[:] = True
        numbers = [0, 0, 1, 1]
        tester.switch(tester.grid, numbers)
        
        assert tester.grid[0][0] == False

        
    def test_switch_when_off(self):
        tester = LED_tester(2)
        numbers = [0, 0, 1, 1]
        tester.switch(tester.grid, numbers) 
        
        assert tester.grid[0][0] == True
    
      
         
    def test_invalid_command_ignored(self):
        grid1 = LED_tester(2).grid
        grid2 = np.copy(grid1)
        parsed_line = ['urbt on',2 ,1 ,8 ,9]
        LED_tester.process_line(self, grid2, parsed_line)
        
        assert grid1.sum() == grid2.sum()
        
    

    
    #########
    
    
    def test_light_count(self):
        grid = LED_tester(4).grid
        grid[:] = True
        
        assert LED_tester.count_lights(self, grid) == 16
        
    #######
