# [HARD] Merge K sorted linked lists

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
import heapq

def solution(lists_arr):
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
```

Time complexity of this solution would be O(nk Log k)
</p>
</details>
