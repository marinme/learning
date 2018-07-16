import bottles
from unittest import TestCase

class TestBottles(TestCase):
    def test_bottles(self):  # not much to test with this simple output function.
        self.assertIn("10 bottles of beer on the wall", bottles.bottles(10))
        self.assertIn("Take one down. Pass it around.", bottles.bottles(2))
        self.assertIn("1 bottle of beer on the wall.", bottles.bottles(2))
