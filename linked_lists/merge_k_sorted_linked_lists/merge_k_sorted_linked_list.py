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
import heapq


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
    # Some validations over the array.
    if lists is None or len(lists) == 0:
        return None

    # Creates a fill the priority queue
    heap = []
    heapq.heapify(heap)
    for head in lists:
        while head is not None:
            heapq.heappush(heap, head.val)
            head = head.next

    # Builds the new linked list
    new_list = ListNode(-1)
    head_node = new_list
    while len(heap) > 0:
        new_list.next = ListNode(heapq.heappop(heap))
        new_list = new_list.next

    return head_node.next
