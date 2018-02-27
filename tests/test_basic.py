# -*- coding: utf-8 -*-

# from .context import led_project - need to ask about this, if going to use this context file at all
from led_project import main

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def testGridSize(self):
        assert(main.grid.size) == main.L ** 2
    
    def testLightCount(self):
        pass

    def testInputFileExists(self):
        assert(main.input_file) != None
        #etc
    # extra test for check file is valid format?    
    
    def testInstructionsFromFileOk(self):
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
    
    

if __name__ == '__main__':
    unittest.main()