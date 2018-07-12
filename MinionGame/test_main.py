import unittest
import main


class TestMain(unittest.TestCase):

    def test_basic_wins(self):
        self.assertEqual(main.minion_game("BANANA"), "Stuart 12")  # testing for Consonant Win
        self.assertEqual(main.minion_game("AT"), "Draw 1")  # testing for Draw condition
        self.assertEqual(main.minion_game("ALOE"), "Kevin 5")

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            main.minion_game("")
            main.minion_game("a")  # pretend to have some semblance of balance
            main.minion_game("123")
            main.minion_game("word1abc")

    def test_input_variance(self):
        self.assertEqual(main.minion_game("aloe"), "Kevin 5")  # lower case works the same
        self.assertEqual(main.minion_game("aLoE"), "Kevin 5")  # mixed case works the same
        self.assertEqual(main.minion_game("A T"), "Kevin 3")  # spaces count as substring, not specified otherwise in req

    def test_get_substrings(self):
        self.assertIsInstance(main._get_substrings("BANANA"), list)  # expecting to get a set of substrings
        self.assertEqual(set(main._get_substrings("ALOE")), set(["A", "AL", "ALO",
                                                        "L", "LO", "LOE",
                                                        "O", "OE", "E"]))

    def test_count_single_string_score(self):
        self.assertEqual(main._count_single_score("BANANA", "AN"), 2)
        self.assertEqual(main._count_single_score("BANANA", "A"), 3)
        self.assertEqual(main._count_single_score("ALOE", "LOE"), 1)
        self.assertEqual(main._count_single_score("ALOE", "B"), 0)

    def test_calc_score(self):
        from main import KEVIN, STUART
        self.assertEqual(main.calc_score(KEVIN, "ALOE"), 5)
        self.assertEqual(main.calc_score(STUART, "BANANA"), 12)
        self.assertEqual(main.calc_score(KEVIN, "AT"), main.calc_score(STUART, "AT"))
