"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
    Input: 38
    Output: 2
    Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
                 Since 2 has only one digit, return it.

Follow up:
    Could you do it without any loop/recursion in O(1) runtime?
"""


def addDigits(num: int) -> int:  # 40 ms, faster than 99.82%. Best solution from submissions (36 ms)
    return 0 if num == 0 else num % 9 or 9  # idea
