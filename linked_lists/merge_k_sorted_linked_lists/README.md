# [HARD] Merge K sorted linked lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

**Example:**

```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

## Clarifications

- Could the array be None? **Yes**
- Could the array be empty? **Yes**
- Are the linked lists in the array sorted? **Yes**
- Are negative numbers in the linked lists? **Yes**
- Are duplicated numbers between the linked lists? **Yes**

## Solution

Try to solve this problem before seeing my solution.

#### Hints
<details><summary>Hint 1</summary>
<p>
Did you try to use a Heap/PriorityQueue?
</p>
</details>

#### Solution
<details><summary>Solution</summary>
<p>

This solution relies in a data structure called Heap or PriorityQueue [here](https://docs.python.org/3/library/heapq.html#theory) a little bit of theory. The steps to solve the problems are:

- Step 1: Validate if the array is None or empty.
- Step 2: Initialize and fill the heap with all the values in all lists.
- Step 3: Retrieve all values from the heap and fill the new linked list.

```python
from queue import PriorityQueue

def solution(lists_arr):
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
```

Time complexity : O(N log k) where K is the number of linked lists.
- The comparison cost is O(log k) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
- There are N nodes in the final linked list.
</p>
</details>
