# defined users for this are Stuart and Kevin
from string import ascii_letters, digits, punctuation
import re


KEVIN = list("AEIOU")
STUART = list(set(ascii_letters).difference(set(KEVIN)))


def minion_game(string):
    """This calculates the winner of a minion game based on the given string
    The two given players are Stuart and Kevin where Stuart must begin substrings with consonants and
    Kevin must begin with vowels. A point is given for each unique occurrence of the substring"""
    if len(set(string).intersection(digits)) > 0 or len(set(string).intersection(punctuation)) > 0:
        raise ValueError("Invalid input")
    if len(string) <= 1:
        raise ValueError("Too short of string")
    treated_string = string.upper()
    kev_score = calc_score(KEVIN, treated_string)
    stu_score = calc_score(STUART, treated_string)
    if kev_score > stu_score:
        return "Kevin {}".format(kev_score)
    return "Stuart {}".format(stu_score)



def _get_substrings(source_string):
    result = list()
    for i in range(len(source_string)):
        for j in range(i+1, len(source_string) + 1):
            result.append(source_string[i:j])

    return list(set(result))


def _count_single_score(source_string, substring):
    pattern = re.compile(substring)
    count = len(pattern.findall(source_string))
    return count


def calc_score(person, source_string):
    """This calculates the score based on a list of characters and the source string. The list of characters
    are available for starting the substrings that are used to calculate the score. This function will aggregate the
    score across all substrings that match the person and the source string."""
    total_score = 0
    for sub_string in _get_substrings(source_string):
        if sub_string[0] in person:
            total_score += _count_single_score(source_string, sub_string)
    return total_score