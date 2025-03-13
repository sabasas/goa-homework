# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    result = list()
    for num in lst:
        result.append(-num)
    return result