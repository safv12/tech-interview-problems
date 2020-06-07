# Two sum

Returns true if there are two numbers that added together give the specified target otherwhise return false.

**Example**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return true.
```

## Clarifications

- Could the array contain repeated elements? **Yes**
- Is the array sorted? **No**

## Solution

Try to solve this problem before seeing my solution.

#### Hints
<details><summary>Hint 1</summary>
<p>
Did you try to use a HashSet for lookups?
</p>
</details>

#### Solution
<details><summary>Solution</summary>
<p>

For this solution I iterate over the array only once, and for each element in the array I look for the complement in a hashset called seen. If the hashset does not contain the complement then I add the current element to the hashset.

```python
def solution(arr, target):
    seen = set() # This hashset contains the element that I already saw.
    for num in arr: # I iterate over each element in the array.
        complement = target - num # I calculate the complement for the current element.
        if complement in seen: # If I already saw this complement then I return true.
            return True
        seen.add(num) # Otherwise, I add the current number to the seen hashset.
    return False # If there are no more elements then I return false.
```

This solution iterates over the array only once, so the time complexity is linear time O(n).
</p>
</details>
