import unittest

#
# Example based on code here: https://docs.python.org/2/library/unittest.html
#
class TestUnitTestPresent(unittest.TestCase):

  def test_dummy_test(self):
    self.assertEqual(1,1)
    self.assertTrue(True)
    self.assertFalse(False)


if __name__ == '__main__':
  unittest.main()

		
