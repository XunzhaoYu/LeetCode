"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
    Input: 123
    Output: 321

Example 2:
    Input: -123
    Output: -321

Example 3:
    Input: 120
    Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


def reverse(x):  # 28 ms, faster: 88.01%; 10.6 MB, less 89.85%
    """
    :type x: int
    :rtype: int
    """
    temp = abs(x)
    result = 0
    while temp // 10 > 0:
        result = result * 10 + temp % 10
        temp = temp // 10
    result = result * 10 + temp
    if x > 0 and result < 2**31:
        return result
    elif x < 0 and result <= 2**31:
        return -result
    else:
        return 0


def reverse2(x):  # 24 ms, faster: 100.00%; 10.7 MB, less 67.92%
    b = str(abs(x))
    res = int(b[::-1])
    if x > 0 and res < 2 ** 31 - 1:
        return res
    elif x < 0 and res < 2 ** 31:
        return -res
    else:
        return 0


test_input = -1234
print(reverse(test_input))
