"""
TODO: Implement the following methods below.
Try to use the fact that in a sorted sublist, if a starting element is larger than the comparable element
then, every element from the starting element to the end of the sublist is also larger than the comparable element.

Example:
Consider two sublists
(Note: By construction of merge sort's merge() we can assume both sublists are sorted)

                         x        len(sublist_1)
                         -  -  -
left_sublist:              [3, 6, 7]
right_sublist:              [2, 6, 8]
Starting element:       3 (of the left sublist)
Comparable element:     2 (of the right sublist)

Theorem:
If (starting element) > (comparable element),
Then for every element after and including the starting element, we get (starting element) > (comparable element)
Which produces the result:      # of inversions = (size of left_sublist) - (starting index)

Applying the theorem above:
3 > 2
Then for every element after and including 3, we get 3 > 2, 6 > 2, and 7 > 2
Which produces the result
# of inversions = len(left_sublist) - 0 = 3
"""


def get_inversions_easy(lst: list) -> int:
    """
    Return the number of inversions in a list of comparables using a brute force approach.

    >>> get_inversions_easy([1, 2, 3])
    0
    >>> get_inversions_easy([5, 2, 3])
    2
    >>> get_inversions_easy([4, 2, 3, 1, 6, 7, 8, 9, 10, 5])
    """
    pass


def get_inversions_hard(lst: list) -> int:
    """
    Return the number of inversions in a list of comparables while incorporating merge sort.
    Hint: You can count number of inversions while merge sorting!

    >>> get_inversions_hard([1, 2, 3])
    0
    >>> get_inversions_hard([5, 2, 3])
    2
    >>> get_inversions_hard([4, 2, 3, 1, 6, 7, 8, 9, 10, 5])
    11
    """
    pass
