"""
Two Sum: Returns true if there are two numbers that added
together give the specified target otherwhise return false.
"""


def solution(arr, target):
    """Solution using a hashset."""
    lookup = set()
    for num in arr:
        complement = target - num
        if complement in lookup:
            return True
        lookup.add(num)
    return False
