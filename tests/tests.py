# -*- coding: utf-8 -*-

# from .context import led_project - need to ask about this, if going to use this context file at all
from led_project import main, input_reader

import numpy as np
import pytest

class TestSuite():
    """Basic test cases."""
    
    
    def test_read_local_input_size(self):
        sample_instructions_list = input_reader.read_input('./test_input.txt') 
        assert sample_instructions_list[0] == '10'
    
    def test_read_local_input_line(self):
        sample_instructions_list = input_reader.read_input('./test_input.txt') 
        assert sample_instructions_list[3] == 'switch 5,5 through 7,7'
    
    def test_read_url_input_size(self):
        sample_instructions_list = input_reader.read_input('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt')
        assert sample_instructions_list[0] == '1000'
        
    def test_read_url_input_line(self):
        sample_instructions_list = input_reader.read_input('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt') 
        assert sample_instructions_list[5] == 'turn off 390,473 through 1341,1378'
    
    
    
    
    #########3
    def test_grid_size(self): #test for grid exists. find better?
        #assert(main.grid.size) == main.L ** 2
        pass
    def test_light_count(self):
        pass

    def testInvalidInstructionIgnored(self):
        pass
    
    def testValidLineParsedCorrectly(self):
        pass
    
    def testCmdAssignedToCorrectMethod(self):
        pass
    
    # tests for correct functionality of main light methods

    def testTurnOnFromOff(self):
        pass
    
    def testTurnOnWhenOn(self):
        pass
        
    def testTurnOffFromOn(self):
        pass
    
    def testTurnOffWhenOff(self):
        pass
        
    def testSwitchWhenOn(self):
        pass
        
    def testSwitchWhenOff(self):
        pass
        
    #######
    
    

#if __name__ == '__main__':
 #   BasicTestSuite()