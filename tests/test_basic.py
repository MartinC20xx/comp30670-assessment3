# -*- coding: utf-8 -*-

# from .context import led_project - need to ask about this, if going to use this context file at all
from led_project import main

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def testGridSize(self):
        assert(main.grid.size) == main.L ** 2

# need to test 



if __name__ == '__main__':
    unittest.main()