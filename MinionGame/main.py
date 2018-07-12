# defined users for this are Stuart and Kevin
from string import ascii_letters
KEVIN = ["AEIOU"]
STUART = list(set(ascii_letters).difference(set(KEVIN)))


def minion_game(string):
    """This calculates the winner of a minion game based on the given string
    The two given players are Stuart and Kevin where Stuart must begin substrings with consonants and
    Kevin must begin with vowels. A point is given for each unique occurrence of the substring"""
    pass


def _get_substrings(source_string):
    result = list()
    for i in range(len(source_string)):
        for j in range(i+1, len(source_string) + 1):
            if source_string[i:j] != source_string:
                result.append(source_string[i:j])

    return list(set(result))


def _count_single_score(source_string, substring):

    return 0


def calc_score(person, source_string):
    """This calculates the score based on a list of characters and the source string. The list of characters
    are available for starting the substrings that are used to calculate the score. This function will aggregate the
    score across all substrings that match the person and the source string."""

    return 0