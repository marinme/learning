import unittest
import unittest.mock  # going to need this to automate the user input and the random function
import guess

class TestGuess(unittest.TestCase):
    def test_guess(self):
        pass
    # req: generate number between 1 and 100
    # req: user input can drive higher or lower
    # req: guessing number gets congrats message
    # req: count how many guesses to reach solution