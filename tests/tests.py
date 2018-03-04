# -*- coding: utf-8 -*-

# from .context import led_project - need to ask about this, if going to use this context file at all
from led_project import main, input_reader, instructions_processor

import numpy as np
import pytest
from led_project.main import parse_line

class TestSuite():
    """Basic test cases."""
    
    # test input reader
    
    
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
        grid = main.create_grid(self,15)
        #grid[:,:] == False
        #grid.sum() = 0
        assert (grid[0][0] == False) and (grid.sum() == 0)
        
    def test_grid_size(self): 
        # what is going on with self here?
        #print(id(self)) - reminder for the issue
        grid = main.create_grid(self,15)
        #print(id(grid)) - reminder 
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
        grid = np.full((2,2), False)
        numbers = [0, 0, 1, 1]
        instructions_processor.turn_on(self, grid, numbers)
        
        assert grid[0][0] == True
       
    
    def test_turn_on_when_on(self):
        grid = np.full((2,2), True)
        numbers = [0, 0, 1, 1]
        instructions_processor.turn_on(self, grid, numbers)
        
        assert grid[0][0] == True
    
        
    def test_turn_off_from_on(self):
        grid = np.full((2,2), True)
        numbers = [0, 0, 1, 1]
        instructions_processor.turn_off(self, grid, numbers)
        
        assert grid[0][0] == False
     
    
    def test_turn_off_when_off(self):
        grid = np.full((2,2), False)
        numbers = [0, 0, 1, 1]
        instructions_processor.turn_off(self, grid, numbers)
        
        assert grid[0][0] == False
        
        
    def test_switch_when_on(self):
        grid = np.full((2,2), True)
        numbers = [0, 0, 1, 1]
        instructions_processor.switch(self, grid, numbers)
        
        assert grid[0][0] == False

        
    def test_switch_when_off(self):
        grid = np.full((2,2), False)
        numbers = [0, 0, 1, 1]
        instructions_processor.switch(self, grid, numbers) 
        
        assert grid[0][0] == True
    
      
         
    def test_invalid_command_ignored(self):
        # maybe have a temp grid, perform process, then compare with orig
        grid1 = np.full((2,2), False)
        grid2 = np.copy(grid1)
        parsed_line = ['urbt on',2 ,1 ,8 ,9]
        instructions_processor.process_line(self, grid2, parsed_line)
        
        assert grid1.sum() == grid2.sum()
        
    

    
    #########
    
    
    def test_light_count(self):
        pass
        
    #######
