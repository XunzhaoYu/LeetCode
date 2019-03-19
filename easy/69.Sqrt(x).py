"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
    Input: 4
    Output: 2

Example 2:
    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""


def mySqrt(x):  # 28 ms, faster than 95.18%; 10.7 MB, less than 89.55%
    """
    :type x: int
    :rtype: int
    """
    start, end = 0, x
    while start < end:
        mid = (start + end)//2  # *** (start + end) >> 2
        temp = mid * mid
        if temp < x:  # *** if mid ** 2 <= x < (mid + 1) ** 2
            start = mid+1
        elif temp > x:
            end = mid
        else:
            return mid
    if start * start > x:
        return start - 1
    else:
        return start


def mySqrt2(x):  # 24 ms. faster than 100%
        r = x
        while r * r > x:
            r = (r + x / r) / 2  # why  x/r?
        return r


test_input = 4
print(mySqrt(test_input))  # 2
test_input = 8
print(mySqrt(test_input))  # 2
test_input = 1
print(mySqrt(test_input))  # 1
