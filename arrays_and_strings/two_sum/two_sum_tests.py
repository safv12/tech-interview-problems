"""
Test cases for the two_sum problem.
"""

import unittest
from two_sum import solution


class TwoSumTests(unittest.TestCase):
    """Test class"""

    def test_empty_array(self):
        """ Given an empty array should return fals"""
        result = solution([], 9)
        self.assertFalse(result)

    def test_with_two_sum(self):
        """
        Given an array with the required elements to
        sum the target, should return true.
        """
        result = solution([3, 1, 1, 2, 4, 100, 2], 7)
        self.assertTrue(result)

    def test_with_no_two_sum(self):
        """
        Given an array without the required elements to
        sum the target, should return false.
        """
        result = solution([2, 4, 6, 8, 10], 15)
        self.assertFalse(result)
