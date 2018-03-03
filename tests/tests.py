# -*- coding: utf-8 -*-

# from .context import led_project - need to ask about this, if going to use this context file at all
from led_project import main, process_instruction_sketch

import numpy as np
import pytest

class BasicTestSuite():
    """Basic test cases."""
    
    
    
    def test_grid_size(self): #test for grid exists. find better?
        assert(main.grid.size) == main.L ** 2
    
    def test_light_count(self):
        pass

    def testInputFileExists(self):
        assert(main.input_file) != None
        #etc
    # extra test for check file is valid format?    
     
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
    
    

if __name__ == '__main__':
    BasicTestSuite()