"""
Given an integer, write a function to determine if it is a power of two.

Example 1:
    Input: 1
    Output: true
    Explanation: 20 = 1

Example 2:
    Input: 16
    Output: true
    Explanation: 24 = 16

Example 3:
    Input: 218
    Output: false
"""


def isPowerOfTwo(n):  # 24 ms, faster than 99.06%. But same as the best solution from submissions (20 ms)
    """
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return False
    while n > 1:
        if n % 2 == 1:
            return False
        else:
            n /= 2
    return True


def isPowerOfTwo2(n):
    return n > 0 and ((n & (n-1)) == 0)  # *** & operation.
