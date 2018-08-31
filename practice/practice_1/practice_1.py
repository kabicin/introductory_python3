import doctest
from typing import List

'''
Task:
- Complete the function body of the templates written below.

How to check answers:
1. Run practice_1.py and make sure all tests pass. (Right click over the function and
click 'Run > Doctest <function name>')
2. Run practice_1_unittest.py and make sure all extra tests pass.
'''


def get_sum_sorted(lst: List[int]):
    """
    Returns the sum of every other element in list
    lst when sorted, starting at and including the first element.
    Bonus: Try implementing using sum().

    Docstring Examples:
    >>> lst1 = [1, 2, 3, 4, 5]
    >>> get_sum_sorted(lst1)
    9
    >>> lst2 = [3, 1, 4, 2]
    >>> get_sum_sorted(lst2)
    4
    """
    pass


def get_keener(names: List[str], marks: List[float]):
    """
    Returns the name of the individual with the highest mark in the class given the
    parallel lists, names and marks.
    You can assume that each person gets a different mark because we are all special snowflakes!
    You can assume that len(names) == len(marks)

    Docstring Examples:
    >>> names = ["Eric", "Billy"]
    >>> marks = [95, 55]
    >>> get_keener(names, marks)
    'Eric is a keener'
    >>> names_2 = []
    >>> marks_2 = []
    >>> get_keener(names_2, marks_2)
    'Nobody is a keener'
    """
    pass


def amazing_sequence():
    """
    Return a list of the format [2, 5, 8, 11, ...] displaying 100 digits of the sequence in one line only.

    No docstring example  :(
    """
    pass

if __name__ == "__main__":
    doctest.testmod()
