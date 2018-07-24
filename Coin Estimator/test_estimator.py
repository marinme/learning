import estimator
import unittest


class TestEstimator(unittest.TestCase):

    def test_base_estimator(self):
        pass
        # test that coin weight and wrapper values match given params
        # test that coin type is accounted for
        # test that exact amounts give the right number of rolls
        # test the number of total coins is given
        # test that the total value of coins is given
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
