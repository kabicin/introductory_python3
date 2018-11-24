"""
Iterative Binary Search

You may have heard of linear search. Where we search a list to find an element val, such as 2 in the list
[3, 2, 6, 7, 4]. Take a look at the linear_search() method below.

This can become inconvenient as the size as our list grows.
Consider a list of size 1000.
[3, 2, 5, 6, 7, 9, 10, ..........]
In a "best case" scenario, the value we are looking for might just be val = 3.
In which we would only iterate once and exit out of the for loop.

However, in a "worst case" scenario, the element might not even be located inside the list!
This would lead to iterating 1000 times (the length of the list) only to break out of the loop and return -1
to signal that the element was not found.

We can describe the "runtime" of an algorithm generally by its worst case scenario. Because a measure of how "bad" the runtime
can get is much more significant to us as programmers, when deciding how to optimize our code.

Linear search is known to be in O(n) (called "Big-Oh of n")
We would represent linear search as some function T(n) where n represents the input size (in our case len(lst))
and T(n) is simply the runtime in number of "steps" that our code runs.
For example, the linear search example would iterate for 1000 "steps" and since n = 1000, T runs in linear time (n).


More precisely we can say, T is in O(n) or "T is in Big-Oh of n" or "T is in linear time"

Big-Oh represents an upper bound of T. How slow of a runtime we can expect.
Big-Omega represents a lower bound of T. How fast of a runtime we can expect.
Big-Theta represents a "tight" upper and lower bound of T. How our runtime generally behaves.


In binary search, we make one assumption that linear search does not, that the list we are working with must be sorted.
We can perform binary search on a list such as [1, 5, 7, 9, 20, 30] but not [3, 5, 2, 8, 10, 23]
even if the list is slightly sorted, we will not be able to perform a fully accurate binary search unless it remains SORTED.

Whether you sort in ascending/descending order is up to you.
For sake of simplicity, I will assume the list is sorted in ascending order.
Thanks to sorting algorithms such as Merge Sort and Timsort such lists can obtained quite intuitively.

Binary search breaks up the search process into lg(n) steps. (lg means log base 2) So T is in lg(n).
This is exemplified in the code below.

First we must create pointer variables to our data. Let's perform binary search for element 30 on the list [3, 7, 10, 30, 50]
b: begin index
e: end index

Our list looks something like this:
where b = 0, e = len(lst) - 1

[3, 7, 10, 30, 50]
 b             e

Keep searching so long as pointers b and e DO NOT PASS each other.
We then find the midpoint of b and e.
m = (b + e) // 2 = (4 + 0) // 2 = 2

Now our updated list shows:

[3, 7, 10, 30, 50]
 b     m        e

We can see that lst[m] = 10. Well. 10 is less than what we are searching for (val = 30).
Then we can assume 30 will never be found in lower sublist [3, 7, 10] since 10 < 30 would imply 7 < 30 and 3 < 30 as well.
So we set b = m + 1 and our updated list is:

[3, 7, 10, 30, 50]
           b    e

Note: Observe how b will either increment itself to a value m + 1 OR e will decrement itself to a value of m - 1.
At one point, both indexes should cross paths and therefore, exit out of the while loop.


We loop back to the start of the while loop and our loop invariant b <= e is still satisfied.
Then m = (b + e) // 2 = (3 + 4) // 2 = 3

[3, 7, 10, 30, 50]
           b    e
           m

We can check again lst[m] = 30 = val.
We have found the element val in the list and therefore, return the index m = 3.
"""


def linear_search(lst: list, val: int) -> int:
    """
    Returns the index of element val in the list of comparables, lst if it exists.
    Otherwise returns -1.
    """
    for i in range(len(lst)):
        if lst[i] == val:
            return i
    return -1


def binary_search_iterative(lst: list, val: int) -> int:
    """
    Returns the index of element val in the list of comparables, lst if it exists.
    Otherwise returns -1.
    This method of binary search uses an iterative approach.
    """
    b = 0
    e = len(lst) - 1

    while b <= e:
        m = (e + b) // 2
        if lst[m] == val:
            return m
        elif lst[m] > val:
            e = m - 1
        else:  # lst[m] < val
            b = m + 1
    return -1


if __name__ == "__main__":
    print("Linear Search:")
    lst = [1, 2, 3]
    print(lst, "linear search for element", 4, "produces index", linear_search(lst, 4))  # should return -1
    lst = [3, 2, 6, 7, 4]
    print(lst, "linear search for element", 2, "produces index", linear_search(lst, 2))  # should return 1

    print("\nBinary Search: ")
    lst = [1, 2, 3]
    print(lst, "binary search for element", 0, "produces index", binary_search_iterative(lst, 0))  # should return -1
    lst = [3, 7, 10, 30, 50]
    print(lst, "binary search for element", 30, "produces index", binary_search_iterative(lst, 30))  # should return 3
