"""
merge_k_sorted_linked_list tests
"""
import unittest
from merge_k_sorted_linked_list import solution
from merge_k_sorted_linked_list import ListNode


class MergeKSortedListsTests(unittest.TestCase):
    """Merge K sorted linked lists test class"""

    def test_given_none(self):
        """
        GIVEN a None input
        WHEN trying to merge the lists
        THEN should return None
        """
        llists = None
        result = solution(llists)
        self.assertEqual(None, result)

    def test_given_empty_array(self):
        """
        GIVEN an empty array
        WHEN trying to merge the lists
        THEN should return an empty linked list
        """
        lists_array = []
        result = solution(lists_array)
        self.assertEqual(None, result)

    def test_merge_single_list(self):
        """
        GIVEN an array with a single list
        WHEN merge the lists
        THEN should return a sorted linked list
        """
        first_list = ListNode(2, ListNode(4, ListNode(5)))
        lists_array = [first_list]
        result = solution(lists_array)

        self.assertEqual(2, result.val)
        self.assertEqual(4, result.next.val)
        self.assertEqual(5, result.next.next.val)

    def test_merge_multiple_lists(self):
        """
        GIVEN an array with multiple lists
        WHEN merge the lists
        THEN should return a sorted linked list
        """
        first_list = ListNode(2, ListNode(4, ListNode(5)))
        second_list = ListNode(-1, ListNode(10))
        third_list = ListNode(0, ListNode(3, ListNode(10)))
        lists_array = [first_list, second_list, third_list]
        result = solution(lists_array)

        self.assertEqual(-1, result.val)
        self.assertEqual(0, result.next.val)
        self.assertEqual(2, result.next.next.val)
        self.assertEqual(3, result.next.next.next.val)
        self.assertEqual(4, result.next.next.next.next.val)
        self.assertEqual(5, result.next.next.next.next.next.val)
        self.assertEqual(10, result.next.next.next.next.next.next.val)
        self.assertEqual(10, result.next.next.next.next.next.next.next.val)
