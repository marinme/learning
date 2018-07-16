import unittest
import main


class TestMain(unittest.TestCase):

    def test_basic_wins(self):
        self.assertEqual(main.minion_game("BANANA"), "Stuart 12")  # testing for Consonant Win
        # self.assertEqual(main.minion_game(""), "Draw 1")  # testing for Draw condition
        # need to figure out a draw condition word, could write some code to find it based on a dictionary, but
        # that isn't the point now. Let's keep moving on.
        self.assertEqual(main.minion_game("ALOE"), "Kevin 7")

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            main.minion_game("")
            main.minion_game("a")  # pretend to have some semblance of balance
            main.minion_game("123")
            main.minion_game("word1abc")

    def test_input_variance(self):
        self.assertEqual(main.minion_game("aloe"), "Kevin 7")  # lower case works the same
        self.assertEqual(main.minion_game("aLoE"), "Kevin 7")  # mixed case works the same
    # self.assertEqual(main.minion_game("A T"), "Kevin 3")  # spaces count as substring, not specified otherwise in req

    def test_get_substrings(self):
        self.assertIsInstance(main._get_substrings("BANANA"), list)  # expecting to get a set of substrings
        self.assertEqual(set(main._get_substrings("ALOE")), set(["A", "AL", "ALO", "ALOE",
                                                        "L", "LO", "LOE",
                                                        "O", "OE", "E"]))

    def test_count_single_string_score(self):
        self.assertEqual(main._count_single_score("BANANA", "AN"), 2)
        self.assertEqual(main._count_single_score("BANANA", "A"), 3)
        self.assertEqual(main._count_single_score("ALOE", "LOE"), 1)
        self.assertEqual(main._count_single_score("ALOE", "B"), 0)

    def test_calc_score(self):
        from main import KEVIN, STUART
        self.assertEqual(main.calc_score(KEVIN, "ALOE"), 7)  # A, AL, ALO, ALOE, O, OE, E
        self.assertEqual(main.calc_score(STUART, "BANANA"), 12)  # B, BA, BAN, BANA, BANAN, BANANA, N, NA, NAN, NANA, N, NA
        # self.assertEqual(main.calc_score(KEVIN, "AT"), main.calc_score(STUART, "AT")) need to figure out a draw
        # condition in order to test it. originally, I thought the some_string[:] didn't count and "AT" would force a
        # draw; this isn't true now and I don't know what else to use to test.
