from heapq import nlargest, nsmallest
"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
    Input: [1,2,3]
    Output: 6

Example 2:
    Input: [1,2,3,4]
    Output: 24

Note:
    The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""


def maximumProduct(nums):# List[int]) -> int:
    # 80 ms, faster than 78.32%.
    s = sorted(nums)
    posi = s[-2] * s[-3]
    if s[-1] <= 0:
        return s[-1] * posi
    else:
        nega = s[0] * s[1]
        if nega >= posi:
            return nega * s[-1]
        else:
            return posi * s[-1]


def maximumProduct2(nums):# List[int]) -> int:
    # 52 ms, the best solution from submissions.
    s, l = nsmallest(2, nums), nlargest(3, nums)    # *** heapq
    return max(s[0] * s[1] * l[0], l[0] * l[1] * l[2])
