# -*- coding: utf-8 -*-

from led_project import input_reader
import numpy as np
import pytest
from led_project.led_tester import LEDTester

class TestSuite():
    """Basic test cases."""
    
    def test_read_local_input_line(self):
        sample_instructions_list = input_reader.read_input('./test_input.txt') 
        assert sample_instructions_list[3] == 'turn off 4,4 through 6,6'
    
        
    def test_read_url_input_line(self):
        sample_instructions_list = input_reader.read_input('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt') 
        assert sample_instructions_list[5] == 'turn off 390,473 through 1341,1378'
    
    
    # test grid creation
    
    def test_grid_init(self):
        grid = LEDTester(15).grid
        assert (grid[0][0] == False) and (grid.sum() == 0)
        
    def test_grid_size(self): 
        grid = LEDTester(15).grid
        assert grid.size == 225
        
    ######
    
    def test_line_parse(self):
        sample_instructions_list = input_reader.read_input('./test_input.txt') 
        parsed_line = input_reader.parse_line(sample_instructions_list[1], 10)
        assert parsed_line == ['turn on', 3, 3, 8, 8]



    def test_out_of_bounds_behavior(self):
        grid_size = 10
        test_line = 'turn off -7,-7 through 12,12'
        parsed_line = input_reader.parse_line(test_line, grid_size)
        
        assert parsed_line == ['turn off', 0, 0, grid_size-1, grid_size-1]
        
          
        
    # test process line

    def test_turn_on_from_off(self):
        tester = LEDTester(2)
        numbers = [0, 0, 1, 1]
        tester.turn_on(numbers)
        
        assert tester.grid[0][0] == True
       
    
    def test_turn_on_when_on(self):
        tester = LEDTester(2)
        tester.grid[:] = True
        numbers = [0, 0, 1, 1]
        tester.turn_on(numbers)
        
        assert tester.grid[0][0] == True
    
        
    def test_turn_off_from_on(self):
        tester = LEDTester(2)
        tester.grid[:] = True
        numbers = [0, 0, 1, 1]
        tester.turn_off(numbers)
        
        assert tester.grid[0][0] == False
     
    
    def test_turn_off_when_off(self):
        tester = LEDTester(2)
        numbers = [0, 0, 1, 1]
        tester.turn_off(numbers)
        
        assert tester.grid[0][0] == False
        
        
    def test_switch_when_on(self):
        tester = LEDTester(2)
        tester.grid[:] = True
        numbers = [0, 0, 1, 1]
        tester.switch(numbers)
        
        assert tester.grid[0][0] == False

        
    def test_switch_when_off(self):
        tester = LEDTester(2)
        numbers = [0, 0, 1, 1]
        tester.switch(numbers) 
        
        assert tester.grid[0][0] == True
    
      
         
    def test_invalid_command_ignored(self):
        grid1 = LEDTester(10).grid
        grid2 = np.copy(grid1)
        parsed_line = ['urbt on',2 ,1 ,8 ,9]
        LEDTester.process_line(self, parsed_line)
        
        assert grid1.sum() == grid2.sum()
    
    
        
    
    #########
    
    
    def test_light_count(self):
        tester = LEDTester(4)
        tester.grid[:] = True
        
        assert tester.count_lights() == 16
        
    #######
