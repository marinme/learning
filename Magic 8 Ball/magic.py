import random
import math

# removed the menu stuff because I want to just work these exercises and get to my own projects for now.
# this is more of my own learning practice and I'll be adding in some more complex stuff like unit testing
# print statements (yes, I did look up redirecting sys.stdout and using doctest), but then I'll be working that
# when I get in to building out network stacks from RFCs since I feel comfortable in that domain.

answers = ["It is decidely so.", "Yes.", "The answer is certain.",
           "Maybe", "It is uncertain, try again later.", "The future is cloudy",
           "No", "Definitely not."]

def magic(question):
    if len(question) <= 0:
        raise ValueError("Invalid question, try again.")
    if not question[-1] == '?':
        raise ValueError("That is not a question")
    return answers[math.floor((random.random() * len(answers)))]

if __name__=="__main__":
    print(magic("Hello?"))