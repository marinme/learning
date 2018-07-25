import funcs
import unittest


class TestFuncs(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(funcs.mean(3, 4, 5), 4)
        self.assertEqual(funcs.mean(1,2,3,4,5), 3)
        self.assertEqual(funcs.mean(1), 1)
        with self.assertRaises(ZeroDivisionError):
            funcs.mean()
        self.assertEqual(funcs.mean(1000000000, 1000000002, 1000000001), 1000000001)
        self.assertEqual(funcs.mean(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1), 1)

    def test_mean_subgoal(self):
        self.assertEqual(funcs.mean(1,2), 1.5)  # subgoals, manually specify 1 significant digits
        self.assertEqual(funcs.mean(1, 2, 4), 2.33)  # subgoals, manually specify 2 for significant digits
        self.assertEqual(funcs.mean(5, 8, 10), 7.67) #subgoals, manually specify 2 for significant digits

    def test_median(self):
        self.assertEqual(funcs.median(3,4,5,7,9), list(5))
        self.assertEqual(funcs.median(1), list(1))
        self.assertEqual(funcs.median(1, 1, 1, 1, 1, 1), list(1))

    def test_median_subgoal(self):
        self.assertEqual(funcs.median(1, 2, 3, 4, 5, 6), list(3, 4))

    def test_mode(self):
        self.assertEqual(funcs.mode(1,1,2,3,4,5), list(1))
        self.assertEqual(funcs.mode(1,1,2,2,2,3,4), list(3))

    def test_mode_subgoal(self):
        self.assertEqual(funcs.mode(1,1,2,2), list(1, 2))
