import os
import sys
sys.path.insert(0, os.path.abspath('lib'))

import unittest

from fizzbuzz import FizzBuzz

#
# Example based on code here: https://docs.python.org/2/library/unittest.html
#
class TestFizzBuzz(unittest.TestCase):

  def setUp(self):
      self.fizzbuzz = FizzBuzz()

  def test_fizz_number(self):
    result = self.fizzbuzz.fizz(4)
    self.assertIsNotNone(result)



if __name__ == '__main__':
    unittest.main()


