
import unittest

import context

from fizzbuzz import MainClass

#
# Example based on code here: https://docs.python.org/2/library/unittest.html
#
class TestFizzBuzz(unittest.TestCase):

  def setUp(self):
      self.fizzbuzz = MainClass()

  def test_fizz_number(self):
    result = self.fizzbuzz.fizz(4)
    self.assertIsNotNone(result)



if __name__ == '__main__':
    unittest.main()


