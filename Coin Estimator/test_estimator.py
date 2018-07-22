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


class TestCoin(unittest.TestCase):

    def setUp(self):
        # base cases set up here. Extended cases must be set up in the test
        self.single_penny_roll = estimator.Coin(125, 'PENNY')
        self.single_nickel_roll = estimator.Coin(200, 'NICKEL')
        self.single_dime_roll = estimator.Coin(113.4, 'DIME')
        self.single_quarter_roll = estimator.Coin(226.8, 'QUARTER')
        self.one_and_a_half_penny_roll = estimator.Coin(187.5, 'PENNY')
        self.five_hundred_dime_rolls = estimator.Coin(56700, 'DIME')
    def test_get_roll(self):
        # should return number of equal rolls and remaining estimated value.
        pass
    def test_get_value(self):
        pass
        # should return estimated value by weight
        # rounded values will be based on 50% boundaries for whether or not another coin exists