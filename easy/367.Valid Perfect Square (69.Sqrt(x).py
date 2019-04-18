"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
    Input: 16
    Output: true

Example 2:
    Input: 14
    Output: false
"""


def isPerfectSquare(num: int) -> bool:
    # 36 ms, faster than 83.55%. Best solution from submissions (28 ms).
    start, end = 1, num + 1
    while start < end:
        mid = (start + end) // 2
        square = mid ** 2
        if square < num:
            start = mid + 1
        elif square > num:
            end = mid
        else:
            return True
    return False


