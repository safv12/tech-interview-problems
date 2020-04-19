"""
Solution module for the problem Longest Consecutive Sequence.
"""


def solution(input_arr):
    """
    This solution uses a hashset to speed up the
    lookups in the input array
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
