# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """

    generated = ''
    special = '!"#$%&()*+,-./:;<=>?@^_`{|}'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    # your code

    return generated


def bubble_sort(numbers):
    n = len(numbers)
    replaces = True
    while replaces:
        replaces = False
        for i in range(1, n):
            if numbers[i-1] > numbers[i]:
                temp = numbers[i]
                numbers[i] = numbers[i-1]
                numbers[i-1] = temp
                replaces = True
        n -= 1
    return numbers
