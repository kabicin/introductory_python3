import doctest

'''
Task:
- Complete the function body of the templates written below.
How to check answers:
1. Run practice_0.py and make sure all tests pass. (Right click over the function and
click 'Run > Doctest <function name>')
2. Run practice_0_unittest.py and make sure all extra tests pass.
'''


def get_letter_grade(mark: int):
    """
    Returns the Ontario standard letter grade of the provided integer, mark.
    If the mark is invalid return 'Invalid'

    A  : 80 - 100%
    B : 70% - 79%
    C : 60% - 69%
    D : 50% - 59%
    R  : 0% - 49%

    >>> mark = 40
    >>> get_letter_grade(mark)
    'R'

    >>> mark2 = -10
    >>> get_letter_grade(mark2)
    'Invalid'
    """
    pass


def compute_complex(x: int):
    """
    Return (x^2 + 2x + 4)^2 mod 4.

    >>> x = 10
    >>> compute_complex(x)
    0
    """
    pass


def splice_this(word: str):
    """
    Return every other letter backwards using string splicing.
    Make the last letter of the word the starting point.
    See example below...

    >>> word = "battleship"
    >>> splice_this(word)
    'pheta'
    """
    pass


if __name__ == "__main__":
    doctest.testmod()
