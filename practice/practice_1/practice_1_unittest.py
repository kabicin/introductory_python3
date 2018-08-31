import unittest
from practice_0 import *

"""
How to use:
- Scroll down to the main function and right click 'Run > Unittests .."

Debugging:
- Make sure your working file is called 'practice_1.py'
- Make sure you have not changed the function names.
- Check to see if the function calls in 'self.assertEqual()' match your function names in 'practice_1.py'
"""

class TestPractice0(unittest.TestCase):
    def test_get_sum_sorted_empty_list(self):
        testlist = []
        self.assertEqual(get_sum_sorted(testlist), 0)

    def test_get_sum_sorted_negative_list(self):
        testlist = [-2, 10, -3]
        self.assertEqual(get_sum_sorted(testlist), 7)

    def test_get_sum_sorted_smalloddsorted_list(self):
        testlist = [1, 2, 5]
        self.assertEqual(get_sum_sorted(testlist), 6)

    def test_get_sum_sorted_smallevensorted_list(self):
        testlist = [2, 4]
        self.assertEqual(get_sum_sorted(testlist), 2)

    def test_get_sum_sorted_smallodddescending_list(self):
        testlist = [10, 3, 2]
        self.assertEqual(get_sum_sorted(testlist), 12)

    def test_get_sum_sorted_smallevendescending_list(self):
        testlist = [10, 1]
        self.assertEqual(get_sum_sorted(testlist), 1)

    def test_get_sum_sorted_smalloddrandom_list(self):
        testlist = [5, 2, 60]
        self.assertEqual(get_sum_sorted(testlist), 62)

    def test_get_sum_sorted_smallevenrandom_list(self):
        testlist = [2, 1]
        self.assertEqual(get_sum_sorted(testlist), 1)

    def test_get_sum_sorted_largeoddsorted_list(self):
        testlist = [1, 2, 5, 9, 10, 20, 26]
        self.assertEqual(get_sum_sorted(testlist), 42)

    def test_get_sum_sorted_largeevensorted_list(self):
        testlist = [2, 4, 10, 200, 201, 500]
        self.assertEqual(get_sum_sorted(testlist), 213)

    def test_get_sum_sorted_largeodddescending_list(self):
        testlist = [1200, 1000, 800, 600, 400, 200, 0]
        self.assertEqual(get_sum_sorted(testlist), 2400)

    def test_get_sum_sorted_largeevendescending_list(self):
        testlist = [1000, 800, 600, 400, 200, 0]
        self.assertEqual(get_sum_sorted(testlist), 1200)

    def test_get_sum_sorted_largeoddrandom_list(self):
        testlist = [0, 20, 60, 40, 10, 25, 3]
        self.assertEqual(get_sum_sorted(testlist), 95)

    def test_get_sum_sorted_largeevenrandom_list(self):
        testlist = [0, 20, 60, 40, 10, 25, 3, 62]
        self.assertEqual(get_sum_sorted(testlist), 95)

    def test_get_keener_empty_lists(self):
        testnames = []
        testmarks = []
        self.assertEqual(get_keener(testnames, testmarks), 'Nobody is a keener')

    def test_get_keener_sorted_list(self):
        testnames = ["Bob", "Bill", "Ricky"]
        testmarks = [10, 50, 67]
        self.assertEqual(get_keener(testnames, testmarks), 'Ricky is a keener')

    def test_get_keener_sorteddescending_list(self):
        testnames = ["Bob", "Bill", "Ricky"]
        testmarks = [100, 50, 20]
        self.assertEqual(get_keener(testnames, testmarks), 'Bob is a keener')

    def test_get_keener_random_list(self):
        testnames = ["Bob", "Bill", "Ricky", "Joseph"]
        testmarks = [30, 10, 100, 30]
        self.assertEqual(get_keener(testnames, testmarks), 'Ricky is a keener')

    def test_amazing_sequence(self):
        self.assertEqual(amazing_sequence(), [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131, 134, 137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173, 176, 179, 182, 185, 188, 191, 194, 197, 200, 203, 206, 209, 212, 215, 218, 221, 224, 227, 230, 233, 236, 239, 242, 245, 248, 251, 254, 257, 260, 263, 266, 269, 272, 275, 278, 281, 284, 287, 290, 293, 296, 299])

if __name__ == "__main__":
    unittest.main()
