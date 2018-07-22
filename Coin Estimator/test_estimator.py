import estimator
import unittest


class TestEstimator(unittest.TestCase):

    def test_base_estimator(self):
        pass
        # test that coin weight and wrapper values match given params
        # test that coin type is accounted for
        # test that exact amounts give the right number of rolls
        # test that under values are excluded and the remaining amount of coins is listed
        # test high numbers
        # test zero values

    def test_convert_units(self):
        pass
        # test that pounds convert to grams correctly
        # test that grams convert to pounds correctly

    def test_bad_inputs(self):
        pass
        # test that negative values are handled
        # test that non-numeric values are handled
