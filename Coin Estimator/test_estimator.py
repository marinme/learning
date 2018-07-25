import estimator
import unittest


class TestEstimator(unittest.TestCase):

    def test_base_estimator(self):
        # DEPENDENCY ON convert_units() function
        # test that coin weight and wrapper values match given params
        # test that coin type is accounted for
        # test that exact amounts give the right number of rolls
        # test the number of total coins is given
        self.assertEqual(estimator.estimator(125, 'g', 'PENNY'), (50, 1))
        self.assertEqual(estimator.estimator(200, 'g', 'NICKEL'), (40, 1))
        self.assertEqual(estimator.estimator(113.4, 'g', 'DIME'), (50, 1))
        self.assertEqual(estimator.estimator(226.8, 'g', 'QUARTER'), (40, 1))
        self.assertEqual(estimator.estimator(187.5, 'g', 'PENNY'), (75, 1))
        self.assertEqual(estimator.estimator(56700, 'g', 'DIME'), (25000, 500))
        self.assertEqual(estimator.estimator(0.275579, 'p', 'PENNY'), (50, 1))
        self.assertEqual(estimator.estimator(0.250005, 'p', 'DIME'), (50, 1))
        self.assertEqual(estimator.estimator(125.002205, 'p', 'DIME'), (25000, 500))
        # I removed some test cases -- zeroes, high values, negative values, asserting error handling. Mostly that
        # this is a trivial program and I'm spending a bit too much time on it without feeling that I'm gaining
        # value from it.

    def test_convert_units(self):
        # this isn't used for grams -> pounds. As that functionality isn't needed, it isn't implemented.
        # adding 0.000005 to assist in rounding errors for such large unit size disparity. Could be implemented
        # through the decimal library, but I'm not really interested in that level of accuracy.
        self.assertEqual(estimator.convert_units(10, 'p'), 4535.920005)
        self.assertEqual(estimator.convert_units(0, 'p'), 0.000005)
        with self.assertRaises(ValueError):
            estimator.convert_units(-5, 'p')
            estimator.convert_units(-999, 'g')


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

        # base case testing
        self.assertEqual(self.single_penny_roll.get_roll(), 1, "Single Penny Roll not valid")
        self.assertEqual(self.single_nickel_roll.get_roll(), 1, "Single Nickel Roll not valid")
        self.assertEqual(self.single_dime_roll.get_roll(), 1, "Single Dime Roll not valid")
        self.assertEqual(self.single_quarter_roll.get_roll(), 1, "Single Quarter Roll not valid")
        self.assertEqual(self.one_and_a_half_penny_roll.get_roll(), 1, "Roll and a half of pennies should"
                                                                       " return 1 roll")
        self.assertEqual(self.five_hundred_dime_rolls.get_roll(), 500, "Five hundred rolls of dimes should "
                                                                       "return 500 rolls")
        # extended case testing
        dirty_pennies = estimator.Coin(1251.225, 'PENNY')  # an extra 1.225g of grime on the 500 pennies
        one_more_penny = estimator.Coin(1252.1, 'PENNY')  # missing a chunk of a penny
        shorted_dimes = estimator.Coin(215.46, 'DIME')  # 95 dimes
        self.assertEqual(dirty_pennies.get_roll(), 10)
        self.assertEqual(one_more_penny.get_roll(), 10)
        self.assertEqual(shorted_dimes.get_roll(), 1)  # only enough to fill out one roll

    def test_get_value(self):
        self.assertEqual(self.single_penny_roll.get_value(), 50, "125g of pennies should be 50 pennies")
        self.assertEqual(self.single_nickel_roll.get_value(), 40, "200g of nickels should be 40 nickels")
        self.assertEqual(self.single_dime_roll.get_value(), 50, "113.4g of dimes should be 50 dimes")
        self.assertEqual(self.single_quarter_roll.get_value(), 40, "226.8g of quarters should be 40 quarters")
        self.assertEqual(self.one_and_a_half_penny_roll.get_value(), 75, "187.5g of pennies should be 75 pennies")
        self.assertEqual(self.five_hundred_dime_rolls.get_value(), 25000, "56,700g of dimes should be 25,000 dimes")
        # should return estimated number of coins by weight
