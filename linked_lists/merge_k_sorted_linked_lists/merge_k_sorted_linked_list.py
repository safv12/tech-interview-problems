"""
Merge k sorted linked lists and return it as one sorted list.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
from queue import PriorityQueue


class ListNode:
    """Represents a linked list node"""
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


def solution(lists):
    """
    This solution uses a heap data structure to build
    the sorted linked list.
    """
    if lists is None:
        return None

    # Creates a fill the priority queue
    priority_queue = PriorityQueue()
    for linked_list in lists:
        while linked_list is not None:
            priority_queue.put(linked_list.val)
            linked_list = linked_list.next

    # Builds the new linked list
    head = point = ListNode(0)
    while not priority_queue.empty():
        val = priority_queue.get()
        point.next = ListNode(val)
        point = point.next

    return head.next
