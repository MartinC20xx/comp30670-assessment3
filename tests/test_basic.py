# -*- coding: utf-8 -*-

# from .context import led_project - need to ask about this, if going to use this context file at all
from led_project import main

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def testGridSize(self):
        assert(main.grid.size) == main.L ** 2

    def testInputFileExists(self):
        assert(main.input_file) != None
    
    # should test out each of the three operations.
    # although might not need separate methods for each one. 
    # could just have a process input line method.
    
    #def testTurnOnFromOff(self):
        #assert (main.turn_on()) == True
    
    #def testTurnOnWhenOn(self):
        #assert (main.turn_on()) == True
        
    #def testTurnOffFromOn(self):
        #assert (main.turn_off()) == False
    
    #def testTurnOffWhenOff(self):
        #assert (main.turn_off()) == False
        
    #def testSwitchWhenOn(self):
        #assert (main.switch()) == False
        
    #def testSwitchWhenOff(self):
        #assert (main.switch()) == True
    

if __name__ == '__main__':
    unittest.main()