"""
Longest consecutive sequence tests.
"""
import unittest
from longest_consecutive_sequence import solution


class LongestConsecutiveSequenceTests(unittest.TestCase):
    """Test class"""

    def test_empty_array(self):
        """ Given an empty array should return 0"""
        result = solution([])
        self.assertEqual(0, result)

    def test_without_repeated(self):
        """
        Given an array with repeated elements should
        return the longest streak counting repeated only
        once.
        """
        result = solution([3, 1, 2, 4, 100, 2])
        self.assertEqual(4, result)

    def test_no_streak(self):
        """
        Given an array with streaks of 1 element
        should return 1
        """
        result = solution([2, 4, 6, 8, 10])
        self.assertEqual(1, result)

    def test_with_negatives(self):
        """
        Given an array with negative number
        should count the strak normally.
        """
        result = solution([2, 4, 6, 8, -1, 0, 1, 3])
        self.assertEqual(6, result)
