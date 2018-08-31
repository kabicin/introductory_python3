import unittest
from practice_0 import *

"""
How to use:
- Scroll down to the main function and right click 'Run > Unittests .."

Debugging:
- Make sure your working file is called 'practice_0.py'
- Make sure you have not changed the function names.
- Check to see if the function calls in 'self.assertEqual()' match your function names in 'practice_0.py'
"""


class TestPractice0(unittest.TestCase):
    def test_get_letter_grade_a(self):
        self.assertEqual(get_letter_grade(90), 'A')

    def test_get_letter_grade_a_highbound(self):
        self.assertEqual(get_letter_grade(100), 'A')

    def test_get_letter_grade_a_lowbound(self):
        self.assertEquals(get_letter_grade(80), 'A')

    def test_get_letter_grade_b(self):
        self.assertEqual(get_letter_grade(75), 'B')

    def test_get_letter_grade_b_highbound(self):
        self.assertEqual(get_letter_grade(79), 'B')

    def test_get_letter_grade_b_lowbound(self):
        self.assertEquals(get_letter_grade(70), 'B')

    def test_get_letter_grade_c(self):
        self.assertEqual(get_letter_grade(65), 'C')

    def test_get_letter_grade_c_highbound(self):
        self.assertEqual(get_letter_grade(69), 'C')

    def test_get_letter_grade_c_lowbound(self):
        self.assertEquals(get_letter_grade(60), 'C')

    def test_get_letter_grade_d(self):
        self.assertEqual(get_letter_grade(54), 'D')

    def test_get_letter_grade_d_highbound(self):
        self.assertEqual(get_letter_grade(59), 'D')

    def test_get_letter_grade_d_lowbound(self):
        self.assertEquals(get_letter_grade(50), 'D')

    def test_get_letter_grade_r(self):
        self.assertEqual(get_letter_grade(25), 'R')

    def test_get_letter_grade_r_highbound(self):
        self.assertEqual(get_letter_grade(49), 'R')

    def test_get_letter_grade_r_lowbound(self):
        self.assertEquals(get_letter_grade(0), 'R')

    def test_get_letter_grade_closeneg(self):
        self.assertEquals(get_letter_grade(-50), 'Invalid')

    def test_get_letter_grade_farneg(self):
        self.assertEquals(get_letter_grade(-200), 'Invalid')

    def test_get_letter_grade_boundneg(self):
        self.assertEquals(get_letter_grade(-100), 'Invalid')

    def test_get_letter_grade_closepos(self):
        self.assertEquals(get_letter_grade(101), 'Invalid')

    def test_get_letter_grade_farpos(self):
        self.assertEquals(get_letter_grade(200), 'Invalid')

    def test_compute_complex_zero(self):
        self.assertEquals(compute_complex(0), 16)

    def test_compute_complex_smallpos(self):
        self.assertEquals(compute_complex(10), 76)

    def test_compute_complex_medpos(self):
        self.assertEquals(compute_complex(100), 16)

    def test_compute_complex_bigpos(self):
        self.assertEquals(compute_complex(1000), 16)

    def test_compute_complex_smallneg(self):
        self.assertEquals(compute_complex(-10), 6)

    def test_compute_complex_medneg(self):
        self.assertEquals(compute_complex(-100), 66)

    def test_compute_complex_bigneg(self):
        self.assertEquals(compute_complex(-1000), 66)

    def test_splice_this_medword(self):
        self.assertEquals(splice_this("bobob"), 'bbb')

    def test_splice_this_smallword(self):
        self.assertEquals(splice_this("bob"), 'bb')

    def test_splice_this_smallerword(self):
        self.assertEquals(splice_this("b"), 'b')

    def test_splice_this_emptystr(self):
        self.assertEquals(splice_this(''), '')

    def test_splice_this_largeword(self):
        self.assertEquals(splice_this("superbob"), "bbeu")

    def test_splice_this_palindrome(self):
        self.assertEquals(splice_this("racecar"), "rccr")

if __name__ == "__main__":
    unittest.main()
