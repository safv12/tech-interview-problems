# Longest consecutive sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

#### Example
**Input**: [3, 2, 100, 5, 20, 4, 21]

**Output**: 4

**Explanation**: The answer is 4 because the longest consecutive sequence is [2, 3, 4, 5] and the sequence length is 4.

### Clarifications

- Could the array contain repeated elements? **Yes**
- Could the array contain repeated elements? **Yes**

### Solution

Try to solve this problem before seeing the solution.

#### Hints
<details><summary>Hint 1</summary>
<p>
Did you try to use a HashSet for lookups?
</p>
</details>
<details><summary>Hint 2</summary>
<p>
Is there a lower consecutive element? If so, you could ignore the current element.
</p>
</details>

#### Solution
<details><summary>Solution</summary>
<p>

Before start to count the longest streak we need to find the lower element in the streak, for this we'll use a HashSet to store all the elements in the array, in this way we'll able to do lookups of the array elements in constant time `O(n)`.

Once we have the HashSet configured we could start to find the streaks for that we'll do the next steps.

- *input**: [5, 2, 3, 1, 4, 100, 200]
- **Step 1** Iterate all over the array to fill our - HashSet. `lookup = {5, 2, 3, 1, 4, 100, 200}`
- **Step 2** Iterate over the array again but for each element look if exist the previous consecutive, if the previous consecutive exists ignore the current number and continue iterating over the array.
- **Step 3**: If the previous consecutive does not exists, then, start to count the current streak from the current number.
- **Step 4** If the current streak is greater than the longest streak we'll replace the longest streak.

```python
def solution(input_arr):
    """
    This solution uses a HashSet to speed up the
    lookups in the input array.
    """
    input_elements = set()
    for number in input_arr:
        input_elements.add(number)

    longest_streak = 0
    for number in input_arr:
        current_streak = 0

        if number - 1 not in input_elements:
            while number in input_elements:
                current_streak += 1
                number += 1

        if current_streak > longest_streak:
            longest_streak = current_streak

    return longest_streak
```

This solution iterates over the array only once, so the time complexity is linear time O(n).
</p>
</details>
