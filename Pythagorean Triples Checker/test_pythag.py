from pythag import pythag
import unittest

class TestPythag(unittest.TestCase):
    def test_pythag(self):
        # test basic inputs
        self.assertTrue(pythag(3,4,5))
        self.assertFalse(pythag(3,4,6))

    def test_pythag_ordering(self):
        self.assertEqual(pythag(3,4,5), pythag(5,3,4))

    def test_pythag_short_input(self):
        self.assertIn(pythag(3,4),[True,False]) # assumes it still returns a value by asking the user for input

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            pythag(2,3,4,5)
            pythag(2,'a')
            pythag(None,1)
