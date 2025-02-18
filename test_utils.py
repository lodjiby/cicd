import unittest

# Sample function to test
def add(a, b):
    return a + b

# Test case class
class TestUtils(unittest.TestCase):
    
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative(self):
        result = add(-1, 1)
        self.assertEqual(result, 0)

