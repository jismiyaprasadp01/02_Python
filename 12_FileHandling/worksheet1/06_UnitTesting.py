'''Unit Testing
 Covers: Basic unit testing
 Description: Write tests using a framework like unittest or pytest to validate the 
functionality of the previously developed scripts.'''

import unittest
from math_script import add

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3), 5)

if __name__ == "__main__":
    unittest.main()
