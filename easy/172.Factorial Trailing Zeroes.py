"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
    Input: 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.

Example 2:
    Input: 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
"""


def trailingZeroes(n):  # 24 ms, faster than 69.34%. The best solution from submissions is same to my solution.
    """
    :type n: int
    :rtype: int
    """
    res = 0
    while n>0:
        n /= 5
        res += n
    return res


for i in range(0, 35, 5):
    print(i, trailingZeroes(i))
