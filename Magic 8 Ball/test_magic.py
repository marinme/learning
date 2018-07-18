import magic
from unittest import TestCase

class TestMagic(TestCase):
    def test_magic(self):
        self.assertGreater(len(magic.magic("What is the meaning of life?")), 0)  # test that a question gets a response
        # test that out of 100 questions, we don't get the same answer. This could fail with low probability, but
        # I'm willing to take the risk for non-prod code.
        answers = {}
        multi_answers = False
        for i in range(100):
            answers[magic.magic("No, really what is the meaning of life?")] = 1
            if len(answers.values()) > 1:
                multi_answers = True
        self.assertEqual(multi_answers, True)

    def test_bad_input_handling(self):
        with self.assertRaises(ValueError):
            magic.magic("")
            magic.magic("This is a question")
