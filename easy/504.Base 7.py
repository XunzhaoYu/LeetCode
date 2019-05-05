"""
Given an integer, return its base 7 string representation.

Example 1:
    Input: 100
    Output: "202"

Example 2:
    Input: -7
    Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""


def convertToBase7(num: int) -> str:
    # 36 ms, faster than 98.85, same to the best solution from submissions (32 ms).
    n, digit = divmod(abs(num), 7)
    digits = [str(digit)]
    while n != 0:
        n, digit = divmod(n, 7)
        digits.append(str(digit))
    res = ''.join(digits)[::-1]
    return res if num >= 0 else '-' + res